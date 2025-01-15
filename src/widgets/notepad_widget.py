from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QFontComboBox, QComboBox, QTextEdit, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QActionGroup, QFont, QKeySequence

from ui.custom_notepad_ui import Ui_Notepad


DEFAULT_TEMPLATE_DIR = r"Email Templates"

class Notepad(QMainWindow, Ui_Notepad):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.combobox_fontfamily = QFontComboBox()
        self.toolBar.insertWidget(self.action_bold, self.combobox_fontfamily)

        self.combobox_fontsize = QComboBox()
        self.toolBar.insertWidget(self.action_bold, self.combobox_fontsize)

        self.init_ui()
        self.init_signals_slots()

    def init_ui(self) -> None:
        Path(DEFAULT_TEMPLATE_DIR).mkdir(exist_ok=True)
        self.textEdit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)

        self.combobox_fontfamily.setToolTip("Select Font Family")
        self.combobox_fontsize.setToolTip("Select Font Size")
        self.combobox_fontsize.addItems(("8", "9", "10", "11", "12", "13", "14", "18", "24", "36", "48", "64", "72", "96", "144", "288"))
        self.combobox_fontsize.setFixedWidth(50)

        action_alignment_group = QActionGroup(self)
        action_alignment_group.setExclusive(True)
        action_alignment_group.addAction(self.action_align_left)
        action_alignment_group.addAction(self.action_align_center)
        action_alignment_group.addAction(self.action_align_right)
        action_alignment_group.addAction(self.action_align_justify)

        self.action_save_template.setShortcut(QKeySequence.StandardKey.SaveAs)
        self.action_load_template.setShortcut(QKeySequence.StandardKey.Open)
        self.action_bold.setShortcut(QKeySequence.StandardKey.Bold)
        self.action_italic.setShortcut(QKeySequence.StandardKey.Italic)
        self.action_underline.setShortcut(QKeySequence.StandardKey.Underline)

        self.textEdit.setFont(QFont("Times New Roman", 12))
        self.textEdit.setFontPointSize(12)

        self.update_format()

    def init_signals_slots(self) -> None:
        self.action_load_template.triggered.connect(self.load_template)
        self.action_save_template.triggered.connect(self.save_template)

        self.textEdit.selectionChanged.connect(self.update_format)

        self.combobox_fontfamily.currentFontChanged.connect(self.textEdit.setCurrentFont)
        self.combobox_fontsize.currentTextChanged.connect(lambda size: self.textEdit.setFontPointSize(float(size)))

        self.action_bold.toggled.connect(
            lambda checked: self.textEdit.setFontWeight(QFont.Weight.Bold if checked else QFont.Weight.Normal))
        self.action_italic.toggled.connect(self.textEdit.setFontItalic)
        self.action_underline.toggled.connect(self.textEdit.setFontUnderline)

        self.action_align_left.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft))
        self.action_align_center.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter))
        self.action_align_right.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight))
        self.action_align_justify.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify))

    def block_signals(self, b: bool):
        self.combobox_fontfamily.blockSignals(b)
        self.combobox_fontsize.blockSignals(b)
        self.action_bold.blockSignals(b)
        self.action_italic.blockSignals(b)
        self.action_underline.blockSignals(b)

    def update_format(self):
        """Update the toolbar when the selection is changed"""
        self.block_signals(True)

        self.combobox_fontfamily.setCurrentFont(self.textEdit.currentFont())
        self.combobox_fontsize.setCurrentText(str(int(self.textEdit.fontPointSize())))

        self.action_bold.setChecked(self.textEdit.fontWeight() == QFont.Weight.Bold)
        self.action_italic.setChecked(self.textEdit.fontItalic())
        self.action_underline.setChecked(self.textEdit.fontUnderline())

        self.action_align_left.setChecked(self.textEdit.alignment() == Qt.AlignmentFlag.AlignLeft)
        self.action_align_center.setChecked(self.textEdit.alignment() == Qt.AlignmentFlag.AlignCenter)
        self.action_align_right.setChecked(self.textEdit.alignment() == Qt.AlignmentFlag.AlignRight)
        self.action_align_justify.setChecked(self.textEdit.alignment() == Qt.AlignmentFlag.AlignJustify)

        self.block_signals(False)

    def load_template(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, "Load Template", DEFAULT_TEMPLATE_DIR, "HTML Document (*.htm *.html);;Text File (*.txt)")
        if path:
            try:
                text = Path(path).read_text()
            except Exception as e:
                QMessageBox.critical(self, "Error!", str(e))
            else:
                self.textEdit.setText(text)

    def save_template(self) -> None:
        path, filter = QFileDialog.getSaveFileName(
            self, "Save Template", DEFAULT_TEMPLATE_DIR, "HTML Document (*.html);;Text File (*.txt)")
        if path:
            try:
                if filter == "HTML Document (*.html)":
                    Path(path).write_text(self.textEdit.toHtml())
                else:
                    Path(path).write_text(self.textEdit.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "Error!", str(e))

    def toPlainText(self) -> str:
        return self.textEdit.toPlainText()

    def toHtml(self) -> str:
        return self.textEdit.toHtml()

    def clear(self) -> None:
        return self.textEdit.clear()


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("WindowsVista")
    window = Notepad()
    window.show()
    app.exec()
