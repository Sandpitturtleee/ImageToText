from detect_Text_functions import *

file_paths_strings = ["character", "lvl", "nick", "uid",
                      "bow_name", "artifact", "refinement", "bow_lvl",
                      "fr_lvl", "aa_lvl", "e_lvl", "q_lvl",
                      "hp_stat", "atk_stat", "def_stat", "em_stat",
                      "cr_stat", "cd_stat", "er_stat"]
file_paths_strings_New = ["character", "lvl", "nick", "uid",
                          "bow_name", "artifact", "refinement", "bow_lvl",
                          "fr_lvl", "hp_stat", "atk_stat", "def_stat", "em_stat",
                          "cr_stat", "cd_stat", "er_stat"]

path_to_data = "C:/Users/karol/Desktop/Studia/5 Semestr/Programowanie Wieloplatformowe w Qt/ImageToText/venv/Data/"

data_lists = [character_list, lvl_list, nick_list, uid_list, bow_name_list, artifact_list, refinement_list,
              bow_lvl_list, fr_lvl_list, aa_lvl_list, e_lvl_list, q_lvl_list, hp_stat_list, atk_stat_list,
              def_stat_list,
              em_stat_list, cr_stat_list, cd_stat_list, er_stat_list]
data_lists_New = [character_list, lvl_list, nick_list, uid_list, bow_name_list, artifact_list, refinement_list,
                  bow_lvl_list, fr_lvl_list, hp_stat_list, atk_stat_list,
                  def_stat_list,
                  em_stat_list, cr_stat_list, cd_stat_list, er_stat_list]


# 1 With a_stat. e_stat, q_stat values
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
    print("Write")
    for x in range(len(file_paths_strings_New)):
        file_paths_strings_New[x] = path_to_data + file_paths_strings_New[x] + ".txt"
        with open(file_paths_strings_New[x], 'w') as f:
            for y in range(lists_len):
                f.write("%s\n" % data_lists_New[x][y])

