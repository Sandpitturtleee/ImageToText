import sys

from PyQt5.QtWidgets import QApplication

from pyQt_files.pyQt_MainMenu import MainMenuWindow
from data_processing_files.supporting_functions import read_values
from data_processing_files.data_manipulation import create_unique_names, fun

if __name__ == '__main__':
    read_values()
    create_unique_names()
    fun()


    #app = QApplication(sys.argv)
    #win = MainMenuWindow()
    #win.show()
    #sys.exit(app.exec())

