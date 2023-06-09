import cv2 as cv

image = cv.imread('Images/car1.jpg')
cv.imshow('Car',image)

cv.waitKey(0)

def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)
                                                                                                                                                                          

def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleframe(image)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('Videos/sample1.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleframe(frame, scale=0.20)
    cv.imshow('Video',frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows