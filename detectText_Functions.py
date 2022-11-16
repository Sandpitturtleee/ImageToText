import cv2
import pytesseract

from variables import image_data


def detect_character(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    character = str(data)
    image_data[0].append(character)
    return image_data[0]


def detect_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    lvl = int(data)
    if lvl < 10:
        image_data[1].append("lvl" + str(number))
    else:
        image_data[1].append(lvl)
    return image_data[1]


def detect_nick(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    nick = str(data)
    image_data[2].append(nick)
    return image_data[2]


def detect_uid(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    uid = data
    if len(uid) != 10 and len(uid) != 0:
        image_data[3].append("uid" + str(number))
    else:
        image_data[3].append(uid)
    return image_data[3]


def detect_bow_name(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    bow_name = str(data)
    image_data[4].append(bow_name)
    return image_data[4]


def detect_artifact(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    artifact = str(data)
    image_data[5].append(artifact)
    return image_data[5]


def detect_refinement(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=12345')
    refinement = int(data)
    if refinement < 1 or refinement > 5:
        image_data[6].append("refinement" + str(number))
    else:
        image_data[6].append(refinement)
    return image_data[6]


def detect_bow_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    bow_lvl = int(data)
    if bow_lvl < 10:
        image_data[7].append("bow_lvl" + str(number))
    else:
        image_data[7].append(bow_lvl)
    return image_data[7]


def detect_fr_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    fr_lvl = int(data)
    if fr_lvl < 1:
        image_data[8].append("fr_lvl" + str(number))
    else:
        image_data[8].append(fr_lvl)
    return image_data[8]


def detect_aa_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    aa_lvl = int(data)
    if aa_lvl < 1 or aa_lvl > 10:
        image_data[9].append("aa_lvl" + str(number))
    else:
        image_data[9].append(aa_lvl)
    return image_data[9]


def detect_e_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    e_lvl = int(data)
    if e_lvl < 1 or e_lvl > 13:
        image_data[10].append("e_lvl" + str(number))
    else:
        image_data[10].append(e_lvl)
    return image_data[10]


def detect_q_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    q_lvl = int(data)
    if q_lvl < 1 or q_lvl > 13:
        image_data[11].append("q_lvl" + str(number))
    else:
        image_data[11].append(q_lvl)
    return image_data[11]


def detect_hp_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    hp_stat = int(data[:5])
    if hp_stat < 10000:
        image_data[12].append("hp_stat" + str(number))
    else:
        image_data[12].append(hp_stat)
    return image_data[12]


def detect_atk_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    atk_stat = int(data[:4])
    if atk_stat < 1000:
        image_data[13].append("atk_stat" + str(number))
    else:
        image_data[13].append(atk_stat)
    return image_data[13]


def detect_def_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    def_stat = int(data[:3])
    if def_stat < 100:
        image_data[14].append("def_stat" + str(number))
    else:
        image_data[14].append(def_stat)
    return image_data[14]


def detect_em_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    em_stat = int(data)
    if em_stat < 10:
        image_data[15].append("em_stat" + str(number))
    else:
        image_data[15].append(em_stat)
    return image_data[15]


def detect_cr_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    cr_stat = float(data)
    if cr_stat < 10:
        image_data[16].append("cr_stat" + str(number))
    else:
        image_data[16].append(cr_stat)
    return image_data[16]


def detect_cd_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    cd_stat = float(data)
    if cd_stat < 50:
        image_data[17].append("cd_stat" + str(number))
    else:
        image_data[17].append(cd_stat)
    return image_data[17]


def detect_er_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    er_stat = float(data)
    if er_stat < 100:
        image_data[18].append("er_stat" + str(number))
    else:
        image_data[18].append(er_stat)
    return image_data[18]
