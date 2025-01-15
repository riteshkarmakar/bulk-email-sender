# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_PreviewDialog(object):
    def setupUi(self, PreviewDialog):
        if not PreviewDialog.objectName():
            PreviewDialog.setObjectName(u"PreviewDialog")
        PreviewDialog.resize(700, 650)
        self.verticalLayout = QVBoxLayout(PreviewDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(PreviewDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label = QLabel(PreviewDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineedit_to = QLineEdit(PreviewDialog)
        self.lineedit_to.setObjectName(u"lineedit_to")
        self.lineedit_to.setReadOnly(True)

        self.gridLayout.addWidget(self.lineedit_to, 0, 1, 1, 1)

        self.label_2 = QLabel(PreviewDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineedit_bcc = QLineEdit(PreviewDialog)
        self.lineedit_bcc.setObjectName(u"lineedit_bcc")
        self.lineedit_bcc.setReadOnly(True)

        self.gridLayout.addWidget(self.lineedit_bcc, 2, 1, 1, 1)

        self.label_4 = QLabel(PreviewDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(PreviewDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineedit_cc = QLineEdit(PreviewDialog)
        self.lineedit_cc.setObjectName(u"lineedit_cc")
        self.lineedit_cc.setReadOnly(True)

        self.gridLayout.addWidget(self.lineedit_cc, 1, 1, 1, 1)

        self.lineedit_subject = QLineEdit(PreviewDialog)
        self.lineedit_subject.setObjectName(u"lineedit_subject")
        self.lineedit_subject.setReadOnly(True)

        self.gridLayout.addWidget(self.lineedit_subject, 3, 1, 1, 1)

        self.label_5 = QLabel(PreviewDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.textedit_body = QTextEdit(PreviewDialog)
        self.textedit_body.setObjectName(u"textedit_body")
        self.textedit_body.setReadOnly(True)

        self.gridLayout.addWidget(self.textedit_body, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_previous = QPushButton(PreviewDialog)
        self.btn_previous.setObjectName(u"btn_previous")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_previous.sizePolicy().hasHeightForWidth())
        self.btn_previous.setSizePolicy(sizePolicy)
        self.btn_previous.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.btn_previous)

        self.spinbox_index = QSpinBox(PreviewDialog)
        self.spinbox_index.setObjectName(u"spinbox_index")
        self.spinbox_index.setMinimumSize(QSize(80, 0))
        self.spinbox_index.setAlignment(Qt.AlignCenter)
        self.spinbox_index.setMinimum(1)
        self.spinbox_index.setMaximum(999)

        self.horizontalLayout.addWidget(self.spinbox_index)

        self.btn_next = QPushButton(PreviewDialog)
        self.btn_next.setObjectName(u"btn_next")
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.btn_next)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 1)

        self.listwidget_attachments = QListWidget(PreviewDialog)
        self.listwidget_attachments.setObjectName(u"listwidget_attachments")
        self.listwidget_attachments.setAutoScroll(False)
        self.listwidget_attachments.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.listwidget_attachments.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.listwidget_attachments, 5, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 6)
        self.gridLayout.setRowStretch(5, 2)

        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(PreviewDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btn_send = QPushButton(PreviewDialog)
        self.btn_send.setObjectName(u"btn_send")

        self.horizontalLayout_2.addWidget(self.btn_send)

        self.btn_cancel = QPushButton(PreviewDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(PreviewDialog)
        self.btn_send.clicked.connect(PreviewDialog.accept)
        self.btn_cancel.clicked.connect(PreviewDialog.reject)
        self.btn_next.clicked.connect(self.spinbox_index.stepUp)
        self.btn_previous.clicked.connect(self.spinbox_index.stepDown)

        self.btn_next.setDefault(False)
        self.btn_send.setDefault(True)


        QMetaObject.connectSlotsByName(PreviewDialog)
    # setupUi

    def retranslateUi(self, PreviewDialog):
        PreviewDialog.setWindowTitle(QCoreApplication.translate("PreviewDialog", u"Preview", None))
        self.label_6.setText(QCoreApplication.translate("PreviewDialog", u"Attachments:", None))
        self.label.setText(QCoreApplication.translate("PreviewDialog", u"To:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("PreviewDialog", u"Carbon Copy", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("PreviewDialog", u"CC:", None))
        self.label_4.setText(QCoreApplication.translate("PreviewDialog", u"Subject:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("PreviewDialog", u"Blind Carbon Copy", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("PreviewDialog", u"BCC:", None))
        self.label_5.setText(QCoreApplication.translate("PreviewDialog", u"Body:", None))
#if QT_CONFIG(tooltip)
        self.btn_previous.setToolTip(QCoreApplication.translate("PreviewDialog", u"Previous", None))
#endif // QT_CONFIG(tooltip)
        self.btn_previous.setText(QCoreApplication.translate("PreviewDialog", u"<", None))
        self.spinbox_index.setSuffix("")
#if QT_CONFIG(tooltip)
        self.btn_next.setToolTip(QCoreApplication.translate("PreviewDialog", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.btn_next.setText(QCoreApplication.translate("PreviewDialog", u">", None))
#if QT_CONFIG(tooltip)
        self.listwidget_attachments.setToolTip(QCoreApplication.translate("PreviewDialog", u"Double click on a file path to open it.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_send.setText(QCoreApplication.translate("PreviewDialog", u"   Send Emails   ", None))
        self.btn_cancel.setText(QCoreApplication.translate("PreviewDialog", u"Cancel", None))
    # retranslateUi

