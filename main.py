import sys

from PyQt5.QtWidgets import QApplication

from pyQt_files.pyQt_MainMenu import MainMenuWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainMenuWindow()
    win.show()
    sys.exit(app.exec())

