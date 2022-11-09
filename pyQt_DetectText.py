from PyQt5.QtWidgets import QWidget, QPushButton

from crop_Functions import *
from writeToFile_Functions import *

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        combine()
        write_to_file2()
        self.finished.emit()


class DetectTextWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.thread = None
        self.btn2 = None
        self.btn1 = None
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.setFixedSize(800, 600)

        # Buttons
        self.btn1 = QPushButton('Detect text and write to file', self)
        self.btn1.setGeometry(300, 100, 200, 100)
        self.btn1.clicked.connect(self.runLongTask)

    def toggle_window1(self, checked):
        self.hide()
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

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
        self.btn1.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.btn1.setEnabled(True)
        )

