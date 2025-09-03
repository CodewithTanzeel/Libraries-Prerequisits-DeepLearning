import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat02.jpg')
cv.imshow("Image",img)
blank = np.zeros(img.shape[:2],dtype = 'uint8')
cv.imshow('Blank',blank)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Image",gray)
# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("BLURIMAGE",blur)

# canny = cv.Canny(img,155,185)
# cv.imshow("Image",canny)
ret,thresh = cv.threshold(gray,125,155,cv.THRESH_BINARY)
cv.imshow("Thresholed IMAGE",thresh)

contours,hierarchies =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)


print(f'{len(contours)} in total were found')

cv.waitKey(0)