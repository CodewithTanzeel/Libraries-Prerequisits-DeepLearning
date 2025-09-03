import cv2 as cv
img = cv.imread('Photos/cat02.jpg')
cv.imshow("Image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Image",gray)
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("BLURIMAGE",blur)

canny = cv.Canny(img,155,185)
cv.imshow("Image",canny)
contours,hierarchies =cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} in total were found')

cv.waitKey(0)