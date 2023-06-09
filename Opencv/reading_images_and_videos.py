import cv2 as cv
# image = cv.imread('Images/cat.jpg')
# cv.imshow('Cat',image)
capture = cv.VideoCapture('Videos/earth.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
