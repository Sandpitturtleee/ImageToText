import cv2
import pytesseract


def detect_character(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    print(data)
    # cv2.imshow('thresh', image)


def detect_lvl(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_nick(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    print(data)
    # cv2.imshow('thresh', image)


def detect_id(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_bow_name(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    print(data)
    # cv2.imshow('thresh', image)


def detect_set(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --oem 3')
    print(data)
    # cv2.imshow('thresh', image)


def detect_refinement(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_bow_lvl(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_fr_lvl(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_aa_lvl(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_e_lvl(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_q_lvl(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(data)
    # cv2.imshow('thresh', image)


def detect_hp_stat(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.%')
    print(data)
    cv2.imshow('thresh', image)


def detect_atk_stat(image,number):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.%')
    #print(data)
    atk_stat = float(data)
    print(atk_stat)
    if(atk_stat<1000):
        print("atk_stat"+str(number))
    else:
        print("Do nothing")

    cv2.imshow('thresh', image)
    cv2.waitKey(5000)


def detect_def_stat(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.%')
    print(data)
    cv2.imshow('thresh', image)


def detect_em_stat(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.%')
    print(data)
    cv2.imshow('thresh', image)


def detect_cr_stat(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.%')
    print(data)
    cv2.imshow('thresh', image)


def detect_cd_stat(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.%')
    print(data)
    cv2.imshow('thresh', image)


def detect_er_stat(image):
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = pytesseract.image_to_string(image, lang='eng',
                                       config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.%')
    print(data)
    cv2.imshow('thresh', image)
