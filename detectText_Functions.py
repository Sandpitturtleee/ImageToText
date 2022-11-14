import cv2
import pytesseract

from variables import data_lists


def detect_character(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    character = str(data)
    data_lists[0].append(character)
    return data_lists[0]


def detect_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    lvl = int(data)
    if lvl < 10:
        data_lists[1].append("lvl" + str(number))
    else:
        data_lists[1].append(lvl)
    return data_lists[1]


def detect_nick(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    nick = str(data)
    data_lists[2].append(nick)
    return data_lists[2]


def detect_uid(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    uid = data
    if len(uid) != 10 and len(uid) != 0:
        data_lists[3].append("uid" + str(number))
    else:
        data_lists[3].append(uid)
    return data_lists[3]


def detect_bow_name(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    bow_name = str(data)
    data_lists[4].append(bow_name)
    return data_lists[4]


def detect_artifact(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    artifact = str(data)
    data_lists[5].append(artifact)
    return data_lists[5]


def detect_refinement(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=12345')
    refinement = int(data)
    if refinement < 1 or refinement > 5:
        data_lists[6].append("refinement" + str(number))
    else:
        data_lists[6].append(refinement)
    return data_lists[6]


def detect_bow_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    bow_lvl = int(data)
    if bow_lvl < 10:
        data_lists[7].append("bow_lvl" + str(number))
    else:
        data_lists[7].append(bow_lvl)
    return data_lists[7]


def detect_fr_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    fr_lvl = int(data)
    if fr_lvl < 1:
        data_lists[8].append("fr_lvl" + str(number))
    else:
        data_lists[8].append(fr_lvl)
    return data_lists[8]


def detect_aa_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    aa_lvl = int(data)
    if aa_lvl < 1 or aa_lvl > 10:
        data_lists[9].append("aa_lvl" + str(number))
    else:
        data_lists[9].append(aa_lvl)
    return data_lists[9]


def detect_e_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    e_lvl = int(data)
    if e_lvl < 1 or e_lvl > 13:
        data_lists[10].append("e_lvl" + str(number))
    else:
        data_lists[10].append(e_lvl)
    return data_lists[10]


def detect_q_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    q_lvl = int(data)
    if q_lvl < 1 or q_lvl > 13:
        data_lists[11].append("q_lvl" + str(number))
    else:
        data_lists[11].append(q_lvl)
    return data_lists[11]

def detect_hp_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    hp_stat = int(data[:5])
    if hp_stat < 10000:
        data_lists[12].append("hp_stat" + str(number))
    else:
        data_lists[12].append(hp_stat)
    return data_lists[12]

def detect_atk_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    atk_stat = int(data[:4])
    if atk_stat < 1000:
        data_lists[13].append("atk_stat" + str(number))
    else:
        data_lists[13].append(atk_stat)
    return data_lists[13]


def detect_def_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    def_stat = int(data[:3])
    if def_stat < 100:
        data_lists[14].append("def_stat" + str(number))
    else:
        data_lists[14].append(def_stat)
    return data_lists[14]


def detect_em_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    em_stat = int(data)
    if em_stat < 10:
        data_lists[15].append("em_stat" + str(number))
    else:
        data_lists[15].append(em_stat)
    return data_lists[15]


def detect_cr_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    cr_stat = float(data)
    if cr_stat < 10:
        data_lists[16].append("cr_stat" + str(number))
    else:
        data_lists[16].append(cr_stat)
    return data_lists[16]


def detect_cd_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    cd_stat = float(data)
    if cd_stat < 50:
        data_lists[17].append("cd_stat" + str(number))
    else:
        data_lists[17].append(cd_stat)
    return data_lists[17]


def detect_er_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    er_stat = float(data)
    if er_stat < 100:
        data_lists[18].append("er_stat" + str(number))
    else:
        data_lists[18].append(er_stat)
    return data_lists[18]
