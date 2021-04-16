import cv2 as cv
import numpy as np

img = cv.imread('Photos/piter.jpg')
img = cv.resize(img, (int(img.shape[0]*.2), int(img.shape[1]*.2)), cv.INTER_LINEAR)
cv.imshow('Piter', img)

b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank,blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

print(green.shape)
print(blue.shape)
print(red.shape)
print(img.shape)

cv.waitKey(0)