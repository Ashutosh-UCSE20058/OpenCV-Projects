import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale image', gray)

blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur image ', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Image', canny)

ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold image', thres)

contours, hierarchies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found.')

# drawing the contours

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)