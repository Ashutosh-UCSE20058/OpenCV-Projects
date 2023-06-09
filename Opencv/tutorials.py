import cv2 as cv
import numpy as np

img = cv.imread('Images\cat.jpg')
#resizing the image
# img = cv.resize(img,(400,400)) resizing 
cv.imshow("Cat",img)

cv.waitKey(0)