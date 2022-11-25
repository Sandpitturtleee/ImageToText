import sys

from PyQt5.QtWidgets import QApplication

from pyQt_files.pyQt_MainMenu import MainMenuWindow
from data_processing_files.supporting_functions import read_values
from data_processing_files.data_manipulation import bow_searching

if __name__ == '__main__':
    read_values()
    bow_searching()
    app = QApplication(sys.argv)
    win = MainMenuWindow()
    win.show()
    sys.exit(app.exec())

