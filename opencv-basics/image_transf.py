import cv2 as cv
import numpy as np

img = cv.imread("Photos/piter.jpg")
cv.imshow("original", img)

# 1. Translation
def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# -x -> left
# -y -> up

translated = translate(img, 100, 100)
cv.imshow("translated", translated)

# 2. Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 450)
cv.imshow("Rotation", rotated)

# 3. Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# 4. Flipping
flip = cv.flip(img, 0) # 0 -vert, 1 -hor, -1 -both
cv.imshow("Flipped", flip)

# 5. Cropping
croped = img[200:400, 300:500]
cv.imshow("Cropped", croped)

cv.waitKey(0)