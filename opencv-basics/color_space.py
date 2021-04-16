import cv2 as cv

img = cv.imread('Photos/piter.jpg')
img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.2)),interpolation=cv.INTER_LINEAR)
cv.imshow("Piter", img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)


cv.waitKey(0)





