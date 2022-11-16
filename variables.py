file_paths = ["character", "lvl", "nick", "uid",
                      "bow_name", "artifact", "refinement", "bow_lvl",
                      "fr_lvl", "aa_lvl", "e_lvl", "q_lvl",
                      "hp_stat", "atk_stat", "def_stat", "em_stat",
                      "cr_stat", "cd_stat", "er_stat"]
file_names = ["character", "lvl", "nick", "uid",
                      "bow_name", "artifact", "refinement", "bow_lvl",
                      "fr_lvl", "aa_lvl", "e_lvl", "q_lvl",
                      "hp_stat", "atk_stat", "def_stat", "em_stat",
                      "cr_stat", "cd_stat", "er_stat"]

file_paths_new = ["character", "lvl", "nick", "uid",
                          "bow_name", "artifact", "refinement", "bow_lvl",
                          "fr_lvl", "hp_stat", "atk_stat", "def_stat", "em_stat",
                          "cr_stat", "cd_stat", "er_stat"]

folder_path = "D:/projectFiles/Images/"
folder_path_data = "D:/projectFiles/Data/"
folder_path_Enka_1 = "D:/projectFiles/Images/Enka_1/"
folder_path_Enka_2 = "D:/projectFiles/Images/Enka2/"
folder_path_G_Wizard_1 = "D:/projectFiles/Images/G_Wizard_1/"
folder_path_G_Wizard_2 = "D:/projectFiles/Images/G_Wizard_2/"
folder_path_new = "D:/projectFiles/Images/New/"
folder_path_errors = "D:/projectFiles/Images/Errors/"


jpg_extension = '.jpg'
png_extension = '.png'


character = []
lvl = []
nick = []
uid = []
bow_name = []
artifact_set = []
refinement = []
bow_lvl = []
fr_lvl = []
aa_lvl = []
e_lvl = []
q_lvl = []
hp_stat = []
atk_stat = []
def_stat = []
em_stat = []
cr_stat = []
cd_stat = []
er_stat = []

image_data = [character, lvl, nick, uid,
              bow_name, artifact_set, refinement, bow_lvl,
              fr_lvl, aa_lvl, e_lvl, q_lvl,
              hp_stat, atk_stat, def_stat,
              em_stat,
              cr_stat, cd_stat, er_stat]

image_data_new = [character, lvl, nick, uid, bow_name, artifact_set, refinement,
                  bow_lvl, fr_lvl, hp_stat, atk_stat,
                  def_stat,
                  em_stat, cr_stat, cd_stat, er_stat]

crop_values_Enka2Artifact = [[45, 80, 35, 160], [100, 125, 80, 120], [55, 80, 200, 315], [750, 780, 25, 190],
                             [40, 80, 915, 1300], [725, 795, 880, 1280], [145, 175, 920, 980], [140, 180, 1047, 1087],
                             [145, 175, 80, 120], [490, 514, 630, 662], [608, 631, 635, 661], [725, 750, 637, 660],
                             [230, 256, 1193, 1278], [290, 320, 1200, 1278], [350, 380, 1203, 1278],
                             [417, 450, 1209, 1278],
                             [482, 509, 1178, 1255], [541, 569, 1178, 1255], [599, 632, 1178, 1255]]

crop_values_G_Wizard_1 = [[26, 65, 28, 175], [65, 95, 70, 112], [31, 71, 197, 372], [31, 71, 197, 372],
                             [25, 55, 700, 935], [495, 567, 620, 990], [25, 50, 560, 610], [105, 135, 740, 773],
                             [96, 125, 67, 105], [68, 91, 504, 531], [136, 158, 505, 533], [204, 224, 505, 533],
                             [193, 218, 688, 974], [223, 250, 646, 974], [264, 288, 646, 974],
                             [402, 425, 807, 976],
                             [295, 320, 714, 952], [332, 355, 714, 952], [369, 391, 786, 952]]

crop_values_G_Wizard_2 = [[26, 65, 28, 175], [66, 95, 72, 112], [31, 71, 197, 372], [31, 71, 197, 372],
                             [27, 55, 700, 972], [495, 568, 620, 990], [26, 50, 563, 601], [105, 135, 740, 773],
                             [96, 125, 67, 105], [68, 91, 504, 531], [136, 158, 505, 533], [204, 224, 505, 533],
                             [193, 218, 688, 974], [223, 250, 646, 974], [264, 288, 646, 974],
                             [295, 332, 805, 974],
                             [329, 358, 710, 952], [361, 394, 714, 952], [402, 429, 786, 952]]

