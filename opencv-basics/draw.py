import numpy as np
import cv2 as cv

blank = np.zeros((500, 500, 3), dtype='uint8')


image = cv.imread('Photos/cat.jpg') 

#
blank[:] = 0, 255, 0

cv.imshow('blank', blank)
cv.rectangle(blank, (10,10), (300, 300), (0,0,255), thickness=-1)
cv.imshow('rect', blank)
#cv.imshow("cat", cv.resize(image, (500, 500), interpolation=cv.INTER_AREA))

cv.circle(blank, (250, 250), 40, (255, 0, 0), -1)
cv.imshow("circle", blank)

# line
cv.line(blank, (0,0), (500, 500), (255, 255, 255), 6)
cv.imshow("line", blank)
# text

cv.putText(blank, "FU", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 6.0, (150, 150, 150), 7)
cv.imshow('Text', blank)


cv.waitKey(0)