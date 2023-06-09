
# Image Blending 
import cv2 as cv
import numpy as np

img1 = cv.imread("Images\cat.jpg")
img1 = cv.resize(img1,(500,700))
img2 = cv.imread("Images\dog.jpg")
img2 = cv.resize(img2,(500,700))

cv.imshow("Cat",img1)
cv.imshow("Dog",img2)

# Peforming Blending
# result = img2 + img1
# cv.imshow("Result: ", result)

# Using addition
result1 = cv.add(img1,img2)
cv.imshow("Result: ", result1)

# Add Weight
result2 = cv.addWeighted(img1,0.3,img2,0.7,0)
cv.imshow("Result: ", result2)

cv.waitKey(0)
cv.destroyAllWindows()