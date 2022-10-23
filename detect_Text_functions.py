import cv2
import pytesseract


def detect_character(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    character = str(data)
    print(character)
    # cv2.imshow('thresh', image)


def detect_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    lvl = int(data)
    print(lvl)
    if lvl < 10:
        print("lvl" + str(number))
        print(lvl)
    # cv2.imshow('thresh', image)


def detect_nick(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    nick = str(data)
    print(nick)
    # cv2.imshow('thresh', image)


def detect_id(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    # cv2.imshow('thresh', image)
    uid = data
    print(uid)
    if len(uid) != 10:
        print("uid" + str(number))
        print(uid)


def detect_bow_name(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    print(data)
    # cv2.imshow('thresh', image)


def detect_set(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    print(data)
    # cv2.imshow('thresh', image)


def detect_refinement(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=12345')
    # print(data)
    refinement = int(data)
    print(refinement)
    if refinement < 1 or refinement > 5:
        print("refinement" + str(number))
        print(refinement)
    # cv2.imshow('thresh', image)


def detect_bow_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    bow_lvl = int(data)
    print(bow_lvl)
    if bow_lvl < 10:
        print("bow_lvl" + str(number))
        print(bow_lvl)
    cv2.imshow('thresh', image)
    cv2.waitKey()


def detect_fr_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    fr_lvl = int(data)
    print(fr_lvl)
    if fr_lvl < 1:
        print("fr_lvl" + str(number))
        print(fr_lvl)
    # cv2.imshow('thresh', image)


def detect_aa_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    cv2.imshow('thresh', image)
    cv2.waitKey()
    aa_lvl = int(data)
    print(aa_lvl)
    if aa_lvl < 1 or aa_lvl > 10:
        print("aa_lvl" + str(number))
        print(aa_lvl)


def detect_e_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    e_lvl = int(data)
    print(e_lvl)
    if e_lvl < 1 or e_lvl > 13:
        print("e_lvl" + str(number))
        print(e_lvl)
    # cv2.imshow('thresh', image)


def detect_q_lvl(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    q_lvl = int(data)
    print(q_lvl)
    if q_lvl < 1 or q_lvl > 13:
        print("q_lvl" + str(number))
        print(q_lvl)
    # cv2.imshow('thresh', image)


def detect_hp_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    hp_stat = int(data)
    if hp_stat < 10000:
        print("hp_stat" + str(number))
        print(hp_stat)
    else:
        print(hp_stat)
    # cv2.imshow('thresh', image)


def detect_atk_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    atk_stat = int(data)
    if atk_stat < 1000:
        print("atk_stat" + str(number))
        print(atk_stat)
    else:
        print(atk_stat)
    # cv2.imshow('thresh', image)
    # cv2.waitKey(5000)


def detect_def_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    # cv2.imshow('thresh', image)
    def_stat = int(data)
    print(def_stat)
    if def_stat < 100:
        print("def_stat" + str(number))
        print(def_stat)


def detect_em_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(data)
    em_stat = int(data)
    print(em_stat)
    # cv2.imshow('thresh', image)


def detect_cr_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    # print(data)
    cr_stat = float(data)
    if cr_stat < 10:
        print("cr_stat" + str(number))
        print(cr_stat)
    else:
        print(cr_stat)
    # cv2.imshow('thresh', image)


def detect_cd_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    # print(data)
    cd_stat = float(data)
    if cd_stat < 50:
        print("cd_stat" + str(number))
        print(cd_stat)
    else:
        print(cd_stat)
    # cv2.imshow('thresh', image)


def detect_er_stat(image, number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.')
    # print(data)
    er_stat = float(data)
    if er_stat < 100:
        print("er_stat" + str(number))
        print(er_stat)
    else:
        print(er_stat)
    # cv2.imshow('thresh', image)
