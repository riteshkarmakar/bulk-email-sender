# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_notepad.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTextEdit,
    QToolBar, QVBoxLayout, QWidget)
from ui import resources_rc

class Ui_Notepad(object):
    def setupUi(self, Notepad):
        if not Notepad.objectName():
            Notepad.setObjectName(u"Notepad")
        Notepad.resize(800, 600)
        self.action_save_template = QAction(Notepad)
        self.action_save_template.setObjectName(u"action_save_template")
        icon = QIcon()
        icon.addFile(u":/ui/icons/save_as.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_save_template.setIcon(icon)
        self.action_load_template = QAction(Notepad)
        self.action_load_template.setObjectName(u"action_load_template")
        icon1 = QIcon()
        icon1.addFile(u":/ui/icons/file_open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_load_template.setIcon(icon1)
        self.action_bold = QAction(Notepad)
        self.action_bold.setObjectName(u"action_bold")
        self.action_bold.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/ui/icons/bold.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_bold.setIcon(icon2)
        self.action_italic = QAction(Notepad)
        self.action_italic.setObjectName(u"action_italic")
        self.action_italic.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/ui/icons/italic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_italic.setIcon(icon3)
        self.action_underline = QAction(Notepad)
        self.action_underline.setObjectName(u"action_underline")
        self.action_underline.setCheckable(True)
        icon4 = QIcon()
        icon4.addFile(u":/ui/icons/underlined.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_underline.setIcon(icon4)
        self.action_align_left = QAction(Notepad)
        self.action_align_left.setObjectName(u"action_align_left")
        self.action_align_left.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/ui/icons/align_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_align_left.setIcon(icon5)
        self.action_align_center = QAction(Notepad)
        self.action_align_center.setObjectName(u"action_align_center")
        self.action_align_center.setCheckable(True)
        icon6 = QIcon()
        icon6.addFile(u":/ui/icons/align_cente.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_align_center.setIcon(icon6)
        self.action_align_right = QAction(Notepad)
        self.action_align_right.setObjectName(u"action_align_right")
        self.action_align_right.setCheckable(True)
        icon7 = QIcon()
        icon7.addFile(u":/ui/icons/align_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_align_right.setIcon(icon7)
        self.action_align_justify = QAction(Notepad)
        self.action_align_justify.setObjectName(u"action_align_justify")
        self.action_align_justify.setCheckable(True)
        icon8 = QIcon()
        icon8.addFile(u":/ui/icons/align_justify.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_align_justify.setIcon(icon8)
        self.centralwidget = QWidget(Notepad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        Notepad.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(Notepad)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        Notepad.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_load_template)
        self.toolBar.addAction(self.action_save_template)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_bold)
        self.toolBar.addAction(self.action_italic)
        self.toolBar.addAction(self.action_underline)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_align_left)
        self.toolBar.addAction(self.action_align_center)
        self.toolBar.addAction(self.action_align_right)
        self.toolBar.addAction(self.action_align_justify)

        self.retranslateUi(Notepad)

        QMetaObject.connectSlotsByName(Notepad)
    # setupUi

    def retranslateUi(self, Notepad):
        Notepad.setWindowTitle("")
        self.action_save_template.setText(QCoreApplication.translate("Notepad", u"Save Template", None))
        self.action_load_template.setText(QCoreApplication.translate("Notepad", u"Load Template", None))
        self.action_bold.setText(QCoreApplication.translate("Notepad", u"Bold", None))
        self.action_italic.setText(QCoreApplication.translate("Notepad", u"Italic", None))
        self.action_underline.setText(QCoreApplication.translate("Notepad", u"Underline", None))
        self.action_align_left.setText(QCoreApplication.translate("Notepad", u"Align Left", None))
        self.action_align_center.setText(QCoreApplication.translate("Notepad", u"Align Center", None))
#if QT_CONFIG(tooltip)
        self.action_align_center.setToolTip(QCoreApplication.translate("Notepad", u"Align Center", None))
#endif // QT_CONFIG(tooltip)
        self.action_align_right.setText(QCoreApplication.translate("Notepad", u"Align Right", None))
        self.action_align_justify.setText(QCoreApplication.translate("Notepad", u"Justify", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Notepad", u"toolBar", None))
    # retranslateUi

