
import cv2 as cv
import numpy as np

# Reading the image
img = cv.imread("Images\cat.jpg")

print("Image Shapes == ",img.shape)
print("No. of pixels == ",img.size)
print("datatype== ",img.dtype)
print("Imagetype== ",type(img))

#Splitting the Image

b,g,r = cv.split(img)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# cv.imshow("Original",img)

#Merging the Images together

merge1 = cv.merge((r,g,b))
# cv.imshow("rgb",merge1)

merge2 = cv.merge((g,b,r))
# cv.imshow("gbr",merge2)
# cv.imshow("Original",img)

# Working on the image pixel values
img2 = cv.imread('Images\scenery.jpg')
img2 = cv.resize(img2,(700,600))
cv.imshow("Scenery",img2)

# Accessing a pixel value by its row and column coordinates
pixel = img2[520,580]
print("the pixel of that co-ordinates",pixel)

#Accessing the blue pixel
blue = img2[520,580,0]
print("The pixel having blue color",blue)

green = img2[520,580,1]
print("The pixel having green color",green)

red = img2[520,580,2]
print("The pixel having red color",red)


# cv.imshow("Cat",img)

cv.waitKey(0)
cv.destroyAllWindows()