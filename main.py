
from PIL import Image
from pytesseract import pytesseract
import cv2
import pytesseract

def crop(image):
    character = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\char.jpg"
    lvl = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\lvl.jpg"
    nick = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\nick.jpg"
    id = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\id.jpg"
    bow_name = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\bow_name.jpg"
    stats = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\stats.jpg"
    set = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\set.jpg"
    refinement = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\refinement.jpg"
    bow_lvl = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\bow_lvl.jpg"
    fr_lvl = r"C:\Users\karol\Desktop\Studia\5 Semestr\Programowanie Wieloplatformowe w Qt\ImageToText\venv\images\New\fr_lvl.jpg"
    character1 = image[45:80, 35:160]
    lvl1 = image[95:125, 35:170]
    nick1 = image[30:120, 200:650]
    id1 = image[750:780, 25:160]
    bow_name1 = image[40:80, 915:1300]
    stats1 = image[235:710, 785:1290]
    set1 = image[715:795, 825:1280]
    refinement1 = image[145:180, 920:970]
    bow_lvl1 = image[140:180, 985:1145]
    fr_lvl1 = image[145:175, 80:120]
    #cv2.imshow("cropped", char)
    cv2.imwrite(character, character1)
    cv2.imwrite(lvl, lvl1)
    cv2.imwrite(nick, nick1)
    cv2.imwrite(id, id1)
    cv2.imwrite(bow_name, bow_name1)
    cv2.imwrite(stats, stats1)
    cv2.imwrite(set, set1)
    cv2.imwrite(refinement, refinement1)
    cv2.imwrite(bow_lvl, bow_lvl1)
    cv2.imwrite(fr_lvl, fr_lvl1)
    cv2.waitKey(0)
def detectText(image):
    print('detect')
    image1 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    #  data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
    image2 = cv2.resize(image1, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    data = pytesseract.image_to_string(image2, lang='eng', config='--psm 4 --oem 3 --dpi 300 digits')
    print(data)

    cv2.imshow('thresh', image2)
    cv2.waitKey()


if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = cv2.imread('venv/images/image3.png', 0)
    crop(image)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
