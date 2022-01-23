import numpy as np
import cv2 as cv
import colormap
img = cv.imread('bw2.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('colored',img)
cv.waitKey(0)
cv.destroyAllWindows()
# Remove small noise
img = cv.medianBlur(img, 5)

#Flood colors in the image.
#Control how small a gap the flood will go through
kernel = 3
c = 0 #color index
for y in range(img.shape[0] - kernel):
    for x in range(img.shape[1] - kernel):
        roi = img[y:y+kernel, x:x+kernel]
        a = np.amin(roi)
        if( a == 255 ):
            c = c + 1
            np.copyto(roi, c)
        elif(a > 0):
            np.copyto(roi, a)

#Create an indexed-color image to show the different regions
colored = cv.applyColorMap(img, colormap.mycolors)
cv.imshow('colored',img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("filled.png", colored)
