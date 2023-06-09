import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)
# img = cv.imread('Images/cat.jpg')
# cv.imshow('Cat',img)

#painting the image
# blank[200:300, 300:400] = (0,255,0)

#drawing a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('rectangle',blank)
# cv.imshow('Green ', blank)

#drawing the circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle',blank)

# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.line(blank, (100,250), (100,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# writing text on an image
cv.putText(blank, 'Hello, name is carl!!1', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Image Text', blank)


cv.waitKey(0)