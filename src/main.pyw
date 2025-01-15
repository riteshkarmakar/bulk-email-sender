import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")
    main_window = MainWindow()
    sys.exit(app.exec())
