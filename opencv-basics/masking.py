import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.2)), interpolation=cv.INTER_LINEAR)

blank = np.zeros(img.shape[:2], dtype="uint8")

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("MASK", mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked", masked)




cv.imshow("Original", img)


cv.waitKey(0)