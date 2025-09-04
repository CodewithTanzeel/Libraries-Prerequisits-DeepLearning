import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/women.jpg')
cv.imshow("image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale image",gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print(f'Number of faces found ={len(faces_rect)}')



for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,225,0),thickness = 2)

cv.imshow("Dectected Faces",img)




cv.waitKey(0)