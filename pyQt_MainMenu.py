
from pyQt_DetectText import DetectTextWindow
from pyQt_DetectErrors import DetectErrorsWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.detectErrorsWindow = DetectErrorsWindow()
        self.detectTextWindow = DetectTextWindow()
        self.worker = None
        self.thread = None
        self.btn2 = None
        self.btn1 = None
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.setFixedSize(800, 600)

        # Buttons
        self.btn1 = QPushButton('Detect errors', self)
        self.btn1.setGeometry(300, 100, 200, 100)
        self.btn1.clicked.connect(self.toggle_detectErrorsWindow)

        self.btn2 = QPushButton('Detect text and write to file', self)
        self.btn2.setGeometry(300, 300, 200, 100)
        self.btn2.clicked.connect(self.toggle_detectTextWindow)

    def toggle_detectErrorsWindow(self, checked):
        self.hide()
        if self.detectErrorsWindow.isVisible():
            self.detectErrorsWindow.hide()

        else:
            self.detectErrorsWindow.show()

    def toggle_detectTextWindow(self, checked):
        self.hide()
        if self.detectTextWindow.isVisible():
            self.detectTextWindow.hide()

        else:
            self.detectTextWindow.show()

