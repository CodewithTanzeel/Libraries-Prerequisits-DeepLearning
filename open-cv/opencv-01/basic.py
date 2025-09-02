import cv2 as cv
img = cv.imread('Photos/cat01.jpg')
cv.imshow('Cat', img)
 # Converting into a GrayScale Image.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# Blurring an Image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)# to increse blur increase numric values
cv.imshow('Blur',blur)

# EDGE Cascade
canny = cv.Canny(img,125,175)
cv.imshow('Edge Cascade',canny)

#Dialating the image
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dialated',dilated)

#Eroding 
eroded =cv.erode(dilated,(7,7),iterations=1)
cv.imshow("ERODED",eroded)

#Resize
#resized =cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC)#ignoring the aspect ratio
# cv.imshow(resized)
#Cropping
cropped =img[50:200,200:40]
cv.imshow('Cropped',cropped)
cv.waitKey(0)