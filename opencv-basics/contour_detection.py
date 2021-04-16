import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpeg")
#img = cv.resize(img, (int(img.shape[0]*.2), int(img.shape[1]*.1)),interpolation=cv.INTER_LINEAR)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("GrayRGB", gray)

blank = np.zeros(img.shape, dtype='uint8')


#blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow("Blur", blur)
#grayBGR = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("GrayBGR", grayBGR)

#canny = cv.Canny(blur, 125, 175)
#cv.imshow("Canny", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'We found: {len(contours)}')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours", blank)

cv.imshow("Original",img)

cv.waitKey(0)