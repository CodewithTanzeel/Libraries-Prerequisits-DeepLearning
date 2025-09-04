import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/women.jpg')
cv.imshow("image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale image",gray)