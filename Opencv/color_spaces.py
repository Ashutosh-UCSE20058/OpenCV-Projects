import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/wallpaper.jpg')
cv.imshow('Scenery', img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Image', hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB Image', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Image', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr', hsv_bgr)

# l*a*b to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab to bgr', lab_bgr)


# plt.imshow(img)
# plt.show()

cv.waitKey(0)