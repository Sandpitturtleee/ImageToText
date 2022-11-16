import os
from natsort import natsorted

from crop_Functions import crop_Enka_2Artifact, rename, clear_lists, crop_Enka_G_Wizard_1, crop_Enka_G_Wizard_2
from detectText_Functions import *


# 1 With a_stat. e_stat, q_stat values
from variables import file_paths, folder_path_data, image_data, file_paths_new, image_data_new, folder_path, \
    folder_path_Enka_2, folder_path_G_Wizard_1, folder_path_G_Wizard_2


def write_to_file1():
    lists_len = len(image_data[12])
    for x in range(len(file_paths)):
        file_paths[x] = folder_path_data + file_paths[x] + ".txt"
        with open(file_paths[x], 'w') as f:
            for y in range(lists_len):
                f.write("%s\n" % image_data[x][y])
    clear_lists()


# 2 Without a_stat. e_stat, q_stat values
def write_to_file2():
    lists_len = len(image_data[12])
    for x in range(len(file_paths_new)):
        file_paths_new[x] = folder_path_data + file_paths_new[x] + ".txt"
        with open(file_paths_new[x], 'w') as f:
            for y in range(lists_len):
                f.write("%s\n" % image_data_new[x][y])
    clear_lists()


def combine():
    rename(1)
    rename(2)
    rename(3)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    for root, dirs, file_names in os.walk(folder_path_Enka_2):
        file_names = natsorted(file_names)
        number = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_Enka_2 + file_name, 0)
            dim = (1924, 802)
            resized = cv2.resize(image, dim)
            crop_Enka_2Artifact(resized, number)
            number = number + 1

    for root, dirs, file_names in os.walk(folder_path_G_Wizard_1):
        file_names = natsorted(file_names)
        new_number = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_G_Wizard_1 + file_name, 0)
            crop_Enka_G_Wizard_1(image, number, new_number)
            number = number + 1
            new_number = new_number + 1

    for root, dirs, file_names in os.walk(folder_path_G_Wizard_2):
        file_names = natsorted(file_names)
        new_number = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_G_Wizard_2 + file_name, 0)
            crop_Enka_G_Wizard_2(image, number, new_number)
            number = number + 1
            new_number = new_number + 1
