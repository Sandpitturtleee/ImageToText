
from pyQt_files.pyQt_DetectText import DetectTextWindow
from pyQt_files.pyQt_DetectErrors import DetectErrorsWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton


class MainMenuWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.detectErrorsWindow = DetectErrorsWindow()
        self.detectTextWindow = DetectTextWindow()
        self.worker = None
        self.thread = None
        self.detectErrorsButton = None
        self.detectTextButton = None
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.setFixedSize(800, 600)

        # Buttons
        self.detectErrorsButton = QPushButton('Detect errors', self)
        self.detectErrorsButton.setGeometry(300, 100, 200, 100)
        self.detectErrorsButton.clicked.connect(self.toggle_detectErrorsWindow)

        self.detectTextButton = QPushButton('Detect text and write to file', self)
        self.detectTextButton.setGeometry(300, 300, 200, 100)
        self.detectTextButton.clicked.connect(self.toggle_detectTextWindow)

    def toggle_detectErrorsWindow(self, checked):
        if self.detectErrorsWindow.isVisible():
            self.detectErrorsWindow.hide()

        else:
            self.detectErrorsWindow.show()

    def toggle_detectTextWindow(self, checked):
        if self.detectTextWindow.isVisible():
            self.detectTextWindow.hide()

        else:
            self.detectTextWindow.show()

