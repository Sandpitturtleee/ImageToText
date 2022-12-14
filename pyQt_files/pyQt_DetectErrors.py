from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from detect_text_files.crop_functions import combine_crop_and_and_rename_functions
from detect_text_files.supporting_functions import delete_new_images, clear_lists
from detect_text_files.variables import image_data


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        delete_new_images()
        combine_crop_and_and_rename_functions()
        clear_lists(image_data)
        self.finished.emit()


class DetectErrorsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.returnButton = None
        self.detectErrorsButton = None
        self.worker = None
        self.thread = None
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.setFixedSize(800, 600)

        # Buttons
        self.detectErrorsButton = QPushButton('Detect errors', self)
        self.detectErrorsButton.setGeometry(300, 100, 200, 100)
        self.detectErrorsButton.clicked.connect(self.runLongTask)

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
        self.detectErrorsButton.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.detectErrorsButton.setEnabled(True)
        )

