from typing import TypedDict, Optional
from pathlib import Path
from pandas import DataFrame
from PySide6.QtCore import QObject, Signal


class WorkerSignals(QObject):
    started = Signal()
    progress = Signal(int)
    log = Signal(str)
    warning = Signal(str)
    error = Signal(str)
    finished = Signal()


class EmailLoginConfig(TypedDict):
    """A TypedDict representing the login configuration for an email account.

    ## Attributes:
        - `host (str)`: The SMTP server host (e.g., "smtp.gmail.com").
        - `port (int)`: The port number for the SMTP server (e.g., 587 for TLS or 465 for SSL).
        - `email (str)`: The email address of the sender.
        - `name (str)`: The display name of the sender.
        - `password (str)`: The password or authentication token for the email account.
    """
    host: str
    port: str
    email: str
    name: str
    password: str


class EmailData(TypedDict):
    """
    A TypedDict representing the data for sending emails with templates and attachments.

    ## Attributes:
        - `subject_template (str)`: Template for the email subject, with placeholders for dynamic content.
        - `html_body_template (str)`: HTML Template for the email body, with placeholders for dynamic content.
        - `plain_body_template (str)`: Plain Template for the email body, with placeholders for dynamic content.
        - `data_frame (DataFrame)`: The DataFrame containing data to populate the templates.
        - `email_column_name (str)`: The column name in the DataFrame containing recipient email addresses.
        - `attachment_column_name (str)`: The column name in the DataFrame containing file names of attachments (optional).
        - `attachment_folder (Path)`: The folder where attachments are located (optional).
        - `cc_emails (list[str])`: A list of email addresses to be added to the CC field (optional).
        - `bcc_emails (list[str])`: A list of email addresses to be added to the BCC field (optional).
    """
    subject_template: str
    plain_body_template: str
    html_body_template: str
    data_frame: DataFrame
    email_column_name: str
    attachment_column_name: Optional[str]
    attachment_folder: Optional[Path]
    cc_emails: list[str]
    bcc_emails: list[str]
