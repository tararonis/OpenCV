import cv2 as cv
import numpy as np

img = cv.imread("Photos/piter.jpg")
img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.2)), interpolation=cv.INTER_LINEAR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplatian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)

combined = cv.bitwise_or(sobelx, sobely)

cv.imshow("Combined", combined)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)


cv.imshow("Original", img)
cv.waitKey(0)