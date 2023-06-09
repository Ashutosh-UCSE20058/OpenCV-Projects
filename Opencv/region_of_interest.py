# Region of Interest
import numpy as np
import cv2 as cv

# Reading the image
img = cv.imread("Images\cat.jpg")
# cv.imshow("Cat",img)

#(204,148)
#(260,207)
roi = img[148:207,204:260]

# Passing data into image
img[148:207,261:317] = roi
img[148:207,318:374] = roi

cv.imshow("ROI",img)
cv.waitKey(0)
cv.destroyAllWindows()
