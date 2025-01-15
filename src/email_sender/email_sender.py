import logging, numpy, pandas as pd
from pathlib import Path
from schemas import EmailLoginConfig, EmailData, WorkerSignals

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formataddr
from email import encoders

from email_sender.data_validator import DataValidator
import email_sender.utils as utils


class EmailSender:
    def __init__(self, login_config: EmailLoginConfig, signals: WorkerSignals):
        """Initializes the EmailSender class."""
        self.login_config = login_config
        self.signals = signals

    def _login(self) -> smtplib.SMTP:
        host = self.login_config.get("host", "smtp.gmail.com")
        port = self.login_config.get("port", 587)
        email = self.login_config["email"]
        password = self.login_config["password"]

        server = smtplib.SMTP(host, port)
        server.starttls(context=ssl.create_default_context())
        server.login(email, password)

        logging.info(f"Successfully logged into the email server at {host}:{port}.")

        return server
    
    def _create_email(
        self,
        subject: str,
        plain_body: str,
        html_body: str,
        recipient_email: str,
        cc_emails: list[str] | None,
        attachment_paths: str | Path | list[str | Path] | None,
    ) -> MIMEMultipart:

        # Create the message
        name = self.login_config["name"]
        email = self.login_config["email"]

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message['From'] = formataddr((name, email)) if name else email
        message["To"] = recipient_email
        if cc_emails:
            message['Cc'] = ", ".join(cc_emails)

        # Attach the email body
        message.attach(MIMEText(plain_body, "plain"))
        message.attach(MIMEText(html_body, "html"))

        # Attach attachments (if any)
        if attachment_paths:
            message = self._attach_attachments(message, attachment_paths)

        return message

    def _attach_attachments(
        self,
        message: MIMEMultipart,
        file_paths: str | Path | list[str | Path]
    ) -> MIMEMultipart:

        # Ensure attachments are lists
        if not isinstance(file_paths, list):
            file_paths = [file_paths]

        for path in file_paths:
            path = Path(path)
            # Add file as application/octet-stream. Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(path.read_bytes())
            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)
            # Add header as key/value pair to attachment part
            part.add_header("Content-Disposition", f"attachment; filename={path.name}")
            message.attach(part)

        return message
    
    def _get_row_data(
        self,
        row: pd.Series,
        email_data: EmailData,
        subject_placeholders: list[str],
        body_placeholders: list[str]
    ) -> tuple[str, str, str, list[Path], str]:
        """Extract and process data for a single email row.

        ## Returns:
        `tuple[str, str, str, list[Path], str, list[str], list[str]]`:
            - Processed subject string.
            - Processed plain body string.
            - Processed html body string.
            - List of attachment paths (if any).
            - Recipient email address.
        """
        # Process subject and body
        subject = email_data["subject_template"]
        plain_body = email_data["plain_body_template"]
        html_body = email_data["html_body_template"]

        for placeholder in (subject_placeholders + body_placeholders):
            value = str(row[placeholder]).rstrip(".0") if isinstance(row[placeholder], float) else str(row[placeholder])
            
            subject = subject.replace("{{" + placeholder + "}}", value)
            plain_body = plain_body.replace("{{" + placeholder + "}}", value)
            html_body = html_body.replace("{{" + placeholder + "}}", value)

        # Process attachment paths
        attachment_paths = []
        attachment_column_name = email_data["attachment_column_name"]
        if attachment_column_name:
            comma_separated_paths = row[attachment_column_name]
            if comma_separated_paths:
                for path in utils.get_paths_from_string(str(comma_separated_paths)):
                    if not path.is_absolute():
                        path = email_data["attachment_folder"] / path
                    attachment_paths.append(path)

        # Get recipient email
        recipient_email = str(row[email_data["email_column_name"]])

        return subject, plain_body, html_body, attachment_paths, recipient_email

    def send_emails(self, email_data: EmailData) -> None:
        self._is_running = True

        # Replace Pandas or Numpy Nan with a None
        email_data["data_frame"] = email_data["data_frame"].replace({numpy.nan: None})

        # Get Subject and Body placeholders
        subject_placeholders = utils.get_placeholders(email_data["subject_template"])
        body_placeholders = utils.get_placeholders(email_data["plain_body_template"])

        # validate Email Data
        validator = DataValidator(email_data)
        validator.validate()

        # Emit the started signal
        self.signals.started.emit()

        # Get CC and BCC email
        cc_emails = email_data.get("cc_emails", [])
        bcc_emails = email_data.get("bcc_emails", [])

        server = None
        try:
            # Set up the SMTP connection
            server = self._login()
                
            # Iterate over the dataframe
            for index, row in email_data["data_frame"].iterrows():
                if not self._is_running:
                    return

                # Get processed data for the row
                subject, plain_body, html_body, attachment_paths, recipient_email = self._get_row_data(
                    row, email_data, subject_placeholders, body_placeholders)

                # Create the message
                message = self._create_email(subject, plain_body, html_body, recipient_email, cc_emails, attachment_paths)

                # Send Email
                from_addr = self.login_config["email"]
                to_addrs = [recipient_email] + cc_emails + bcc_emails

                server.sendmail(from_addr, to_addrs, message.as_string())

                # Emit the progress signal
                self.signals.progress.emit(index + 1)

                logging.info(f"Email #{index + 1} successfully sent to recipient: {recipient_email}")

        finally:
            self._is_running = False
            if server:
                server.quit() # Close the SMTP Server

    def stop(self) -> None:
        self._is_running = False
