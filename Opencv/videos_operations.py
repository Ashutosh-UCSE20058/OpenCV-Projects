import cv2 as cv
import numpy as np

video = cv.VideoCapture('Videos\earth.mp4')
while True:
    ret, frame = video.read()
    frame = cv.resize(frame, (700,450))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Frames", frame)
    cv.imshow("Grayscale",gray)
    key = cv.waitKey(25)
    if key == ord("q") & 0xFF:
        break
video.release()
cv.destroyAllWindows()