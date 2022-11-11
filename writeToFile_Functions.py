import os

from crop_Functions import crop_Enka_2Artifact
from detectText_Functions import *


# 1 With a_stat. e_stat, q_stat values
from variables import file_paths_strings, path_to_data, data_lists, file_paths_strings_New, data_lists_New, folder_path, \
    folder_path_Enka_2


def write_to_file1():
    lists_len = len(data_lists[12])
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = path_to_data + file_paths_strings[x] + ".txt"
        with open(file_paths_strings[x], 'w') as f:
            for y in range(lists_len):
                f.write("%s\n" % data_lists[x][y])


# 2 Without a_stat. e_stat, q_stat values
def write_to_file2():
    lists_len = len(data_lists[12])
    for x in range(len(file_paths_strings_New)):
        file_paths_strings_New[x] = path_to_data + file_paths_strings_New[x] + ".txt"
        with open(file_paths_strings_New[x], 'w') as f:
            for y in range(lists_len):
                f.write("%s\n" % data_lists_New[x][y])


def combine():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    for root, dirs, file_names in os.walk(folder_path_Enka_2):
        number = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_Enka_2 + file_name, 0)
            dim = (1927, 804)
            resized = cv2.resize(image, dim)
            crop_Enka_2Artifact(resized, number)
            number = number + 1
