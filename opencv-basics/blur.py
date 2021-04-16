import cv2 as cv

img = cv.imread('Photos/cat.jpg')
img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.2)), cv.INTER_LINEAR)
cv.imshow("Kittens", img)

# Averiging
average = cv.blur(img, (3,3))
cv.imshow('Average blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussin Blur", gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
