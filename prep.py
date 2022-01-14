import cv2 as cv
import sys

front = cv.imread('test_images/front.jpg')

if front is None:
    sys.exit('Could not read the image.')

cv.imshow('Display window', front)
k = cv.waitKey(0)

