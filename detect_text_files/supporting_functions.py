import os
import shutil
import cv2
from natsort import natsorted

from detect_text_files.variables import jpg_extension, png_extension, folder_path_errors, folder_path_new, image_data, folder_path_data, \
    file_names


def move_files(folder_path, small_iterator, big_iterator):
    old_file_path = folder_path + "image" + str(small_iterator) + png_extension
    new_file_path = folder_path_errors + "image" + str(big_iterator) + png_extension
    shutil.move(old_file_path, new_file_path)


def rename_files(folder_path):
    count = 1
    for file_name in natsorted(os.listdir(folder_path)):
        source = folder_path + file_name
        destination = folder_path + "image" + str(count) + ".png"
        os.rename(source, destination)
        count += 1


def save_images(output_images_filepaths, cropped_images):
    for x in range(len(output_images_filepaths)):
        cv2.imwrite(output_images_filepaths[x], cropped_images[x])


def delete_new_images():
    for file_name in os.listdir(folder_path_new):
        source = folder_path_new + file_name
        os.remove(source)


def create_output_images_filepaths(big_iterator):
    output_images_filepaths = [None] * len(file_names)
    for x in range(len(file_names)):
        output_images_filepaths[x] = folder_path_new + file_names[x] + str(big_iterator) + jpg_extension
    return output_images_filepaths


def write_data_to_file(data_from_images):
    output_txt_filepaths = [None] * len(file_names)
    length = len(image_data[12])
    for x in range(len(output_txt_filepaths)):
        output_txt_filepaths[x] = folder_path_data + file_names[x] + ".txt"
        with open(output_txt_filepaths[x], 'w', encoding='utf-8') as f:
            for y in range(length):
                f.write("%s\n" % data_from_images[x][y])


def clear_lists(data_from_images):
    for f in range(len(data_from_images)):
        data_from_images[f].clear()







