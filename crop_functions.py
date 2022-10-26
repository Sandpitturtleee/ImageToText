import cv2
import pytesseract

from detect_Text_functions import *
import shutil


def crop(image, number):
    folder_path = 'C:/Users/karol/Desktop/Studia/5 Semestr/Programowanie Wieloplatformowe w Qt/ImageToText/venv/Images/'
    extension_string_jpg = '.jpg'
    extension_string_png = '.png'
    file_paths_strings = ["character", "lvl", "nick", "uid",
                          "bow_name", "artifact", "refinement", "bow_lvl",
                          "fr_lvl", "aa_lvl", "e_lvl", "q_lvl",
                          "hp_stat", "atk_stat", "def_stat", "em_stat",
                          "cr_stat", "cd_stat", "er_stat"]
    file_names_strings = ["character", "lvl", "nick", "uid",
                          "bow_name", "artifact", "refinement", "bow_lvl",
                          "fr_lvl", "aa_lvl", "e_lvl", "q_lvl",
                          "hp_stat", "atk_stat", "def_stat", "em_stat",
                          "cr_stat", "cd_stat", "er_stat"]
    crop_values_matrix = [[45, 80, 35, 160], [100, 125, 80, 120], [55, 80, 200, 315], [750, 780, 25, 190],
                          [40, 80, 915, 1300], [725, 795, 880, 1280], [145, 175, 920, 980], [140, 180, 1050, 1085],
                          [145, 175, 80, 120], [495, 518, 630, 658], [608, 631, 635, 661], [725, 750, 637, 660],
                          [230, 256, 1193, 1278], [290, 320, 1200, 1278], [355, 380, 1203, 1278],
                          [422, 450, 1209, 1278],
                          [482, 509, 1178, 1255], [541, 569, 1178, 1255], [604, 632, 1178, 1255]]
    # Creating filepaths for output images
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = folder_path + "New/" + file_paths_strings[x] + str(number) + extension_string_jpg
        # print(file_paths_strings[x])

    # Creating names for cropped images and cropping
    for x in range(len(file_names_strings)):
        file_names_strings[x] = file_names_strings[x] + str(number)
        file_names_strings[x] = image[crop_values_matrix[x][0]:crop_values_matrix[x][1],
                                crop_values_matrix[x][2]:crop_values_matrix[x][3]]
        # print(file_names_strings[x])

    # Saving images
    for x in range(len(file_paths_strings)):
        cv2.imwrite(file_paths_strings[x], file_names_strings[x])

    def detect_text():
        try:
            detect_character(file_names_strings[0], number)
            detect_lvl(file_names_strings[1], number)
            detect_nick(file_names_strings[2], number)
            detect_uid(file_names_strings[3], number)
            detect_bow_name(file_names_strings[4], number)
            detect_artifact(file_names_strings[5], number)
            detect_refinement(file_names_strings[6], number)
            detect_bow_lvl(file_names_strings[7], number)
            detect_fr_lvl(file_names_strings[8], number)
            #detect_aa_lvl(file_names_strings[9], number)
            #detect_e_lvl(file_names_strings[10], number)
            #detect_q_lvl(file_names_strings[11], number)
            detect_hp_stat(file_names_strings[12], number)
            detect_atk_stat(file_names_strings[13], number)
            detect_def_stat(file_names_strings[14], number)
            detect_em_stat(file_names_strings[15], number)
            detect_cr_stat(file_names_strings[16], number)
            detect_cd_stat(file_names_strings[17], number)
            detect_er_stat(file_names_strings[18], number)
        except ValueError:
            print("image" + str(number))
            old_file_path = folder_path + "Base/image" + str(number) + extension_string_png
            new_file_path = folder_path + "Errors/image" + str(number) + extension_string_png
            shutil.move(old_file_path, new_file_path)
    detect_text()
