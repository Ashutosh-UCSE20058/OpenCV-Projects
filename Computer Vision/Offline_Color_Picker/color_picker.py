
import cv2 as cv
import numpy as np

def cross(x):
    pass

# Creating Blank Images
img = np.zeros((300,512,3),np.uint8)
cv.namedWindow("Color Picker")

# Creating switch
s1 = "0:OFF \ 1:ON"
cv.createTrackbar(s1,"Color Picker",0,1,cross)

#Creating the RGB

#Creating Track Bars fr Adjusting Colors
cv.createTrackbar("R","Color Picker",0,255,cross)
cv.createTrackbar("G","Color Picker",0,255,cross)
cv.createTrackbar("B","Color Picker",0,255,cross)

while True:
    cv.imshow("Color Picker",img)
    key = cv.waitKey(1) & 0xFF
    if key==27: # For Exit
        break

    # Getting the trackbars Position
    s = cv.getTrackbarPos(s1,"Color Picker")
    r = cv.getTrackbarPos("R","Color Picker")
    g = cv.getTrackbarPos("G","Color Picker")
    b = cv.getTrackbarPos("B","Color Picker")

    if s==0:
        img[:] = 0
    else:
        img[:] = [r,g,b]

cv.destroyAllWindows()