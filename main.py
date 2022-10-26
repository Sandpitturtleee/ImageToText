import os
from crop_functions import *
from write_to_file_functions import *


def combine1():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    path_to_images = "C:/Users/karol/Desktop/Studia/5 Semestr/Programowanie Wieloplatformowe w Qt/ImageToText/venv/Images/Base/"

    for root, dirs, file_names in os.walk(path_to_images):
        y = 1
        for file_name in file_names:
            image = cv2.imread(path_to_images + file_name, 0)
            dim = (1927, 804)
            resized = cv2.resize(image, dim)
            crop(resized, y)
            y = y + 1


if __name__ == '__main__':
    combine1()
    write_to_file2()




