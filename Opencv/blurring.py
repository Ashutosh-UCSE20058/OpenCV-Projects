import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)