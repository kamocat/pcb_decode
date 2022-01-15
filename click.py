import numpy as np
import cv2 as cv
img = cv.imread('test_images/front.jpg')
# mouse callback function
def draw_circle(event,x,y,flags,param):
    size = 30
    if event == cv.EVENT_LBUTTONDBLCLK:
        sub = img[y-size:y+size, x-size:x+size] 
        cv.imshow('ROI', sub)
# Create a black image, a window and bind the function to window
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
cv.imshow('image',img)
while(1):
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
