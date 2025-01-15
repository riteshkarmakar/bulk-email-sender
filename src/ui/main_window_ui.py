# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QToolBar, QVBoxLayout,
    QWidget)
from ui import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 700)
        icon = QIcon()
        icon.addFile(u":/ui/icons/Bulk Email Sender.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        icon1 = QIcon()
        icon1.addFile(u":/ui/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_clear.setIcon(icon1)
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        icon2 = QIcon()
        icon2.addFile(u":/ui/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_settings.setIcon(icon2)
        self.action_send_emails = QAction(MainWindow)
        self.action_send_emails.setObjectName(u"action_send_emails")
        self.action_send_emails.setIcon(icon)
        self.action_check_for_updates = QAction(MainWindow)
        self.action_check_for_updates.setObjectName(u"action_check_for_updates")
        self.action_read_documentation = QAction(MainWindow)
        self.action_read_documentation.setObjectName(u"action_read_documentation")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(15, 15, 15, 15)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupbox_receiver_details = QGroupBox(self.layoutWidget)
        self.groupbox_receiver_details.setObjectName(u"groupbox_receiver_details")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_receiver_details.sizePolicy().hasHeightForWidth())
        self.groupbox_receiver_details.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.groupbox_receiver_details)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(15, 10, 15, 15)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.groupbox_receiver_details)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineedit_data_file = QLineEdit(self.groupbox_receiver_details)
        self.lineedit_data_file.setObjectName(u"lineedit_data_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineedit_data_file.sizePolicy().hasHeightForWidth())
        self.lineedit_data_file.setSizePolicy(sizePolicy1)
        self.lineedit_data_file.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineedit_data_file)

        self.btn_data_file = QPushButton(self.groupbox_receiver_details)
        self.btn_data_file.setObjectName(u"btn_data_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_data_file.sizePolicy().hasHeightForWidth())
        self.btn_data_file.setSizePolicy(sizePolicy2)
        self.btn_data_file.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_5.addWidget(self.btn_data_file)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.groupbox_receiver_details)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.combobox_sheet_names = QComboBox(self.groupbox_receiver_details)
        self.combobox_sheet_names.setObjectName(u"combobox_sheet_names")

        self.verticalLayout_12.addWidget(self.combobox_sheet_names)


        self.verticalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.email_column_label = QLabel(self.groupbox_receiver_details)
        self.email_column_label.setObjectName(u"email_column_label")
        self.email_column_label.setMinimumSize(QSize(225, 0))

        self.verticalLayout_7.addWidget(self.email_column_label)

        self.combobox_email_column = QComboBox(self.groupbox_receiver_details)
        self.combobox_email_column.setObjectName(u"combobox_email_column")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combobox_email_column.sizePolicy().hasHeightForWidth())
        self.combobox_email_column.setSizePolicy(sizePolicy3)
        self.combobox_email_column.setMinimumSize(QSize(0, 0))
        self.combobox_email_column.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_7.addWidget(self.combobox_email_column)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)


        self.verticalLayout_4.addWidget(self.groupbox_receiver_details)

        self.groupbox_attachments = QGroupBox(self.layoutWidget)
        self.groupbox_attachments.setObjectName(u"groupbox_attachments")
        sizePolicy.setHeightForWidth(self.groupbox_attachments.sizePolicy().hasHeightForWidth())
        self.groupbox_attachments.setSizePolicy(sizePolicy)
        font = QFont()
        self.groupbox_attachments.setFont(font)
        self.groupbox_attachments.setCheckable(True)
        self.groupbox_attachments.setChecked(False)
        self.verticalLayout_9 = QVBoxLayout(self.groupbox_attachments)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 10, 15, 15)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.groupbox_attachments)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineedit_attachment_folder = QLineEdit(self.groupbox_attachments)
        self.lineedit_attachment_folder.setObjectName(u"lineedit_attachment_folder")
        self.lineedit_attachment_folder.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineedit_attachment_folder)

        self.btn_attachment_folder = QPushButton(self.groupbox_attachments)
        self.btn_attachment_folder.setObjectName(u"btn_attachment_folder")
        sizePolicy2.setHeightForWidth(self.btn_attachment_folder.sizePolicy().hasHeightForWidth())
        self.btn_attachment_folder.setSizePolicy(sizePolicy2)
        self.btn_attachment_folder.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_attachment_folder)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.attachment_filename_column_label = QLabel(self.groupbox_attachments)
        self.attachment_filename_column_label.setObjectName(u"attachment_filename_column_label")
        self.attachment_filename_column_label.setMinimumSize(QSize(225, 0))
        self.attachment_filename_column_label.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_8.addWidget(self.attachment_filename_column_label)

        self.combobox_attachment_column = QComboBox(self.groupbox_attachments)
        self.combobox_attachment_column.setObjectName(u"combobox_attachment_column")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.combobox_attachment_column.sizePolicy().hasHeightForWidth())
        self.combobox_attachment_column.setSizePolicy(sizePolicy4)
        self.combobox_attachment_column.setMinimumSize(QSize(0, 0))
        self.combobox_attachment_column.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_8.addWidget(self.combobox_attachment_column)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_4.addWidget(self.groupbox_attachments)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.copyright_label = QLabel(self.layoutWidget)
        self.copyright_label.setObjectName(u"copyright_label")
        sizePolicy.setHeightForWidth(self.copyright_label.sizePolicy().hasHeightForWidth())
        self.copyright_label.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.copyright_label)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupbox_carbon_copies = QGroupBox(self.layoutWidget1)
        self.groupbox_carbon_copies.setObjectName(u"groupbox_carbon_copies")
        self.horizontalLayout_3 = QHBoxLayout(self.groupbox_carbon_copies)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 10, 15, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.email_subject_label_2 = QLabel(self.groupbox_carbon_copies)
        self.email_subject_label_2.setObjectName(u"email_subject_label_2")

        self.horizontalLayout.addWidget(self.email_subject_label_2)

        self.lineedit_cc = QLineEdit(self.groupbox_carbon_copies)
        self.lineedit_cc.setObjectName(u"lineedit_cc")

        self.horizontalLayout.addWidget(self.lineedit_cc)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.email_subject_label_3 = QLabel(self.groupbox_carbon_copies)
        self.email_subject_label_3.setObjectName(u"email_subject_label_3")

        self.horizontalLayout_2.addWidget(self.email_subject_label_3)

        self.lineedit_bcc = QLineEdit(self.groupbox_carbon_copies)
        self.lineedit_bcc.setObjectName(u"lineedit_bcc")

        self.horizontalLayout_2.addWidget(self.lineedit_bcc)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.groupbox_carbon_copies)

        self.groupbox_compose = QGroupBox(self.layoutWidget1)
        self.groupbox_compose.setObjectName(u"groupbox_compose")
        self.verticalLayout_2 = QVBoxLayout(self.groupbox_compose)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 10, 15, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.email_subject_label = QLabel(self.groupbox_compose)
        self.email_subject_label.setObjectName(u"email_subject_label")

        self.verticalLayout.addWidget(self.email_subject_label)

        self.lineedit_subject = QLineEdit(self.groupbox_compose)
        self.lineedit_subject.setObjectName(u"lineedit_subject")

        self.verticalLayout.addWidget(self.lineedit_subject)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.textedit_layout = QVBoxLayout()
        self.textedit_layout.setSpacing(7)
        self.textedit_layout.setObjectName(u"textedit_layout")
        self.email_body_label = QLabel(self.groupbox_compose)
        self.email_body_label.setObjectName(u"email_body_label")

        self.textedit_layout.addWidget(self.email_body_label)


        self.verticalLayout_2.addLayout(self.textedit_layout)


        self.verticalLayout_3.addWidget(self.groupbox_compose)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_11.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolbar = QToolBar(MainWindow)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(30, 30))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1150, 26))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.toolbar.addAction(self.action_send_emails)
        self.toolbar.addAction(self.action_clear)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_settings)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_read_documentation)
        self.menuHelp.addAction(self.action_check_for_updates)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bulk Email Sender", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Fields", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.action_send_emails.setText(QCoreApplication.translate("MainWindow", u"Send Emails", None))
        self.action_check_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates...", None))
        self.action_read_documentation.setText(QCoreApplication.translate("MainWindow", u"Read Documentation", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.action_exit.setToolTip(QCoreApplication.translate("MainWindow", u"Exit Application", None))
#endif // QT_CONFIG(tooltip)
        self.groupbox_receiver_details.setTitle(QCoreApplication.translate("MainWindow", u"Receiver Details", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select the Excel Data File:", None))
        self.lineedit_data_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No File Selected.", None))
#if QT_CONFIG(tooltip)
        self.btn_data_file.setToolTip(QCoreApplication.translate("MainWindow", u"Browse Excel Data File", None))
#endif // QT_CONFIG(tooltip)
        self.btn_data_file.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sheet Name:", None))
        self.email_column_label.setText(QCoreApplication.translate("MainWindow", u"Email Column Name:", None))
        self.groupbox_attachments.setTitle(QCoreApplication.translate("MainWindow", u"Attachments", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"Not mandatory if absolute paths are used in the attachment column of the datafile.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Attachments Folder:", None))
#if QT_CONFIG(tooltip)
        self.lineedit_attachment_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Not mandatory if absolute paths are used in the attachment column of the datafile.", None))
#endif // QT_CONFIG(tooltip)
        self.lineedit_attachment_folder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No Folder Selected.", None))
#if QT_CONFIG(tooltip)
        self.btn_attachment_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Browse Attachment Folder", None))
#endif // QT_CONFIG(tooltip)
        self.btn_attachment_folder.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.attachment_filename_column_label.setToolTip(QCoreApplication.translate("MainWindow", u"Multiple files can be attached by separating the filenames using commas.", None))
#endif // QT_CONFIG(tooltip)
        self.attachment_filename_column_label.setText(QCoreApplication.translate("MainWindow", u"Attachment Column Name:", None))
#if QT_CONFIG(tooltip)
        self.combobox_attachment_column.setToolTip(QCoreApplication.translate("MainWindow", u"Filenames must include extensions and be enclosed in quotes. When attaching multiple files, separate them with commas.", None))
#endif // QT_CONFIG(tooltip)
        self.copyright_label.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Ritesh karmakar\n"
"riteshkarmakar7407@gmail.com", None))
        self.groupbox_carbon_copies.setTitle(QCoreApplication.translate("MainWindow", u"Carbon Copies", None))
#if QT_CONFIG(tooltip)
        self.email_subject_label_2.setToolTip(QCoreApplication.translate("MainWindow", u"Carbon Copy: send a copy of the email to someone other than the primary recipient.", None))
#endif // QT_CONFIG(tooltip)
        self.email_subject_label_2.setText(QCoreApplication.translate("MainWindow", u"CC:", None))
#if QT_CONFIG(tooltip)
        self.lineedit_cc.setToolTip(QCoreApplication.translate("MainWindow", u"In case of multiple emails, separate them with commas.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineedit_cc.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineedit_cc.setText("")
        self.lineedit_cc.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.email_subject_label_3.setToolTip(QCoreApplication.translate("MainWindow", u"Blind Carbon Copy: Send a copy of the email to a recipient without their name being visible to other recipients.", None))
#endif // QT_CONFIG(tooltip)
        self.email_subject_label_3.setText(QCoreApplication.translate("MainWindow", u"BCC:", None))
#if QT_CONFIG(tooltip)
        self.lineedit_bcc.setToolTip(QCoreApplication.translate("MainWindow", u"In case of multiple emails, separate them with commas.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineedit_bcc.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineedit_bcc.setText("")
        self.lineedit_bcc.setPlaceholderText("")
        self.groupbox_compose.setTitle(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.email_subject_label.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
#if QT_CONFIG(tooltip)
        self.lineedit_subject.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineedit_subject.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineedit_subject.setText("")
        self.lineedit_subject.setPlaceholderText("")
        self.email_body_label.setText(QCoreApplication.translate("MainWindow", u"Body:", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

