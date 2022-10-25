import sys

import cv2
import pytesseract

character_list = []
lvl_list = []
nick_list = []
uid_list = []
bow_name_list = []
artifact_list = []
refinement_list = []
bow_lvl_list = []
fr_lvl_list = []
aa_lvl_list = []
e_lvl_list = []
q_lvl_list = []
hp_stat_list = []
atk_stat_list = []
def_stat_list = []
em_stat_list = []
cr_stat_list = []
cd_stat_list = []
er_stat_list = []


# cv2.imshow('thresh', image)

def detect_character(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
        character = str(data)
        character_list.append(character)
        return character_list
    except ValueError:
        character_list.append("Error_character" + str(number))


def detect_lvl(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        lvl = int(data)
        if lvl < 10:
            lvl_list.append("lvl" + str(number))
        else:
            lvl_list.append(lvl)
        return lvl_list
    except ValueError:
        lvl_list.append("Error_lvl" + str(number))


def detect_nick(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
        nick = str(data)
        nick_list.append(nick)
        return nick_list
    except ValueError:
        nick_list.append("Error_nick" + str(number))


def detect_uid(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        uid = data
        if len(uid) != 10 and len(uid) != 0:
            uid_list.append("uid" + str(number))
        else:
            uid_list.append(uid)
        return uid_list
    except ValueError:
        uid_list.append("Error_uid" + str(number))


def detect_bow_name(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
        bow_name = str(data)
        bow_name_list.append(bow_name)
        return bow_name_list
    except ValueError:
        bow_name_list.append("Error_bow_name" + str(number))


def detect_artifact(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
        artifact = str(data)
        artifact_list.append(artifact)
        return artifact_list
    except ValueError:
        artifact_list.append("Error_artifact" + str(number))


def detect_refinement(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=12345')
        refinement = int(data)
        if refinement < 1 or refinement > 5:
            refinement_list.append("refinement" + str(number))
        else:
            refinement_list.append(refinement)
        return refinement_list
    except ValueError:
        refinement_list.append("Error_refinement" + str(number))


def detect_bow_lvl(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        bow_lvl = int(data)
        if bow_lvl < 10:
            bow_lvl_list.append("bow_lvl" + str(number))
        else:
            bow_lvl_list.append(bow_lvl)
        return bow_lvl_list
    except ValueError:
        bow_lvl_list.append("Error_bow_lvl" + str(number))


def detect_fr_lvl(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        fr_lvl = int(data)
        if fr_lvl < 1:
            fr_lvl_list.append("fr_lvl" + str(number))
        else:
            fr_lvl_list.append(fr_lvl)
        return fr_lvl_list
    except ValueError:
        fr_lvl_list.append("Error_fr_lvl" + str(number))


def detect_aa_lvl(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        aa_lvl = int(data)
        if aa_lvl < 1 or aa_lvl > 10:
            aa_lvl_list.append("aa_lvl" + str(number))
        else:
            aa_lvl_list.append(aa_lvl)
        return aa_lvl_list
    except ValueError:
        aa_lvl_list.append("Error_aa_lvl" + str(number))


def detect_e_lvl(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        e_lvl = int(data)
        if e_lvl < 1 or e_lvl > 13:
            e_lvl_list.append("e_lvl" + str(number))
        else:
            e_lvl_list.append(e_lvl)
        return e_lvl_list
    except ValueError:
        e_lvl_list.append("Error_e_lvl" + str(number))


def detect_q_lvl(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        q_lvl = int(data)
        if q_lvl < 1 or q_lvl > 13:
            q_lvl_list.append("q_lvl" + str(number))
        else:
            q_lvl_list.append(q_lvl)
        return q_lvl_list
    except ValueError:
        q_lvl_list.append("Error_q_lvl" + str(number))


def detect_hp_stat(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        hp_stat = int(data)
        if hp_stat < 10000:
            hp_stat_list.append("hp_stat" + str(number))
        else:
            hp_stat_list.append(hp_stat)
        return hp_stat_list
    except ValueError:
        hp_stat_list.append("Error_hp_stat" + str(number))


def detect_atk_stat(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        atk_stat = int(data)
        if atk_stat < 1000:
            atk_stat_list.append("atk_stat" + str(number))
        else:
            atk_stat_list.append(atk_stat)
        return atk_stat_list
    except ValueError:
        atk_stat_list.append("Error_atk_stat" + str(number))


def detect_def_stat(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        def_stat = int(data)
        if def_stat < 100:
            def_stat_list.append("def_stat" + str(number))
        else:
            def_stat_list.append(def_stat)
        return def_stat_list
    except ValueError:
        def_stat_list.append("Error_def_stat" + str(number))


def detect_em_stat(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        em_stat = int(data)
        em_stat_list.append(em_stat)
        return em_stat_list
    except ValueError:
        em_stat_list.append("Error_em_stat" + str(number))


def detect_cr_stat(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
        cr_stat = float(data)
        if cr_stat < 10:
            cr_stat_list.append("cr_stat" + str(number))
        else:
            cr_stat_list.append(cr_stat)
        return cr_stat_list
    except ValueError:
        cr_stat_list.append("Error_cr_stat" + str(number))


def detect_cd_stat(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
        cd_stat = float(data)
        if cd_stat < 50:
            cd_stat_list.append("cd_stat" + str(number))
        else:
            cd_stat_list.append(cd_stat)
        return cd_stat_list
    except ValueError:
        cd_stat_list.append("Error_cd_stat" + str(number))


def detect_er_stat(image, number):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
        er_stat = float(data)
        if er_stat < 100:
            er_stat_list.append("er_stat" + str(number))
        else:
            er_stat_list.append(er_stat)
        return er_stat_list
    except ValueError:
        er_stat_list.append("Error_er_stat" + str(number))

