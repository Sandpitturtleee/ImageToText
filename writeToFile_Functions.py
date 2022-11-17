import os
from natsort import natsorted

from crop_Functions import crop_Enka_2Artifact, rename_files, clear_lists, crop_Enka_G_Wizard_1, crop_Enka_G_Wizard_2
from detectText_Functions import *


# 1 With a_stat. e_stat, q_stat values
from variables import file_paths, folder_path_data, image_data, file_paths_new, image_data_new, \
    folder_path_Enka_2, folder_path_G_Wizard_1, folder_path_G_Wizard_2


def write_to_file(file_names, data_from_images):
    length = len(image_data[12])
    for x in range(len(file_names)):
        file_names[x] = folder_path_data + file_names[x] + ".txt"
        with open(file_names[x], 'w') as f:
            for y in range(length):
                f.write("%s\n" % data_from_images[x][y])


def combine():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    big_iterator = 1
    rename_files(folder_path_Enka_2)
    rename_files(folder_path_G_Wizard_1)
    rename_files(folder_path_G_Wizard_2)

    for root, dirs, file_names in os.walk(folder_path_Enka_2):
        file_names = natsorted(file_names)
        small_iterator = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_Enka_2 + file_name, 0)
            dim = (1924, 802)
            resized = cv2.resize(image, dim)
            cropped_images = crop_Enka_2Artifact(resized, big_iterator)
            detect_text(cropped_images, folder_path_Enka_2, small_iterator, big_iterator)
            big_iterator = big_iterator + 1
            small_iterator = small_iterator + 1

    for root, dirs, file_names in os.walk(folder_path_G_Wizard_1):
        file_names = natsorted(file_names)
        small_iterator = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_G_Wizard_1 + file_name, 0)
            cropped_images = crop_Enka_G_Wizard_1(image, big_iterator)
            detect_text(cropped_images, folder_path_G_Wizard_1, small_iterator, big_iterator)
            big_iterator = big_iterator + 1
            small_iterator = small_iterator + 1

    for root, dirs, file_names in os.walk(folder_path_G_Wizard_2):
        file_names = natsorted(file_names)
        small_iterator = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_G_Wizard_2 + file_name, 0)
            cropped_images = crop_Enka_G_Wizard_2(image, big_iterator)
            detect_text(cropped_images, folder_path_G_Wizard_2, small_iterator, big_iterator)
            big_iterator = big_iterator + 1
            small_iterator = small_iterator + 1
