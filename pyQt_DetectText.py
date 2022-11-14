from PyQt5.QtWidgets import QWidget, QPushButton

from crop_Functions import rename, delete_files
from writeToFile_Functions import *

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        delete_files()
        combine()
        write_to_file2()
        self.finished.emit()


class DetectTextWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.MainWindow = None
        self.detectTextButton = None
        self.returnButton = None
        self.worker = None
        self.thread = None
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.setFixedSize(800, 600)

        # Buttons
        self.detectTextButton = QPushButton('Detect text and write to file', self)
        self.detectTextButton.setGeometry(300, 100, 200, 100)
        self.detectTextButton.clicked.connect(self.runLongTask)

        self.returnButton = QPushButton('Return', self)
        self.returnButton.setGeometry(300, 400, 200, 100)
        self.returnButton.clicked.connect(self.toggle_MainMenu)

    def toggle_MainMenu(self, checked):
        self.hide()

    def runLongTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.detectTextButton.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.detectTextButton.setEnabled(True)
        )

