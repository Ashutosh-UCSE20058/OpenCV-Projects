#Draw date time and Figures on videos
import cv2 as cv
import numpy as np
import datetime

cap = cv.VideoCapture("Videos\earth.mp4")
print("for width== ", cap.get(cv.CAP_PROP_FRAME_WIDTH))
print("for height== ", cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# print("Width== ", cap.get(3)) #3 for width
# print("Height== ", cap.get(4)) #4 for height

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        font2 = cv.FONT_ITALIC
        text = ' Height: ' + str(cap.get(4)) + ' Width: ' + str(cap.get(3))
        frame = cv.putText(frame, text, (10,20), font, 1, (0,120,0), 1, cv.LINE_AA)

        date_data = "Date: " + str(datetime.datetime.now())
        frame = cv.putText(frame, date_data, (20,50), font2, 1, (100,5,255),1, cv.LINE_AA)

        cv.imshow('Frame', frame)
        if cv.waitKey(30) & 0XFF==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
