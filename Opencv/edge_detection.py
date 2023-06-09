import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale Color', gray)

# Laplacian 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian ', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow(' Sobel x', sobelx)
cv.imshow('Sobel y', sobely)

combine_sobel = cv.bitwise_and(sobelx, sobely)
cv.imshow('Sobel Combine', combine_sobel)

##########

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)