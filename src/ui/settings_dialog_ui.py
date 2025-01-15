# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from ui import resources_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(400, 500)
        SettingsDialog.setMinimumSize(QSize(400, 450))
        icon = QIcon()
        icon.addFile(u":/ui/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsDialog.setWindowIcon(icon)
        SettingsDialog.setModal(False)
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.protocol_groupbox = QGroupBox(SettingsDialog)
        self.protocol_groupbox.setObjectName(u"protocol_groupbox")
        self.gridLayout_5 = QGridLayout(self.protocol_groupbox)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(15, 10, 15, 10)
        self.lineedit_host = QLineEdit(self.protocol_groupbox)
        self.lineedit_host.setObjectName(u"lineedit_host")
        self.lineedit_host.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.lineedit_host, 0, 1, 1, 1)

        self.port_label = QLabel(self.protocol_groupbox)
        self.port_label.setObjectName(u"port_label")

        self.gridLayout_5.addWidget(self.port_label, 1, 0, 1, 1)

        self.lineedit_port = QLineEdit(self.protocol_groupbox)
        self.lineedit_port.setObjectName(u"lineedit_port")
        self.lineedit_port.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.lineedit_port, 1, 1, 1, 1)

        self.host_label = QLabel(self.protocol_groupbox)
        self.host_label.setObjectName(u"host_label")

        self.gridLayout_5.addWidget(self.host_label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.protocol_groupbox)

        self.sender_credentials_groupbox = QGroupBox(SettingsDialog)
        self.sender_credentials_groupbox.setObjectName(u"sender_credentials_groupbox")
        self.gridLayout_4 = QGridLayout(self.sender_credentials_groupbox)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 10, 15, 10)
        self.sender_email_label = QLabel(self.sender_credentials_groupbox)
        self.sender_email_label.setObjectName(u"sender_email_label")

        self.gridLayout_4.addWidget(self.sender_email_label, 0, 0, 1, 1)

        self.sender_name_label = QLabel(self.sender_credentials_groupbox)
        self.sender_name_label.setObjectName(u"sender_name_label")

        self.gridLayout_4.addWidget(self.sender_name_label, 1, 0, 1, 1)

        self.lineedit_name = QLineEdit(self.sender_credentials_groupbox)
        self.lineedit_name.setObjectName(u"lineedit_name")
        self.lineedit_name.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.lineedit_name, 1, 1, 1, 1)

        self.lineedit_email = QLineEdit(self.sender_credentials_groupbox)
        self.lineedit_email.setObjectName(u"lineedit_email")
        self.lineedit_email.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.lineedit_email, 0, 1, 1, 1)

        self.email_password_label = QLabel(self.sender_credentials_groupbox)
        self.email_password_label.setObjectName(u"email_password_label")

        self.gridLayout_4.addWidget(self.email_password_label, 2, 0, 1, 1)

        self.lineedit_password = QLineEdit(self.sender_credentials_groupbox)
        self.lineedit_password.setObjectName(u"lineedit_password")
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        self.lineedit_password.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.lineedit_password, 2, 1, 1, 1)

        self.checkbox_password = QCheckBox(self.sender_credentials_groupbox)
        self.checkbox_password.setObjectName(u"checkbox_password")

        self.gridLayout_4.addWidget(self.checkbox_password, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.sender_credentials_groupbox)

        self.placeholder_delimiter_groupbox_2 = QGroupBox(SettingsDialog)
        self.placeholder_delimiter_groupbox_2.setObjectName(u"placeholder_delimiter_groupbox_2")
        self.verticalLayout_2 = QVBoxLayout(self.placeholder_delimiter_groupbox_2)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 10, 15, 10)
        self.checkbox_update_check_at_startup = QCheckBox(self.placeholder_delimiter_groupbox_2)
        self.checkbox_update_check_at_startup.setObjectName(u"checkbox_update_check_at_startup")
        self.checkbox_update_check_at_startup.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkbox_update_check_at_startup)

        self.checkbox_preview_before_sending = QCheckBox(self.placeholder_delimiter_groupbox_2)
        self.checkbox_preview_before_sending.setObjectName(u"checkbox_preview_before_sending")
        self.checkbox_preview_before_sending.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkbox_preview_before_sending)


        self.verticalLayout.addWidget(self.placeholder_delimiter_groupbox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(SettingsDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_clear = QPushButton(self.frame)
        self.btn_clear.setObjectName(u"btn_clear")
        icon1 = QIcon()
        icon1.addFile(u":/ui/icons/clear_all.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_clear)

        self.btn_reset = QPushButton(self.frame)
        self.btn_reset.setObjectName(u"btn_reset")
        icon2 = QIcon()
        icon2.addFile(u":/ui/icons/reset_settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reset.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_reset)

        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        icon3 = QIcon()
        icon3.addFile(u":/ui/icons/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(SettingsDialog)

        self.btn_save.setDefault(True)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.protocol_groupbox.setTitle(QCoreApplication.translate("SettingsDialog", u"SMTP Protocol", None))
        self.lineedit_host.setText("")
        self.lineedit_host.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"SMTP Server Address", None))
        self.port_label.setText(QCoreApplication.translate("SettingsDialog", u"Port:", None))
        self.lineedit_port.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"SMTP port", None))
        self.host_label.setText(QCoreApplication.translate("SettingsDialog", u"Host:", None))
        self.sender_credentials_groupbox.setTitle(QCoreApplication.translate("SettingsDialog", u"Sender Credentials", None))
        self.sender_email_label.setText(QCoreApplication.translate("SettingsDialog", u"Email ID:", None))
        self.sender_name_label.setText(QCoreApplication.translate("SettingsDialog", u"Name:", None))
        self.lineedit_name.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"Enter your Full Name", None))
        self.lineedit_email.setText("")
        self.lineedit_email.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"Enter your Email Address", None))
        self.email_password_label.setText(QCoreApplication.translate("SettingsDialog", u"Password:", None))
        self.lineedit_password.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"Enter your Password (App Password)", None))
        self.checkbox_password.setText(QCoreApplication.translate("SettingsDialog", u"Show Password", None))
        self.placeholder_delimiter_groupbox_2.setTitle(QCoreApplication.translate("SettingsDialog", u"Preferences", None))
        self.checkbox_update_check_at_startup.setText(QCoreApplication.translate("SettingsDialog", u"Check for updates at startup.", None))
        self.checkbox_preview_before_sending.setText(QCoreApplication.translate("SettingsDialog", u"Show preview before sending e-mails.", None))
        self.btn_clear.setText(QCoreApplication.translate("SettingsDialog", u"Clear", None))
        self.btn_reset.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
        self.btn_save.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
    # retranslateUi

