import numpy as np
import cv2 as cv

img = cv.imread('Images\cat.jpg')
# img = cv.resize(img,(500,700))

# for black screen
img = np.zeros([512,512,3], np.uint8)*255 

# for white screen
img = np.ones([512,512,3], np.uint8)*255 

#here line accept 5 parameters (img,starting,ending,color,thicknes)
img = cv.line(img, (0,0),(200,200),(255,181,102),8) #color format BGR

#arrowed line accept also accept 5 parameter (img, starting, ending, color, thickness)
img = cv.arrowedLine(img, (0,125),(255,255),(255,0,125),10)

#Rectangle = accept parameter(img, start_co, end_co, color, thickness)
img = cv.rectangle(img, (100,10), (150,128), (128,0,255),5)

#circle = accept(img, start_co, radius, color, thickness)
img = cv.circle(img, (100,125),50,(210,255,0),-5)

#puttext = accept(img, text, start_co, font, fontsize, color, thickness, linetype)
font = cv.FONT_ITALIC
img = cv.putText(img, 'Cat', (20,500),font,2, (0,125,225),6,cv.LINE_AA)

#ellipse = accept(img, start_co, (length,height), color, thickness)
img = cv.ellipse(img,(100,300),(100,50),0,0,360,155,5)

cv.imshow("Cat",img)

cv.waitKey(0)
cv.destroyAllWindows()