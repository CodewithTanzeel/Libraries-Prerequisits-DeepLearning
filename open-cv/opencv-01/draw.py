import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
#paint the image a Certain color,
# blank[:] = 0,255,213
# cv.imshow('Musturd',blank)
# Color in range of pixels
# blank[200:300,300:400] = 0,255,0
# cv.imshow('Musturd',blank)
#Drawing a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
# cv.imshow("rectangle",blank)


cv.putText(blank,'This',(255,255),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1.0,(0,0,255),2)
cv.imshow("Text",blank)
img = cv.imread('Photos/cat01.jpg')
cv.imshow("Cat",img)


cv.waitKey(0) 