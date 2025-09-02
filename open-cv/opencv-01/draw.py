import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
#paint the image a Certain color,
blank[:] = 0,255,213
cv.imshow('Musturd',blank)

img = cv.imread('Photos/cat01.jpg')
cv.imshow("Cat",img)


cv.waitKey(0)