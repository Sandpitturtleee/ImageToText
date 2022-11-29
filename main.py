import sys

from PyQt5.QtWidgets import QApplication

from data_processing_files.variables import refinements_bows, folder_path_data_bows, unique_bow, values_elements, \
    unique_element, folder_path_data_elements, artifact, folder_path_data_artifacts, unique_artifact, \
    unique_artifact_count
from pyQt_files.pyQt_MainMenu import MainMenuWindow
from data_processing_files.supporting_functions import read_values, write_data_to_file, write_artifact_to_file
from data_processing_files.data_manipulation import create_unique_names, group_refinements, group_dmg_bonuses, \
    count_artifacts

if __name__ == '__main__':
    read_values()
    create_unique_names()
    group_refinements()
    group_dmg_bonuses()
    count_artifacts()
    write_data_to_file(folder_path_data_bows, unique_bow, refinements_bows)
    write_data_to_file(folder_path_data_elements, unique_element, values_elements)
    write_artifact_to_file(folder_path_data_artifacts, unique_artifact_count)

    #app = QApplication(sys.argv)
    #win = MainMenuWindow()
    #win.show()
    #sys.exit(app.exec())

