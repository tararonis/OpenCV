import cv2 as cv

img = cv.imread("Photos/piter.jpg")
img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.1)), interpolation=cv.INTER_AREA)

# 1. Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

# 2. Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow("blur", blur)

# 3. Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# 4. Dilating the img
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("dil", dilated)

# 5. Eroding the img
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("eroded", eroded)

# 6. Resize
resized = cv.resize(img, (600,600), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# 7. Cropping
cropped = img[50:200, 200:400]
cv.imshow("croped", cropped)

cv.imshow('cat', img)
cv.waitKey(0)