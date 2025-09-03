import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Photos/cat02.jpg')
cv.imshow("Image",img)
blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r =cv.split(img)
blue = cv.merge([b,blank,blank])
green = cv.merge([g,blank,blank])
red = cv.merge([r,blank,blank])
cv.imshow("blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
merge = cv.merge([b,g,r])
cv.imshow("MERGEDIMAGE",merge)
cv.waitKey(0)