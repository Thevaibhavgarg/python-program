import cv2
from pytesseract import pytesseract
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img =cv2.imread("Screenshot_(7.2).png")
words_in_image=pytesseract.image_to_string(img)
print(words_in_image)
a=open("text.txt","w+")
a.write(words_in_image)
a.write("\n")
