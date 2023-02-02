
from pyQt_files.pyQt_DetectText import DetectTextWindow
from pyQt_files.pyQt_DetectErrors import DetectErrorsWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from data_processing_files.data_manipulation import data_processing
from data_processing_files.supporting_functions import read_values, write_to_files
from detect_text_files.crop_functions import combine_crop_and_and_rename_functions
from detect_text_files.supporting_functions import delete_new_images, write_data_to_file, clear_lists
from detect_text_files.variables import image_data, error_images
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from detect_text_files.crop_functions import combine_crop_and_and_rename_functions
from detect_text_files.supporting_functions import delete_new_images, clear_lists
from detect_text_files.variables import image_data


class DetectErrorsWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        combine_crop_and_and_rename_functions()
        clear_lists(image_data)
        self.finished.emit()


class DetectTextWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        combine_crop_and_and_rename_functions()
        write_data_to_file(image_data)
        clear_lists(image_data)
        self.finished.emit()


class MainMenuWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.processDataButton = None
        self.worker = None
        self.thread = None
        self.detectErrorsButton = None
        self.detectTextButton = None
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Detect Text from Images")
        self.setFixedSize(800, 600)

        # Buttons
        self.detectErrorsButton = QPushButton('Detect errors', self)
        self.detectErrorsButton.setGeometry(300, 100, 200, 100)
        self.detectErrorsButton.clicked.connect(self.detect_errors)

        self.detectTextButton = QPushButton('Detect text and write to file', self)
        self.detectTextButton.setGeometry(300, 250, 200, 100)
        self.detectTextButton.clicked.connect(self.detect_text)
        self.detectTextButton.setEnabled(False)

        self.processDataButton = QPushButton('Preprocess data', self)
        self.processDataButton.setGeometry(300, 400, 200, 100)
        self.processDataButton.clicked.connect(lambda: read_values())
        self.processDataButton.clicked.connect(lambda: data_processing())
        self.processDataButton.clicked.connect(lambda: write_to_files())
        self.processDataButton.setEnabled(False)

    def warning_msg(self):
        QMessageBox.information(self, "Error", "Errors images detected and moved to errors Folder")

    def check_errors(self):
        if len(error_images) > 0:
            self.warning_msg()
            error_images.clear()
        else:
            self.detectTextButton.setEnabled(True)
            error_images.clear()

    def detect_errors(self):
        self.thread = QThread()
        self.worker = DetectErrorsWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

        self.detectErrorsButton.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.check_errors()
        )

    def detect_text(self):
        self.thread = QThread()
        self.worker = DetectTextWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

        # Final resets
        self.detectTextButton.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.processDataButton.setEnabled(True)
        )
