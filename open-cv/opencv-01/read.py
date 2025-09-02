import cv2 as cv
# Reading Images
img = cv.imread('Photos/cat01.jpg')
cv.imshow('Cat',img)

#Reading Videos
capture = cv.VideoCapture('Videos/CatVideo-01.mp4')
while True:
    isTrue,frame= capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('b'):
        break
    
capture.release()
cv.destroyAllWindows()
    
#
cv.waitKey(0)

