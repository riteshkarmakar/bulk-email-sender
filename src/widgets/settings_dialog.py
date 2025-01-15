import json
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QSettings

import constants as const
from schemas import EmailLoginConfig
from ui.settings_dialog_ui import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.preferences = QSettings("RiteshKarmakar", "Bulk Email Sender")
        self.init_ui()
        self.init_signals_slots()

    def init_ui(self) -> None:
        self.lineedit_port.setValidator(QIntValidator())
        self.load_settings()

    def init_signals_slots(self) -> None:
        self.btn_clear.clicked.connect(self.clear)
        self.btn_reset.clicked.connect(self.load_settings)
        self.btn_save.clicked.connect(self.save_settings)
        self.checkbox_password.toggled.connect(
            lambda checked: self.lineedit_password.setEchoMode(QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password))

    def load_settings(self) -> None:
        # Load login config
        if const.LOGIN_CONFIG_PATH.exists():
            login_config: EmailLoginConfig = json.loads(const.LOGIN_CONFIG_PATH.read_text())
        else:
            login_config: EmailLoginConfig = {
                "host": "smtp.gmail.com",
                "port": "587",
                "email": "",
                "name": "",
                "password": "",
            }
            const.LOGIN_CONFIG_PATH.write_text(json.dumps(login_config))

        self.lineedit_host.setText(login_config["host"])
        self.lineedit_port.setText(login_config["port"])
        self.lineedit_email.setText(login_config["email"])
        self.lineedit_name.setText(login_config["name"])
        self.lineedit_password.setText(login_config["password"])

        # Load preferences
        self.checkbox_update_check_at_startup.setChecked(self.preferences.value("update_check_at_startup", True, type=bool))
        self.checkbox_preview_before_sending.setChecked(self.preferences.value("preview_before_sending", True, type=bool))
        
    def clear(self) -> None:
        for lineedit in self.findChildren(QLineEdit):
            lineedit.clear()
        self.checkbox_password.setChecked(False)

    def save_settings(self) -> None:
        # Save love config
        login_config: EmailLoginConfig = {
            "host": self.lineedit_host.text(),
            "port": self.lineedit_port.text(),
            "email": self.lineedit_email.text(),
            "name": self.lineedit_name.text(),
            "password": self.lineedit_password.text()
        }
        const.LOGIN_CONFIG_PATH.write_text(json.dumps(login_config, indent="\t"))

        # Save preferences
        self.preferences.setValue("update_check_at_startup", self.checkbox_update_check_at_startup.isChecked())
        self.preferences.setValue("preview_before_sending", self.checkbox_preview_before_sending.isChecked())

        QMessageBox.information(self, "Settings Saved!", "The login settings and application preferences have been successfully saved.")
        self.accept()


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("WindowsVista")
    dialog = SettingsDialog()
    dialog.show()
    app.exec()
