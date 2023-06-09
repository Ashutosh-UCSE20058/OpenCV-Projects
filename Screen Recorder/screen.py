import cv2 as cv
import pyautogui as py
import numpy as np

#Create resolution
rs = py.size()

#filename in which we store recording
fn = input('Please enter any file name and path: ')
#fix the frame rate
fps = 60.0

fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter(fn,fourcc,fps,rs)

#create recording module
cv.namedWindow("Live_Recording",cv.WINDOW_NORMAL)
cv.resizeWindow("Live_Rec", (600,400))

while True:
    img = py.screenshot()
    f = np.array(img)
    f = cv.cvtColor(f,cv.COLOR_BGR2RGB)
    output.write(f)
    cv.imshow("Live_Record",f)
    if cv.waitKey(1) == ord("q"):
        break

cv.destroyAllWindows()
output.release()

