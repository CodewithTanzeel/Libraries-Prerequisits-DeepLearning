import cv2 as cv
import numpy as np


img = cv.imread("Photos/cat02.jpg")
cv.imshow("BASEIMG",img)
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)

mask =cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('MASKIMG',mask)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("MASKEDIMG",masked)

cv.waitKey(0)