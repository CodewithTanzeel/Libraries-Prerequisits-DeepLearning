import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat02.jpg')
cv.imshow("Cat",img)


#Translate

def translate(img,x,y):
    transMAT =np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMAT,dimensions)


# -x --->left
# -y --->up
# x --->Right
# y --->Down

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        
    rotMAT = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img,rotMAT,dimensions)

rotated = rotate(img,-45)# minus for roatating clock wise image
cv.imshow("RotatedImage",rotated)
rotated_rotated = rotate(img,45)
cv.imshow('Roatated Rotated',rotated_rotated)

 #Resizing
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image',resized)
#Flipping
flipped = cv.flip(img,0)
cv.imshow("Flipped img",flipped)
#cropping 
cropped = img[300:400,150:350]
cv.imshow("CroppedImage",cropped)


translated = translate(img,100,100)
cv.imshow('Translated',translated)

cv.waitKey(0)