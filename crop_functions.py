import cv2
import pytesseract

from detect_Text_functions import *


def crop(image, number):
    folder_path = 'C:/Users/karol/Desktop/Studia/5 Semestr/Programowanie Wieloplatformowe w Qt/ImageToText/venv/images/New/'
    extension_string = '.jpg'
    file_paths_strings = ["character", "lvl", "nick", "id", "bow_name", "set", "refinement", "bow_lvl",
                          "fr_lvl", "aa_lvl", "e_lvl", "q_lvl"]
    file_names_strings = ["character", "lvl", "nick", "id", "bow_name", "set", "refinement", "bow_lvl",
                          "fr_lvl", "aa_lvl", "e_lvl", "q_lvl"]
    crop_values_matrix = [[45, 80, 35, 160], [100, 125, 80, 120], [55, 80, 200, 315], [750, 780, 25, 190],
                          [40, 80, 915, 1300], [725, 795, 880, 1280], [145, 175, 920, 980],
                          [140, 180, 1050, 1090], [145, 175, 80, 120], [495, 518, 630, 658],
                          [608, 631, 635, 661], [725, 750, 637, 660]]

    # Creating filepaths for output images
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = folder_path + file_paths_strings[x] + str(number) + extension_string
        # print(file_paths_strings[x])

    # Creating names for cropped images
    for x in range(len(file_names_strings)):
        file_names_strings[x] = file_names_strings[x] + str(number)
        # print(file_names_strings[x])

    # Cropping images
    for x in range(len(file_names_strings)):
        file_names_strings[x] = image[crop_values_matrix[x][0]:crop_values_matrix[x][1],
                                crop_values_matrix[x][2]:crop_values_matrix[x][3]]

    # Saving images
    for x in range(len(file_paths_strings)):
        cv2.imwrite(file_paths_strings[x], file_names_strings[x])

    # Detecting text
    # for x in range(len(file_names_strings)):
    # functions[x]
    detect_character(file_names_strings[0])
    detect_lvl(file_names_strings[1])
    detect_nick(file_names_strings[2])
    detect_id(file_names_strings[3])
    detect_bow_name(file_names_strings[4])
    detect_set(file_names_strings[5])
    detect_refinement(file_names_strings[6])
    detect_bow_lvl(file_names_strings[7])
    detect_fr_lvl(file_names_strings[8])
    detect_aa_lvl(file_names_strings[9])
    detect_e_lvl(file_names_strings[10])
    detect_q_lvl(file_names_strings[11])
