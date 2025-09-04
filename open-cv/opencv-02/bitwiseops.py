import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat02.jpg')
# cv.imshow("BASE img",img)

blank = np.zeros((400,400),dtype="uint8")
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

#Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("BIWISE AND IMAGE",bitwise_and)
#Bitwise or
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("BIWISE OR IMAGE",bitwise_or)
#Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("BIWISE XOR IMAGE",bitwise_xor)
#Bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow("BIWISE NOT IMAGE",bitwise_not)
cv.waitKey(0)
