import os
import shutil
from natsort import natsorted

from detectText_Functions import *

from variables import folder_path_new, jpg_extension, png_extension, crop_values_Enka2Artifact, \
    image_data_new, folder_path_Enka_2, folder_path_errors, folder_path_Enka_1, folder_path_G_Wizard_1, \
    crop_values_G_Wizard_1, folder_path_G_Wizard_2, crop_values_G_Wizard_2


def rename_files(folder_path):
    count = 1
    for file_name in natsorted(os.listdir(folder_path)):
        source = folder_path + file_name
        destination = folder_path + "image" + str(count) + ".png"
        os.rename(source, destination)
        count += 1


def delete_files():
    for file_name in os.listdir(folder_path_new):
        source = folder_path_new + file_name
        os.remove(source)


def clear_lists():
    for f in range(len(image_data_new)):
        image_data_new[f].clear()


def create_output_images_filepaths(big_iterator):
    from variables import file_names
    output_images_filepaths = [None] * len(file_names)
    for x in range(len(file_names)):
        output_images_filepaths[x] = folder_path_new + file_names[x] + str(big_iterator) + jpg_extension
    return output_images_filepaths


def crop_images(image, output_images_filepaths, crop_values):
    cropped_images = [None] * len(output_images_filepaths)
    for x in range(len(output_images_filepaths)):
        cropped_images[x] = image[crop_values[x][0]:crop_values[x][1], crop_values[x][2]:crop_values[x][3]]
    return cropped_images


def save_images(output_images_filepaths, cropped_images):
    for x in range(len(output_images_filepaths)):
        cv2.imwrite(output_images_filepaths[x], cropped_images[x])


def crop_Enka_2Artifact(image, big_iterator):
    output_images_filepaths = create_output_images_filepaths(big_iterator)
    cropped_images = crop_images(image, output_images_filepaths, crop_values_Enka2Artifact)
    save_images(output_images_filepaths, cropped_images)
    return cropped_images


def crop_Enka_G_Wizard_1(image, big_iterator):
    output_images_filepaths = create_output_images_filepaths(big_iterator)
    cropped_images = crop_images(image, output_images_filepaths, crop_values_G_Wizard_1)
    save_images(output_images_filepaths, cropped_images)
    return cropped_images


def crop_Enka_G_Wizard_2(image, big_iterator):
    output_images_filepaths = create_output_images_filepaths(big_iterator)
    cropped_images = crop_images(image, output_images_filepaths, crop_values_G_Wizard_2)
    save_images(output_images_filepaths, cropped_images)
    return cropped_images



