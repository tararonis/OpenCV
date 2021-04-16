import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.2)), interpolation=cv.INTER_LINEAR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255,cv.THRESH_BINARY)
cv.imshow("SImple threshold", thresh)
 

threshold, thresh_inv = cv.threshold(gray, 150, 255,cv.THRESH_BINARY_INV)
cv.imshow("SImple threshold INVERSE", thresh_inv)
print(threshold)

# Adaptibe Threshold
adaptibe_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow("Adaptive", adaptibe_thresh) 

cv.waitKey(0)