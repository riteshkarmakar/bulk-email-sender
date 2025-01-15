import json, logging, requests, pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl, QSettings

from widgets.settings_dialog import SettingsDialog
from widgets.preview_dialog import PreviewDialog
from widgets.progress_dialog import ProgressDialog
from widgets.notepad_widget import Notepad

import constants as const
from ui.main_window_ui import Ui_MainWindow
from worker_thread import EmailSenderThread
from schemas import EmailLoginConfig, EmailData


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.preferences = QSettings("RiteshKarmakar", "Bulk Email Sender")
        self.init_ui()
        self.init_signals_slots()
        self.setup_logging()
        self.show()
        if self.preferences.value("update_check_at_startup", True, type=bool):
            self.check_for_updates()
        
    def init_ui(self):
        self.setWindowTitle(f"Bulk Email Sender {const.CURRENT_VERSION}")
        self.notepad = Notepad()
        self.textedit_layout.addWidget(self.notepad)

        delimiter = "{{ }}".split()
        self.lineedit_subject.setToolTip(
            f"Use `{delimiter[0]}` and `{delimiter[1]}` to include placeholders in the email subject line.\n"
            "Placeholders will be replaced dynamically with actual values from the data file.\n\n"
            "Example:\n"
            f"'Hello, {delimiter[0]}name{delimiter[1]}' will be replaced with 'Hello, Ram' when 'name' is substituted with a value from the data file."
        )
        self.notepad.textEdit.setToolTip(
            f"Use `{delimiter[0]}` and `{delimiter[1]}` to include placeholders in the email body text.\n"
            "Placeholders will be replaced dynamically with actual values from the data file.\n\n"
            "Example:\n"
            f"'Dear {delimiter[0]}name{delimiter[1]},\nYour order {delimiter[0]}order_id{delimiter[1]} has been shipped.'\n"
            "can be replaced with:\n"
            "'Dear Ram,\nYour order #12345 has been shipped.'"
        )

    def init_signals_slots(self):
        self.btn_data_file.clicked.connect(self.browse_data_file)
        self.combobox_sheet_names.currentTextChanged.connect(self.handle_sheet_changed)
        self.btn_attachment_folder.clicked.connect(self.browse_attachment_folder)

        self.action_exit.triggered.connect(QApplication.exit)
        self.action_send_emails.triggered.connect(self.send_emails)
        self.action_clear.triggered.connect(self.clear_fields)
        self.action_settings.triggered.connect(self.change_settings)

        self.action_read_documentation.triggered.connect(
            lambda: QDesktopServices.openUrl(QUrl(const.README_URL)))
        self.action_check_for_updates.triggered.connect(self.check_for_updates)

    def setup_logging(self) -> None:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        # Root logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # Add handler only once to avoid duplicates
        if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
            logger.addHandler(console_handler)

    def check_for_updates(self) -> None:
        response = None
        try:
            response = requests.get(const.UPDATE_URL)
            response.raise_for_status()
        except:
            if self.sender() != self.action_check_for_updates:
                return
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Update Check Failed!")
            msg.setText("Unable to fetch update information.")
            msg.setInformativeText("Please check your internet connection or try again later.")
            msg.setDetailedText(f"Error code: {response.status_code if response != None else "None"}\nURL: {const.UPDATE_URL}")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        
        release_data = response.json()
        latest_version = release_data['tag_name']
        release_page_url = release_data['html_url']
        download_url = release_data['assets'][0]['browser_download_url']
        
        if latest_version > const.CURRENT_VERSION:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Update Available")
            msg.setText(
                f"<h3>A New Version ({latest_version}) is Available!</h3>"
                f"To learn more about what's new, click 'View Details' below.</p>")
            msg.setInformativeText("Would you like to update now?")
            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Help | QMessageBox.StandardButton.Cancel)
            msg.button(QMessageBox.StandardButton.Help).setText("  View Details  ")
            
            # Open the download URL or View Details
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
                QDesktopServices.openUrl(QUrl(download_url))
            elif result == QMessageBox.StandardButton.Help:
                QDesktopServices.openUrl(QUrl(release_page_url))
        else:
            if self.sender() == self.action_check_for_updates:
                QMessageBox.information(
                    self, "No Update Available", f"You are currently using the latest version ({const.CURRENT_VERSION})")

    def change_settings(self) -> None:
        settings_dialog = SettingsDialog(self)
        if settings_dialog.exec():
            logging.debug(f"Settings changed successfully.")

    def browse_data_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Select the Data File.", filter="Spreadsheet File (*.xlsx *.csv)")
        if not path:
            return
        
        self.lineedit_data_file.setText(path)
        self.combobox_sheet_names.clear()
        try:
            if path.endswith(".xlsx"):
                sheet_names = pd.ExcelFile(path).sheet_names
                self.combobox_sheet_names.addItems(sheet_names)
                dataframe = pd.read_excel(path, sheet_names[0])
            else:
                dataframe = pd.read_csv(path)
        except Exception as e:
            logging.exception(f"Failed to read spreadsheet file: {path!r}")
            QMessageBox.critical(self, "Error!", str(e))
        else:
            self.combobox_email_column.clear()
            self.combobox_attachment_column.clear()
            headers = list(dataframe)
            self.combobox_email_column.addItems(headers)
            self.combobox_attachment_column.addItems(headers)
            logging.debug(f"Data file loaded: {path!r}")

    def browse_attachment_folder(self) -> None:
        path = QFileDialog.getExistingDirectory(self, "Select the folder containg the Attachment Files.")
        if path:
            self.lineedit_attachment_folder.setText(path)
            logging.debug(f"Attachment folder selected: {path!r}")

    def handle_sheet_changed(self, sheet_name: str) -> None:
        if not sheet_name:
            return
        dataframe = pd.read_excel(self.lineedit_data_file.text(), sheet_name)
        self.combobox_email_column.clear()
        self.combobox_attachment_column.clear()
        headers = list(dataframe)
        self.combobox_email_column.addItems(headers)
        self.combobox_attachment_column.addItems(headers)

        logging.debug(f"Sheet changed: {sheet_name!r}")

    def clear_fields(self) -> None:
        if self.sender() == self.action_clear:
            if QMessageBox.question(self, "Confirm Clear",
                "This will clear all entries and reset the fields. Do you want to proceed?") != QMessageBox.StandardButton.Yes:
                return
        self.lineedit_data_file.clear()
        self.lineedit_attachment_folder.clear()
        self.lineedit_cc.clear()
        self.lineedit_bcc.clear()
        self.lineedit_subject.clear()

        self.combobox_sheet_names.clear()
        self.combobox_email_column.clear()
        self.combobox_attachment_column.clear()

        self.notepad.clear()
        self.groupbox_attachments.setChecked(False)
        
        logging.debug("Cleared all fields.")

    def get_login_config(self) -> EmailLoginConfig | None:
        login_config: EmailLoginConfig = json.loads(const.LOGIN_CONFIG_PATH.read_text())
        for k, v in login_config.items():
            if k != "name" and not v:
                QMessageBox.warning(self, "Incomplete Login Configuration!", f"The <b>{k}</b> field is empty.")
                self.change_settings()
                return
        
        if not login_config["name"]:
            login_config["name"] = None

        return login_config

    def get_email_data(self) -> EmailData | None:
        # Get dataframe
        path = self.lineedit_data_file.text().strip()
        if not path:
            QMessageBox.warning(self, "Empty Field", "No Data File is selected")
            return None
        try:
            if path.endswith(".xlsx"):
                sheet_name = self.combobox_sheet_names.currentText()
                data_frame = pd.read_excel(path, sheet_name)
            else:
                data_frame = pd.read_csv(path)
        except Exception as e:
            logging.error(f"Failed to read data file: {path!r}")
            QMessageBox.critical(self, "Error!", str(e))

        # Get email column name
        email_column_name = self.combobox_email_column.currentText()

        # Get attachment folder and attachment column name
        if self.groupbox_attachments.isChecked():
            attachment_column_name = self.combobox_attachment_column.currentText()
            attachment_folder = self.lineedit_attachment_folder.text() or None
        else:
            attachment_column_name = None
            attachment_folder = None

        # Get CC and BCC emails
        cc_emails = self.lineedit_cc.text().strip(" ,")
        cc_emails = cc_emails.split(",") if cc_emails else []
        bcc_emails = self.lineedit_bcc.text().strip(" ,")
        bcc_emails = bcc_emails.split(",") if bcc_emails else []

        # Get subject and body templates
        subject = self.lineedit_subject.text()
        plain_body = self.notepad.toPlainText()
        html_body = self.notepad.toHtml()
        if not subject.strip():
            QMessageBox.warning(self, "Empty Field", "No Subject is provied.")
            return
        if not plain_body.strip():
            QMessageBox.warning(self, "Empty Field", "No body is provied.")
            return

        email_data: EmailData = {
            "subject_template": subject,
            "plain_body_template": plain_body,
            "html_body_template": html_body,
            "data_frame": data_frame,
            "email_column_name": email_column_name,
            "attachment_column_name": attachment_column_name,
            "attachment_folder": attachment_folder,
            "cc_emails": cc_emails,
            "bcc_emails": bcc_emails
        }
        return email_data

    def send_emails(self) -> None:
        # Get login config
        login_config = self.get_login_config()
        if not login_config:
            return
        
        # Get email data
        email_data = self.get_email_data()
        if not email_data:
            return
        
        # Show the preview of the dynamic emails
        if self.preferences.value("preview_before_sending", True, type=bool):
            preview_dialog = PreviewDialog(self, login_config, email_data)
            if not preview_dialog.exec():
                return
        
        # Initialize the progress dialog and start sending emails
        self.email_thread = EmailSenderThread(login_config, email_data)
        self.progress_dialog = ProgressDialog(self, self.email_thread, len(email_data["data_frame"]))
        self.email_thread.start()
