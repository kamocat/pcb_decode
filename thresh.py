import numpy as np
import cv2 as cv
img = cv.imread('cropped.png')
img = cv.medianBlur(img,5)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
th = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv.THRESH_BINARY,11,2)
cv.imshow('gaussian threshold',th)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("bw.png", th)
