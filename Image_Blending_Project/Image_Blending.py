
import cv2 as cv
import numpy as np

img1 = cv.imread("Images\cat.jpg")
img1 = cv.resize(img1, (500,700))

img2 = cv.imread("Images\dog.jpg")
img2 = cv.resize(img2, (500,700))

# cv.imshow("Image1",img1)
# cv.imshow("Image2",img2)

def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv.namedWindow('Window')
cv.createTrackbar('Alpha','Window',1,100, blend)
switch = '0 : OFF \n 1 : ON'
cv.createTrackbar(switch,'Window',0,1,blend)

while True:
    s = cv.getTrackbarPos(switch,"Window")
    a = cv.getTrackbarPos("Alpha","Window")
    n = float(a/100)
    print(n)

    if s==0:
        dst = img[:]
    else:
        dst = cv.addWeighted(img1,1-n,img2,n,0)
        cv.putText(dst, str(a), (20,50), cv.FONT_ITALIC, 2 , (0,125,255),2)        

    cv.imshow('Dst',dst)
    k = cv.waitKey(1)&0xFF
    if k==27:
        break

cv.waitKey()
cv.destroyAllWindows()
