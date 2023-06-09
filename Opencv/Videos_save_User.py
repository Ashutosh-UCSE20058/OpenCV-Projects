import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

vid = cv.VideoWriter_fourcc(*"XVID")
output = cv.VideoWriter("Videos\Me.avi",vid,20.0,(640,480),0)

while video.isOpened():
    ret,frame = video.read()
    if ret==True:
        # frame = cv.resize(frame, (500,500))
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Original Frame", frame)
        cv.imshow('GrayScale Frame', gray)
        output.write(frame)
        
        if cv.waitKey(1) & 0XFF == ord('q'):
            break

video.release()
output.release()
cv.destroyAllWindows()