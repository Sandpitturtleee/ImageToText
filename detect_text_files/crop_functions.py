import os
import cv2
from natsort import natsorted
from pytesseract import pytesseract

from detect_text_files.detect_text_functions import detect_text
from detect_text_files.supporting_functions import delete_new_images, rename_files, create_output_images_filepaths, \
    save_images
from variables import folder_path_enka, folder_path_wizard1, folder_path_wizard2, crop_values_enka, \
    crop_values_wizard1, crop_values_wizard2


def combine_crop_and_and_rename_functions():
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    big_iterator = 1
    delete_new_images()

    rename_files(folder_path_enka)
    big_iterator = crop_and_detect_images_enka(big_iterator)

    rename_files(folder_path_wizard1)
    big_iterator = crop_and_detect_images_wizard1(big_iterator)

    rename_files(folder_path_wizard2)
    crop_and_detect_images_wizard2(big_iterator)


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


def crop_image_enka(image, big_iterator):
    output_images_filepaths = create_output_images_filepaths(big_iterator)
    cropped_images = crop_images(image, output_images_filepaths, crop_values_enka)
    save_images(output_images_filepaths, cropped_images)
    return cropped_images


def crop_image_wizard1(image, big_iterator):
    output_images_filepaths = create_output_images_filepaths(big_iterator)
    cropped_images = crop_images(image, output_images_filepaths, crop_values_wizard1)
    save_images(output_images_filepaths, cropped_images)
    return cropped_images


def crop_image_wizard2(image, big_iterator):
    output_images_filepaths = create_output_images_filepaths(big_iterator)
    cropped_images = crop_images(image, output_images_filepaths, crop_values_wizard2)
    save_images(output_images_filepaths, cropped_images)
    return cropped_images


def crop_images(image, output_images_filepaths, crop_values):
    cropped_images = [None] * len(output_images_filepaths)
    for x in range(len(output_images_filepaths)):
        cropped_images[x] = image[crop_values[x][0]:crop_values[x][1], crop_values[x][2]:crop_values[x][3]]
    return cropped_images

