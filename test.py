import cv2 as cv

img = cv.imread('12.png', cv.IMREAD_GRAYSCALE)
cv.imshow("image", img)
cv.waitKey(0)
