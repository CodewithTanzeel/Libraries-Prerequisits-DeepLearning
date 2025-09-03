import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img = cv.imread('Photos/cat02.jpg')
cv.imshow("Image",img)

# plt.imshow(img)
# plt.show()



gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Image",gray)

# BGR TO HSV
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV IMAGE",hsv)
# BGR TO L*A*B
lab =cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab IMAGE",lab)
# BGR to RGB
rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB_IMAGE",rgb)
plt.imshow(rgb)
plt.show()
cv.waitKey(0)