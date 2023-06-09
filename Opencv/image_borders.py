
# Creating Image Borders
import cv2 as cv
import numpy as np

img = cv.imread("Images\cat.jpg")

border = cv.copyMakeBorder(img, 10,10,5,5, cv.BORDER_CONSTANT, value=[255,0,125])
cv.imshow("Cat",border)

cv.waitKey(0)
cv.destroyAllWindows()