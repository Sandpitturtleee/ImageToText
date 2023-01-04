# ImageToText
Initial idea for the project came for Fischl mains discord server. I made this project to detect text from shared there images and then to process it. 
I used processed data to make an online spreadsheet for everyone to look at. Here is a link [Fischl spreadsheet](https://docs.google.com/spreadsheets/d/1ATCu5dhktB9Fd_IZtxidCoF-kD91e2kU-51Gm3HglE8/edit#gid=99213294 "Fischl Spreadsheet")
Currently data is gathered from 261 images. Basic GUI made with PyQt5. 
# Technologies
- Code implemented in **Python**
- AI used to detect text from images - **Pytesseract**
- used python libraries: os, cv2, natsort, shutil, PyQt5
- online google excel spreadsheet
# Functionalities
- Loading images from 4 folders containing different image sizes/formats
- Cropping desired parts of images
- Detecting text from cropped images and handling errors during detection with exception handling
- Moving images with errors to Error folder
- Saving detected text to .txt files
- Processing some of data to make it appropriate for spreadsheet 
