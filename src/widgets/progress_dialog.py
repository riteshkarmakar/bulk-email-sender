import logging
from PySide6.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QTextEdit, QProgressBar, QLabel
from PySide6.QtCore import QDateTime
from worker_thread import EmailSenderThread
from typing import Literal


class ProgressDialog(QDialog):
    def __init__(self, parent, email_thread: EmailSenderThread, total_emails: int) -> None:
        super().__init__(parent)
        self._is_running = False
        self.email_thread = email_thread
        self.total_emails = total_emails
        self.init_ui()
        self.init_signals_slots()

    @staticmethod
    def get_formatted_time() -> str:
        return QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

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

    def init_signals_slots(self) -> None:
        self.email_thread.signals.warning.connect(self.handle_warning_signal)
        self.email_thread.signals.started.connect(self.handle_started_signal)
        self.email_thread.signals.progress.connect(self.handle_progress_signal)
        self.email_thread.signals.log.connect(self.append_log_to_textedit)
        self.email_thread.signals.error.connect(self.handle_error_signal)
        self.email_thread.signals.finished.connect(self.handle_finished_signal)

    def append_log_to_textedit(self, msg: str, color: Literal["RED", "ORNGE", "BLUE", "GREY", "BLACK", "GREEN"] = "BLACK") -> None:
        logging.info(msg)
        self.textedit_log.append(f'<span style="color: {color};">{self.get_formatted_time()} - {msg}</span>')

    def handle_warning_signal(self, msg: str) -> None:
        self._is_running = False
        logging.warning(msg)
        QMessageBox.warning(self, "Invalid Data", msg)

    def handle_started_signal(self) -> None:
        self._is_running = True
        self.show()

    def handle_progress_signal(self, index: int) -> None:
        self.progressbar.setValue(index)

    def handle_error_signal(self, msg: str) -> None:
        self._is_running = False
        self.append_log_to_textedit(msg, "RED")
        QMessageBox.critical(self, "Error!", msg)

    def handle_finished_signal(self) -> None:
        self._is_running = False
        if self.progressbar.value() == self.progressbar.maximum():
            msg = "All emails have been sent successfully!"
            self.append_log_to_textedit(msg, "GREEN")
            QMessageBox.information(self, "Success!", msg)

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
