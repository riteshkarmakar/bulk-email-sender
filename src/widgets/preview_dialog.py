import os, numpy
from pathlib import Path
from PySide6.QtWidgets import QDialog, QMessageBox

from schemas import EmailLoginConfig, EmailData
import email_sender.utils as utils
from ui.preview_dialog_ui import Ui_PreviewDialog


class PreviewDialog(QDialog, Ui_PreviewDialog):
    def __init__(self, parent, login_config: EmailLoginConfig, email_data: EmailData) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.login_config = login_config
        self.email_data = email_data
        self.dataframe = self.email_data["data_frame"].replace({numpy.nan: ""}) # Replace Pandas or Numpy Nan with ""
        self.init_ui()

    def init_ui(self) -> None:
        total_rows = len(self.dataframe)
        self.spinbox_index.setMaximum(total_rows)
        self.spinbox_index.setSuffix("/" + str(total_rows))
        self.fill_email_details(1)

        self.spinbox_index.valueChanged.connect(self.fill_email_details)
        self.listwidget_attachments.itemDoubleClicked.connect(self.handle_double_click)

    def handle_double_click(self, item) -> None:
        path = Path(item.text())
        try:
            os.startfile(path)
        except Exception as e:
            QMessageBox.critical(self, "Error!", str(e))

    def fill_email_details(self, index: int) -> dict:
        # Convert to 0 based index
        index -= 1

        # Get emails
        to_emails = str(self.dataframe[self.email_data["email_column_name"]].iloc[index])
        cc_emails = ", ".join(self.email_data["cc_emails"] or [])
        bcc_emails = ", ".join(self.email_data["bcc_emails"] or [])

        subject = self.email_data["subject_template"]
        body = self.email_data["html_body_template"]

        headers = list(self.dataframe)
        subject_placeholders = utils.get_placeholders(subject)
        body_placeholders = utils.get_placeholders(body)

        for placeholder in (subject_placeholders + body_placeholders):
            if placeholder in headers:
                value = self.dataframe[placeholder].iloc[index]
                value = str(value).rstrip(".0") if isinstance(value, float) else str(value)
                
                subject = subject.replace("{{" + placeholder + "}}", value)
                body = body.replace("{{" + placeholder + "}}", value)

        # Get attachment paths
        attachment_paths = []
        if self.email_data["attachment_column_name"]:
            comma_separated_paths = self.dataframe[self.email_data["attachment_column_name"]].iloc[index]
            if comma_separated_paths:
                for path in utils.get_paths_from_string(str(comma_separated_paths)):
                    if not path.is_absolute():
                        # Combine the attachment folder with the relative path to get the full path
                        path = (self.email_data["attachment_folder"] or "") / path
                    attachment_paths.append(str(path))

        # Fill details
        self.lineedit_to.setText(to_emails)
        self.lineedit_cc.setText(cc_emails)
        self.lineedit_bcc.setText(bcc_emails)
        self.lineedit_subject.setText(subject)
        self.textedit_body.setText(body)
        self.listwidget_attachments.clear()
        self.listwidget_attachments.addItems(attachment_paths)
