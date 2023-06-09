import cv2 as cv
import numpy as np


frame = cv.imread("Images\colorballs.jpg")
frame = cv.resize(frame, (600,400))

def nothing(x):
    pass

cv.namedWindow("Color Adjustments")

cv.createTrackbar("Lower_H","Color Adjustments",0,255, nothing)
cv.createTrackbar("Lower_S","Color Adjustments",0,255, nothing)
cv.createTrackbar("Lower_V", "Color Adjustments",0,255,nothing)

cv.createTrackbar("Upper_H","Color Adjustments",255,255, nothing)
cv.createTrackbar("Upper_S","Color Adjustments",255,255, nothing)
cv.createTrackbar("Upper_V", "Color Adjustments",255,255,nothing)

while True:
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lowerh = cv.getTrackbarPos("Lower_H", "Color Adjustments")
    lowers = cv.getTrackbarPos("Lower_S","Color Adjustments")
    lowerv = cv.getTrackbarPos("Lower_V","Color Adjustments")

    upperh = cv.getTrackbarPos("Upper_H", "Color Adjustments")
    uppers = cv.getTrackbarPos("Upper_S","Color Adjustments")
    upperv = cv.getTrackbarPos("Upper_V","Color Adjustments")

    lower_bound = np.array([lowerh,lowers,lowerv])
    upper_bound = np.array([upperh,uppers,upperv])

    mask = cv.inRange(hsv,lower_bound,upper_bound)

    # filter mask with image
    Result = cv.bitwise_and(frame,frame, mask=mask)
    cv.imshow("Original Frame", frame)
    cv.imshow("Mask",mask)
    cv.imshow("Result",Result)

    key = cv.waitKey(1)
    if key==27:
        break


cv.destroyAllWindows()