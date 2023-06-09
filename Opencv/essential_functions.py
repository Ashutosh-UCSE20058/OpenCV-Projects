import cv2 as cv

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

# converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# how to blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny',canny)

# dilate the image 
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated ', dilated)

# erode the image
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Erode',eroded)

# resizng the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)   
cv.imshow('Resized ', resized)

# croping the image
croped = img[50:200, 200:400]
cv.imshow('Cropped', croped)

cv.waitKey(0)