import utils
import cv2 as cv
import numpy as np

webcam = False
path = 'image.jpg' #to be given 
capture = cv.VideoCapture(0)
capture.set(10,160)
capture.set(3,1920)
capture.set(4,1080)

scale = 3

wP = 210 * scale
hP = 297 * scale



while True:
    
    if webcam:
        success, img = capture.read()
    elif cv.waitKey(20000) & 0xFF==ord('d'):
        break
    else:
        img = cv.imread(path)

        imgConts, finalContours = utils.getContours(img, minArea=50000, filter=4)

        if len(finalContours)!=0:
            biggest = finalContours[0][2]
            # print(biggest)
            imgWarp = utils.warpImg(img,biggest,wP,hP)
            
            imgConts2, finalContours2 = utils.getContours(imgWarp, minArea=20000, filter=4, threshold=[50,50], draw=False)
            


            if len(finalContours) != 0:
                for obj in finalContours2:
                    cv.polylines(imgConts2, [obj[2]], True, (0,255,0),2)
                    newpoints = utils.reorder(obj[2])
                    newwidth = round((utils.findDis(newpoints[0][0]//scale, newpoints[1][0]//scale)/10),1)
                    newheight = round((utils.findDis(newpoints[0][0]//scale, newpoints[2][0]//scale)/10),1)
                    cv.arrowedLine(imgConts2, (newpoints[0][0][0], newpoints[0][0][1]), (newpoints[1][0][0], newpoints[1][0][1]),
                                    (255, 0, 255), 3, 8, 0, 0.05)
                    cv.arrowedLine(imgConts2, (newpoints[0][0][0], newpoints[0][0][1]), (newpoints[2][0][0], newpoints[2][0][1]),
                                    (255, 0, 255), 3, 8, 0, 0.05)
                    x, y, w, h = obj[3]
                    cv.putText(imgConts2, '{}cm'.format(newwidth), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                                (255, 0, 255), 2)
                    cv.putText(imgConts2, '{}cm'.format(newheight), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                                (255, 0, 255), 2)

            cv.imshow('A4 image', imgConts2)

        img = cv.resize(img,(0,0),None,0.5,0.5)
        cv.imshow('Original Image', img)
