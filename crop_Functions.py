import os
import shutil
from natsort import natsorted

from detectText_Functions import *

from variables import folder_path_new, extension_string_jpg, crop_values_Enka2Artifact, extension_string_png, \
    data_lists_New, folder_path_Enka_2, folder_path_errors, folder_path_Enka_1, folder_path_G_Wizard_1, \
    crop_values_G_Wizard_1, folder_path_G_Wizard_2, crop_values_G_Wizard_2


def rename(folder_number):
    if folder_number == 1:
        count = 1
        for file_name in natsorted(os.listdir(folder_path_Enka_2)):
            source = folder_path_Enka_2 + file_name
            destination = folder_path_Enka_2 + "image" + str(count) + ".png"
            os.rename(source, destination)
            count += 1

    elif folder_number == 2:
        count = 1
        for file_name in natsorted(os.listdir(folder_path_G_Wizard_1)):
            source = folder_path_G_Wizard_1 + file_name
            destination = folder_path_G_Wizard_1 + "image" + str(count) + ".png"
            os.rename(source, destination)
            count += 1

    elif folder_number == 3:
        count = 1
        for file_name in natsorted(os.listdir(folder_path_G_Wizard_2)):
            source = folder_path_G_Wizard_2 + file_name
            destination = folder_path_G_Wizard_2 + "image" + str(count) + ".png"
            os.rename(source, destination)
            count += 1


def delete_files():
    for file_name in os.listdir(folder_path_new):
        source = folder_path_new + file_name
        os.remove(source)


def clear_lists():
    for f in range(len(data_lists_New)):
        data_lists_New[f].clear()


def crop_Enka_2Artifact(image, number):
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
    # Creating filepaths for output images
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = folder_path_new + file_paths_strings[x] + str(number) + extension_string_jpg

    # Creating names for cropped images and cropping
    for x in range(len(file_names_strings)):
        file_names_strings[x] = file_names_strings[x] + str(number)
        file_names_strings[x] = image[crop_values_Enka2Artifact[x][0]:crop_values_Enka2Artifact[x][1],
                                crop_values_Enka2Artifact[x][2]:crop_values_Enka2Artifact[x][3]]

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
            # detect_aa_lvl(file_names_strings[9], number)
            # detect_e_lvl(file_names_strings[10], number)
            # detect_q_lvl(file_names_strings[11], number)
            detect_hp_stat(file_names_strings[12], number)
            detect_atk_stat(file_names_strings[13], number)
            detect_def_stat(file_names_strings[14], number)
            detect_em_stat(file_names_strings[15], number)
            detect_cr_stat(file_names_strings[16], number)
            detect_cd_stat(file_names_strings[17], number)
            detect_er_stat(file_names_strings[18], number)
        except ValueError:
            print("imageError" + str(number))
            old_file_path = folder_path_Enka_2 + "image" + str(number) + extension_string_png
            new_file_path = folder_path_errors + "image" + str(number) + extension_string_png
            shutil.move(old_file_path, new_file_path)

    detect_text()


def crop_Enka_G_Wizard_1(image, number, new_number):
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
    # Creating filepaths for output images
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = folder_path_new + file_paths_strings[x] + str(number) + extension_string_jpg
        #print(file_paths_strings[x])

    # Creating names for cropped images and cropping
    for x in range(len(file_names_strings)):
        file_names_strings[x] = file_names_strings[x] + str(number)
        #print(file_names_strings[x])
        file_names_strings[x] = image[crop_values_G_Wizard_1[x][0]:crop_values_G_Wizard_1[x][1],
                                crop_values_G_Wizard_1[x][2]:crop_values_G_Wizard_1[x][3]]

    # Saving images
    for x in range(len(file_paths_strings)):
        #print(file_paths_strings[x])
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
            # detect_aa_lvl(file_names_strings[9], number)
            # detect_e_lvl(file_names_strings[10], number)
            # detect_q_lvl(file_names_strings[11], number)
            detect_hp_stat(file_names_strings[12], number)
            detect_atk_stat(file_names_strings[13], number)
            detect_def_stat(file_names_strings[14], number)
            detect_em_stat(file_names_strings[15], number)
            detect_cr_stat(file_names_strings[16], number)
            detect_cd_stat(file_names_strings[17], number)
            detect_er_stat(file_names_strings[18], number)
        except ValueError:
            print("imageError" + str(number))
            old_file_path = folder_path_G_Wizard_1 + "image" + str(new_number) + extension_string_png
            new_file_path = folder_path_errors + "image" + str(number) + extension_string_png
            shutil.move(old_file_path, new_file_path)

    detect_text()


def crop_Enka_G_Wizard_2(image, number, new_number):
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
    # Creating filepaths for output images
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = folder_path_new + file_paths_strings[x] + str(number) + extension_string_jpg

    # Creating names for cropped images and cropping
    for x in range(len(file_names_strings)):
        file_names_strings[x] = file_names_strings[x] + str(number)
        file_names_strings[x] = image[crop_values_G_Wizard_2[x][0]:crop_values_G_Wizard_2[x][1],
                                crop_values_G_Wizard_2[x][2]:crop_values_G_Wizard_2[x][3]]

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
            # detect_aa_lvl(file_names_strings[9], number)
            # detect_e_lvl(file_names_strings[10], number)
            # detect_q_lvl(file_names_strings[11], number)
            detect_hp_stat(file_names_strings[12], number)
            detect_atk_stat(file_names_strings[13], number)
            detect_def_stat(file_names_strings[14], number)
            detect_em_stat(file_names_strings[15], number)
            detect_cr_stat(file_names_strings[16], number)
            detect_cd_stat(file_names_strings[17], number)
            detect_er_stat(file_names_strings[18], number)
        except ValueError:
            print("imageError" + str(number))
            old_file_path = folder_path_G_Wizard_2 + "image" + str(new_number) + extension_string_png
            new_file_path = folder_path_errors + "image" + str(number) + extension_string_png
            shutil.move(old_file_path, new_file_path)

    detect_text()
