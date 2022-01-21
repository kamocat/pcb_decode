from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import sys
import corner

source_window = 'Source image'
corners_window = 'Corners detected'
max_thresh = 255

# Load source image and convert it to gray
parser = argparse.ArgumentParser(description='Code for Harris corner detector tutorial.')
parser.add_argument('--input', help='Path to input image.',
        default='test_images/fslaser_front.jpg')
args = parser.parse_args()
src = cv.imread(args.input)
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
# Create a window and a trackbar
cv.namedWindow(source_window)
cv.imshow(source_window, src)
thresh = 180 # initial threshold
# mouse callback function
def select_ROI(event,x,y,flags,param):
    size = 30
    if event == cv.EVENT_LBUTTONDBLCLK:
        sub = src[y-size:y+size, x-size:x+size, :] 
        corner.fast(thresh, sub)
cv.setMouseCallback(source_window,select_ROI)
cv.waitKey()
