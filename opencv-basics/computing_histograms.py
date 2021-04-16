import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/cat.jpg")
img = cv.resize(img, (int(img.shape[0]*.3), int(img.shape[1]*.2)), interpolation=cv.INTER_LINEAR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Creating hist
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()




cv.imshow("Original", img)
cv.waitKey(0)