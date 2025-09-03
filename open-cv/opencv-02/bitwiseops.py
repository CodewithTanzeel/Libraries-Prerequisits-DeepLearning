import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat02.jpg')
# cv.imshow("BASE img",img)

blank = np.zeros((400,400),dtype="uint8")
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

cv.waitKey(0)