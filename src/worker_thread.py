from email_sender.email_sender import EmailSender
from email_sender.data_validator import InvalidDataException
from PySide6.QtCore import QThread

from schemas import EmailLoginConfig, EmailData, WorkerSignals


class EmailSenderThread(QThread):
    def __init__(self, login_config: EmailLoginConfig, email_data: EmailData) -> None:
        super().__init__()
        self.login_config = login_config
        self.email_data = email_data
        self.signals = WorkerSignals()
        self.email_sender = None

    def run(self) -> None:
        self.email_sender = EmailSender(self.login_config, self.signals)
        try:
            self.email_sender.send_emails(self.email_data)
        except InvalidDataException as e:
            self.signals.warning.emit(str(e))
        except Exception as e:
            self.signals.error.emit(str(e))
        else:
            self.signals.finished.emit()

    def stop(self) -> None:
        if self.email_sender:
            self.email_sender.stop()
        