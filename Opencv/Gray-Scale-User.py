import cv2 as cv
import numpy as np

# image Conversion project: Colored Image into Grayscale.

path = input("Enter the path of your image: ")
print("The path of the image you have entered: ", path)

img = cv.imread(path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

save = cv.waitKey(0)
if save==ord("s"):
    cv.imwrite('Images\GrayScale-Cat.jpg', gray)
else:
    cv.destroyAllWindows()
