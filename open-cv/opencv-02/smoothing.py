import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Photos/cat02.jpg')
cv.imshow("BASEIMG",img)
#AVERAGING
average = cv.blur(img,(4,4))
cv.imshow('AverageBlur',average)
#GAUSSIANBLUR
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('GAUSSAINBlur',gauss)

#MEDIAN BLUR
median = cv.medianBlur(img,3)
cv.imshow("MEDIAN IMAGE",median)

#BILATREL
bilateral =cv.bilateralFilter(img,15,15,15)
cv.imshow('Bilateral IMAGE',bilateral)


cv.waitKey(0)