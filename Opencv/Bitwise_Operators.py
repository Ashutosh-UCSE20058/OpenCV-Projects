
import cv2 as cv
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv.rectangle(img1, (150,100), (200,250), (255,255,255),-1)

img2 = np.zeros((250,500,3), np.uint8)
img2 = cv.rectangle(img2, (10,10), (170,190),(255,255,255),-1)

cv.imshow("Image1",img1)
cv.imshow("image2",img2)

# Bitwise And operations
bitand = cv.bitwise_and(img2,img1)
cv.imshow('Bitwise And', bitand)

# Bitwise OR operation
bitor = cv.bitwise_or(img2,img1)
cv.imshow('Bitwise or', bitor)

#  Bitwise NOT operation
bitnot1 = cv.bitwise_not(img1)
bitnot2 = cv.bitwise_not(img2)
cv.imshow("Bit Not image1",bitnot1)
cv.imshow("Bit Not image2",bitnot2)

# Bitwise XOR operation
bitxor = cv.bitwise_xor(img1, img2)
cv.imshow("Bitwise XOR",bitxor)

cv.waitKey(0)
cv.destroyAllWindows()