import cv2 as cv
import numpy as np

# Provide your screen Path
vidcap = cv.VideoCapture(r'C:\Users\ashut\Desktop\OpenCV Projects\Opencv\Videos\TestVideo.mp4')

# Reading the Video
ret,image = vidcap.read()
count = 0
while True:
    if ret==True:
        cv.imwrite(r'C:\Users\ashut\Desktop\OpenCV Projects\Screen Recorder\New_Frames\img%d.jpg'%count,image)
        vidcap.set(cv.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv.imshow("Images",image)
        count+=1
        if cv.waitKey(1) & 0xFF==ord("q"):
                break
                cv.destroyAllWindows()

vidcap.release()
cv.destroyAllWindows()

# import cv2

# vidcap = cv2.VideoCapture(0)
# ret,image = vidcap.read()#READ THE VIDEO



# count = 0

# while True:
#   if ret == True:
#       cv2.imwrite("frames\\imgN%d.jpg" % count, image)     # save frame as JPEG file
#       vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) #used to hold speed of frane generation
#       ret,image = vidcap.read()
#       cv2.imshow("res",image)
#       print ('Read a new frame:',count ,ret)
#       count += 1
#       if cv2.waitKey(1) & 0xFF == ord("q"):
#           break
#           cv2.destroyAllWindows()
#   else:
#       break

# vidcap.release() 
# cv2.destroyAllWindows()  
