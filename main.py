from PIL import Image
from pytesseract import pytesseract
import cv2
import pytesseract


def crop(image, number):
    folder_path = 'C:/Users/karol/Desktop/Studia/5 Semestr/Programowanie Wieloplatformowe w Qt/ImageToText/venv/images/New/'
    extension_string = '.jpg'
    file_paths_strings = ["character", "lvl", "nick", "id", "bow_name", "stats", "set", "refinement", "bow_lvl",
                          "fr_lvl"]
    file_names_strings = ["character", "lvl", "nick", "id", "bow_name", "stats", "set", "refinement", "bow_lvl",
                          "fr_lvl"]
    crop_values_matrix = [[45, 80, 35, 160], [95, 125, 35, 170], [30, 120, 200, 650], [750, 780, 25, 160],
                          [40, 80, 915, 1300], [235, 710, 785, 1290], [715, 795, 825, 1280], [145, 180, 920, 970],
                          [140, 180, 985, 1145], [145, 175, 80, 120], ]

    # Creating filepaths for output images
    for x in range(len(file_paths_strings)):
        file_paths_strings[x] = folder_path + file_paths_strings[x] + str(number) + extension_string
        # print(file_paths_strings[x])

    # Creating names for cropped images
    for x in range(len(file_names_strings)):
        file_names_strings[x] = file_names_strings[x] + str(number)
        # print(file_names_strings[x])

    # Cropping images
    for x in range(len(file_names_strings)):
        file_names_strings[x] = image[crop_values_matrix[x][0]:crop_values_matrix[x][1],crop_values_matrix[x][2]:crop_values_matrix[x][3]]

    # Saving images
    for x in range(len(file_paths_strings)):
        cv2.imwrite(file_paths_strings[x], file_names_strings[x])

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
    crop(image, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
