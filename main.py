from PIL import Image
from pytesseract import pytesseract
import cv2
import pytesseract
from detect_Text_functions import *
from crop_functions import *


if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = cv2.imread('venv/images/image.png', 0)
    dim = (1927, 804)
    resized = cv2.resize(image, dim)
    crop(resized, 1)
    #crop(resized, 1)
    #crop(image, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
