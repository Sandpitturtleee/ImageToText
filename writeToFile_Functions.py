import os
from natsort import natsorted

from crop_Functions import crop_image_enka, rename_files, clear_lists, crop_image_wizard1, crop_image_wizard2, \
    delete_new_images
from detectText_Functions import *


# 1 With a_stat. e_stat, q_stat values
from variables import folder_path_data, image_data, file_paths_new, image_data_new, \
    folder_path_enka, folder_path_wizard1, folder_path_wizard2


def write_data_to_file(file_names, data_from_images):
    length = len(image_data[12])
    for x in range(len(file_names)):
        file_names[x] = folder_path_data + file_names[x] + ".txt"
        with open(file_names[x], 'w') as f:
            for y in range(length):
                f.write("%s\n" % data_from_images[x][y])


def crop_and_detect_images_enka(big_iterator):
    for root, dirs, file_names in os.walk(folder_path_enka):
        file_names = natsorted(file_names)
        small_iterator = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_enka + file_name, 0)
            dim = (1924, 802)
            resized = cv2.resize(image, dim)
            cropped_images = crop_image_enka(resized, big_iterator)
            detect_text(cropped_images, folder_path_enka, small_iterator, big_iterator)
            big_iterator = big_iterator + 1
            small_iterator = small_iterator + 1
    return big_iterator


def crop_and_detect_images_wizard1(big_iterator):
    for root, dirs, file_names in os.walk(folder_path_wizard1):
        file_names = natsorted(file_names)
        small_iterator = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_wizard1 + file_name, 0)
            cropped_images = crop_image_wizard1(image, big_iterator)
            detect_text(cropped_images, folder_path_wizard1, small_iterator, big_iterator)
            big_iterator = big_iterator + 1
            small_iterator = small_iterator + 1
    return big_iterator


def crop_and_detect_images_wizard2(big_iterator):
    for root, dirs, file_names in os.walk(folder_path_wizard2):
        file_names = natsorted(file_names)
        small_iterator = 1
        for file_name in file_names:
            image = cv2.imread(folder_path_wizard2 + file_name, 0)
            cropped_images = crop_image_wizard2(image, big_iterator)
            detect_text(cropped_images, folder_path_wizard2, small_iterator, big_iterator)
            big_iterator = big_iterator + 1
            small_iterator = small_iterator + 1
    return big_iterator


def combine_crop_and_and_rename_functions():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    big_iterator = 1
    delete_new_images()

    rename_files(folder_path_enka)
    big_iterator = crop_and_detect_images_enka(big_iterator)

    rename_files(folder_path_wizard1)
    big_iterator = crop_and_detect_images_wizard1(big_iterator)

    rename_files(folder_path_wizard2)
    crop_and_detect_images_wizard2(big_iterator)








