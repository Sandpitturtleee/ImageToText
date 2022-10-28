import os

from detect_Text_functions import *


# 1 With a_stat. e_stat, q_stat values
from variables import file_paths_strings, path_to_data, data_lists, file_paths_strings_New, data_lists_New, folder_path, \
    folder_path_base


def write_to_file1():
    lists_len = len(character_list)
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = path_to_data + file_paths_strings[x] + ".txt"
        with open(file_paths_strings[x], 'w') as f:
            for y in range(lists_len):
                f.write("%s\n" % data_lists[x][y])


# 2 Without a_stat. e_stat, q_stat values
def write_to_file2():
    lists_len = len(character_list)
    for x in range(len(file_paths_strings_New)):
        file_paths_strings_New[x] = path_to_data + file_paths_strings_New[x] + ".txt"
        with open(file_paths_strings_New[x], 'w') as f:
            for y in range(lists_len):
                f.write("%s\n" % data_lists_New[x][y])


def rename():
    count = 1
    # count increase by 1 in each iteration
    # iterate all files from a directory
    for file_name in os.listdir(folder_path_base):
        # Construct old file name
        source = folder_path_base + file_name

        # Adding the count to the new file name and extension
        destination = folder_path_base + "image" + str(count) + ".png"

        # Renaming the file
        os.rename(source, destination)
        count += 1
    print('All Files Renamed')

    print('New Names are')
    # verify the result
    res = os.listdir(folder_path_base)
    print(res)
