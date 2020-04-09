import numpy as np
import cv2
import imutils
import os
import pytesseract
from PIL import Image
from pytesseract import image_to_string



# image = cv2.imread("bill1.png")
# ratio = image.shape[0] / 500.0
# orig = image.copy()
# image = imutils.resize(image, height = 500)
 


# load the example image and convert it to grayscale
image = cv2.imread("aa.png")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray=image
 

 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)



# text = pytesseract.image_to_string(Image.open(filename), lang='ara')
print(pytesseract.image_to_pdf_or_hocr('aa.png', lang='ara', extension='hocr'))

os.remove(filename)
# print(text)
 
# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)





