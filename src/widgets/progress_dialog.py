import logging
from PySide6.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QTextEdit, QProgressBar, QLabel
from worker_thread import EmailSenderThread


class QTextEditLogger(logging.Handler):
    def __init__(self, text_edit: QTextEdit):
        super().__init__()
        self.text_edit = text_edit
        self.level_colors = {
            "DEBUG": "#808080",     # Gray
            "INFO": "#000000",      # Black
            "WARNING": "#FFA500",   # Orange
            "ERROR": "#FF0000",     # Red
            "CRITICAL": "#8B0000",  # Dark Red
        }

    def emit(self, record):
        log_entry = self.format(record)
        color = self.level_colors.get(record.levelname, "#000000")  # Default to black
        colored_message = f'<span style="color: {color};">{log_entry}</span>'
        self.text_edit.append(colored_message)


class ProgressDialog(QDialog):
    def __init__(self, parent, email_thread: EmailSenderThread, total_emails: int) -> None:
        super().__init__(parent)
        self._is_running = False
        self.email_thread = email_thread
        self.total_emails = total_emails
        self.init_ui()
        self.init_signals_slots()
        self.setup_logging()

    def init_ui(self)-> None:
        self.setWindowTitle("Sending Emails")
        self.resize(600, 400)
        self.setContentsMargins(5, 5, 5, 5)
        self.setModal(True)

        # Create widgets
        self.progressbar = QProgressBar(self)
        self.progressbar.setRange(0, self.total_emails)
        self.textedit_log = QTextEdit(self)
        self.textedit_log.setReadOnly(True)

        # Set up layout
        vbox = QVBoxLayout(self)
        vbox.addWidget(QLabel("Progress:", self))
        vbox.addWidget(self.progressbar)
        vbox.addWidget(QLabel("Log:", self))
        vbox.addWidget(self.textedit_log)
        self.setLayout(vbox)

    def setup_logging(self):
        text_edit_handler = QTextEditLogger(self.textedit_log)
        text_edit_handler.setLevel(logging.INFO)
        text_edit_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        logger = logging.getLogger()

        # Remove any existing QTextEditLogger handlers
        old_handlers = [h for h in logger.handlers if isinstance(h, QTextEditLogger)]
        for handler in old_handlers:
            logger.removeHandler(handler)
            handler.close()

        # Add the new QTextEditLogger handler with the updated QTextEdit
        logger.addHandler(text_edit_handler)

    def init_signals_slots(self) -> None:
        self.email_thread.signals.warning.connect(self.handle_warning_signal)
        self.email_thread.signals.started.connect(self.handle_started_signal)
        self.email_thread.signals.progress.connect(self.progressbar.setValue)
        self.email_thread.signals.error.connect(self.handle_error_signal)
        self.email_thread.signals.finished.connect(self.handle_finished_signal)

    def handle_warning_signal(self, msg: str) -> None:
        self._is_running = False
        logging.warning(msg)
        QMessageBox.warning(self, "Invalid Data", msg)

    def handle_started_signal(self) -> None:
        self._is_running = True
        self.show()

    def handle_error_signal(self, msg: str) -> None:
        self._is_running = False
        logging.error(msg)
        QMessageBox.critical(self, "Error!", msg)

    def handle_finished_signal(self) -> None:
        self._is_running = False
        if self.progressbar.value() == self.progressbar.maximum():
            logging.info("All emails have been sent successfully.")
            QMessageBox.information(self, "Success!", "All emails have been sent successfully.")

    def closeEvent(self, event):
        if not self._is_running:
            event.accept()
        else:
            if QMessageBox.question(
                self, "Confirmation", "Are you sure you want to QUIT? Pending emails won't be sent.",
                defaultButton=QMessageBox.StandardButton.No
            ) != QMessageBox.StandardButton.Yes:
                event.ignore()
            else:
                self.email_thread.stop()
                event.accept()
                logging.info("Email-sending process has been stopped.")
