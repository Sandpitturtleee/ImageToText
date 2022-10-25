import os

from PIL import Image
from pytesseract import pytesseract
import cv2
import pytesseract
from detect_Text_functions import *
from crop_functions import *


if __name__ == '__main__':

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    path_to_images = "C:/Users/karol/Desktop/Studia/5 Semestr/Programowanie Wieloplatformowe w Qt/ImageToText/venv/images/Base/"

    for root, dirs, file_names in os.walk(path_to_images):
        # Iterate over each file_name in the folder
        y = 1
        for file_name in file_names:
            image = cv2.imread(path_to_images + file_name, 0)
            dim = (1927, 804)
            resized = cv2.resize(image, dim)
            crop(resized, y)
            print(y)
            y = y+1

    hp_sum = 0
    for x in range(len(hp_stat_list)):
        print(hp_stat_list[x])
        hp_sum = hp_sum + hp_stat_list[x]

    print(hp_sum / len(hp_stat_list))


