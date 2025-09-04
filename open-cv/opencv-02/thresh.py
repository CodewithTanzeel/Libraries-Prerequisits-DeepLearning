import cv2 as cv
img =cv.imread('Photos/cat02.jpg')
cv.imshow('Cats',img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)
#simple Thresholding
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple THRESHOLDING',thresh)

thresold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('INVERTED Thresholded',thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('ADAPTIVETHRESHOLDING',adaptive_thresh)




cv.waitKey(0)
