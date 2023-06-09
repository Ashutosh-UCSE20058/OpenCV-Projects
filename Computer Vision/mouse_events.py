# Mouse calback functions

import cv2 as cv
import numpy as np

def draw(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(125,0,255),5)
    if event == cv.EVENT_RBUTTONDBLCLK:
        cv.rectangle(img, (x,y), (x+100,y+75),
        (125,125.255),2)

cv.namedWindow(winname = "Image")
img = np.zeros((512,512,3), np.uint8)
cv.setMouseCallback("Image",draw)

while True:
    cv.imshow("Image",img)
    if cv.waitKey(1) & 0xFF == 27: #esc key
        break

cv.destroyAllWindows()