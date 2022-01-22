import numpy as np
import cv2 as cv
img = cv.imread('cropped.png')
#TODO: Flood colors in the image.
#Control how small a gap the flood will go through
#Create an indexed-color image to show the different regions
cv.imshow('colored',img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("bw.png", th)
