import sys

from PyQt5.QtWidgets import QApplication

from data_processing_files.variables import refinements_bows, folder_path_data_bows, unique_bow, values_elements, \
    unique_element, folder_path_data_elements, artifact, folder_path_data_artifacts, unique_artifact, \
    unique_artifact_count, unique_bow_count
from pyQt_files.pyQt_MainMenu import MainMenuWindow
from data_processing_files.supporting_functions import read_values, write_data_to_file, write_artifact_to_file, \
    write_bow_to_file, write_to_files
from data_processing_files.data_manipulation import create_unique_names, group_refinements, group_dmg_bonuses, \
    count_artifacts, count_bows, data_processing

if __name__ == '__main__':
    read_values()
    data_processing()
    write_to_files()

    #app = QApplication(sys.argv)
    #win = MainMenuWindow()
    #win.show()
    #sys.exit(app.exec())

