import os

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator

from crop_functions import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel
from write_to_file_functions import write_to_file2


def combine():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    path_to_images = "C:/Users/karol/Desktop/Studia/5 Semestr/Programowanie Wieloplatformowe w Qt/ImageToText/venv/Images/Base/"

    for root, dirs, file_names in os.walk(path_to_images):
        y = 1
        for file_name in file_names:
            image = cv2.imread(path_to_images + file_name, 0)
            dim = (1927, 804)
            resized = cv2.resize(image, dim)
            crop(resized, y)
            y = y + 1


def combine_and_write():
    combine()
    write_to_file2()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello PyQt5')
        self.setFixedSize(800, 600)

        ## Buttons
        self.btn1 = QPushButton('Detect errors', self)
        self.btn1.setGeometry(300, 100,200,100)
        self.btn1.clicked.connect(lambda: combine())

        self.btn2 = QPushButton('Detect text and write to file', self)
        self.btn2.setGeometry(300, 300,200,100)
        self.btn2.clicked.connect(lambda: combine_and_write())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    # combine1()
    # write_to_file2()
