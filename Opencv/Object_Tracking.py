
# Object tracking or Color Detection

import cv2 as cv
import numpy as np

frame = cv.imread("Images\colorballs.jpg")

while True:
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    upper_value = np.array([48,255,248])
    lower_value = np.array([20,143,139])

    # Creating Mask
    mask = cv.inRange(hsv, lower_value, upper_value)
    # Filtering mask with image
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("Frame", frame)
    cv.imshow("Mask",mask)
    cv.imshow("Res",res)

    key = cv.waitKey(1)
    if key==27:
        break

cv.destroyAllWindows()

