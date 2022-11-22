import cv2
import pytesseract

from detect_text_files.supporting_functions import move_files
from variables import image_data


def detect_text(cropped_image, folder_path, small_iterator, big_iterator):
    try:
        detect_character(cropped_image[0], big_iterator)
        detect_lvl(cropped_image[1], big_iterator)
        detect_nick(cropped_image[2], big_iterator)
        detect_uid(cropped_image[3], big_iterator)
        detect_bow_name(cropped_image[4], big_iterator)
        detect_artifact(cropped_image[5], big_iterator)
        detect_refinement(cropped_image[6], big_iterator)
        detect_bow_lvl(cropped_image[7], big_iterator)
        detect_fr_lvl(cropped_image[8], big_iterator)
        detect_aa_lvl(cropped_image[9], big_iterator)
        detect_e_lvl(cropped_image[10], big_iterator)
        detect_q_lvl(cropped_image[11], big_iterator)
        detect_hp_stat(cropped_image[12], big_iterator)
        detect_atk_stat(cropped_image[13], big_iterator)
        detect_def_stat(cropped_image[14], big_iterator)
        detect_em_stat(cropped_image[15], big_iterator)
        detect_cr_stat(cropped_image[16], big_iterator)
        detect_cd_stat(cropped_image[17], big_iterator)
        detect_er_stat(cropped_image[18], big_iterator)
    except ValueError:
        print("imageError" + str(big_iterator))
        move_files(folder_path, small_iterator, big_iterator)


def detect_character(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    character = str(data)
    image_data[0].append(character)
    return image_data[0]


def detect_lvl(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    lvl = int(data)
    if lvl < 10:
        image_data[1].append("lvl" + str(big_iterator))
    else:
        image_data[1].append(lvl)
    return image_data[1]


def detect_nick(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    nick = str(data)
    image_data[2].append(nick)
    return image_data[2]


def detect_uid(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    uid = data
    if len(uid) != 10 and len(uid) != 0:
        image_data[3].append("uid" + str(big_iterator))
    else:
        image_data[3].append(uid)
    return image_data[3]


def detect_bow_name(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    bow_name = str(data)
    image_data[4].append(bow_name)
    return image_data[4]


def detect_artifact(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    artifact = str(data)
    image_data[5].append(artifact)
    return image_data[5]


def detect_refinement(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=12345')
    refinement = int(data)
    if refinement < 1 or refinement > 5:
        image_data[6].append("refinement" + str(big_iterator))
    else:
        image_data[6].append(refinement)
    return image_data[6]


def detect_bow_lvl(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    bow_lvl = int(data)
    if bow_lvl < 10:
        image_data[7].append("bow_lvl" + str(big_iterator))
    else:
        image_data[7].append(bow_lvl)
    return image_data[7]


def detect_fr_lvl(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    fr_lvl = int(data)
    if fr_lvl < 1:
        image_data[8].append("fr_lvl" + str(big_iterator))
    else:
        image_data[8].append(fr_lvl)
    return image_data[8]


def detect_aa_lvl(image, big_iterator):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        aa_lvl = int(data)
        if aa_lvl < 1 or aa_lvl > 10:
            image_data[9].append("aa_lvl" + str(big_iterator))
        else:
            image_data[9].append(aa_lvl)
    except ValueError:
        image_data[9].append("aa_lvl" + str(big_iterator))
    return image_data[9]


def detect_e_lvl(image, big_iterator):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        e_lvl = int(data)
        if e_lvl < 1 or e_lvl > 13:
            image_data[10].append("e_lvl" + str(big_iterator))
        else:
            image_data[10].append(e_lvl)
    except ValueError:
        image_data[10].append("e_lvl" + str(big_iterator))
    return image_data[10]


def detect_q_lvl(image, big_iterator):
    try:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        data = pytesseract.image_to_string(image, lang='eng',
                                           config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        q_lvl = int(data)
        if q_lvl < 1 or q_lvl > 13:
            image_data[11].append("q_lvl" + str(big_iterator))
        else:
            image_data[11].append(q_lvl)
    except ValueError:
        image_data[11].append("q_lvl" + str(big_iterator))
    return image_data[11]


def detect_hp_stat(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    hp_stat = int(data[:5])
    if hp_stat < 10000:
        image_data[12].append("hp_stat" + str(big_iterator))
    else:
        image_data[12].append(hp_stat)
    return image_data[12]


def detect_atk_stat(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    atk_stat = int(data[:4])
    if atk_stat < 1000:
        image_data[13].append("atk_stat" + str(big_iterator))
    else:
        image_data[13].append(atk_stat)
    return image_data[13]


def detect_def_stat(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789(')
    def_stat = int(data[:3])
    if def_stat < 100:
        image_data[14].append("def_stat" + str(big_iterator))
    else:
        image_data[14].append(def_stat)
    return image_data[14]


def detect_em_stat(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    em_stat = int(data)
    if em_stat < 10:
        image_data[15].append("em_stat" + str(big_iterator))
    else:
        image_data[15].append(em_stat)
    return image_data[15]


def detect_cr_stat(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    cr_stat = float(data)
    if cr_stat < 10:
        image_data[16].append("cr_stat" + str(big_iterator))
    else:
        image_data[16].append(cr_stat)
    return image_data[16]


def detect_cd_stat(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    cd_stat = float(data)
    if cd_stat < 50:
        image_data[17].append("cd_stat" + str(big_iterator))
    else:
        image_data[17].append(cd_stat)
    return image_data[17]


def detect_er_stat(image, big_iterator):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    er_stat = float(data)
    if er_stat < 100:
        image_data[18].append("er_stat" + str(big_iterator))
    else:
        image_data[18].append(er_stat)
    return image_data[18]
