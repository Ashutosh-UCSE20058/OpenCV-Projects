import cv2 as cv
import numpy as np
# Create a function which help to find coordinate of any pixel and its color.

def mouse_event(event,x,y,flag,param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flags==",flag)
    print("param==",param)
    font = cv.FONT_HERSHEY_PLAIN
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,'  ',y)
        cord = ".  " + str(x) + ',  ' + str(y)
        cv.putText(img,cord, (x,y), font, 1, (155,125,100),2)
        # cv.imshow('Image', img)
    
    if event == cv.EVENT_RBUTTONDOWN:
       b = img[y,x,0]    # for blue channel is 0
       g = img[y,x,1]     # for green channel in 1
       r = img[y,x,2]       # for red channel is 2

       color_bgr = ".  "  + str(b) + ',  ' + str(g) + ',  ' + str(r)
       cv.putText(img,color_bgr, (x,y), font, 1, (52,64,235),2)
    #    cv.imshow('Image',img)

cv.namedWindow(winname="res")

# img = np.zeros((512,512,3), np.uint8)
img = cv.imread("Images\cat.jpg")
cv.setMouseCallback("res",mouse_event)
 

while True:
    cv.imshow("res",img)
    if cv.waitKey(1) & 0xFF==27:    #esc Key
        break

cv.destroyAllWindows()