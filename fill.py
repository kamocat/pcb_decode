import numpy as np
import cv2 as cv
import colormap
img = cv.imread('bw2.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('colored',img)
cv.waitKey(0)
cv.destroyAllWindows()

ymax = img.shape[0]-1
xmax = img.shape[1]-1
print(f'xmax: {xmax} ymax: {ymax}')

def Inside(x, y):
    if x<0 or x>xmax or y<0 or y>ymax :
        return False
    elif img[y,x] == 255:
        return True
    else:
        return False

# scan-and-fill implementation from Wikipedia
# https://en.wikipedia.org/wiki/Flood_fill#Span_Filling
def flood(img, mark, x, y):
    if not Inside(x,y):
        return
    s = []
    s.append((x,x,y))
    while( len(s) > 0 ):
        (x1, x2, y) = s.pop()
        if( x2 < x1 ):
            continue #empty span
        if( y<0 or y>ymax):
            continue # y is out of range
        x = x1
        # Fill to the left
        while Inside(x-1, y):
            img[y,x-1] = mark
            x = x-1
        # Search above
        s.append((x, x1-1, y-1))
        while (x1 < x2):
            # Fill to the right
            while Inside(x1,y):
                img[y, x1] = mark
                x1 = x1 + 1
            # Search below
            s.append((x, x1-1, y+1))
            x = x1
            # Continue searching designated span
            while (x1<x2) and not Inside(x,y):
                x1 = x1 + 1
        if (x > x2):
            # Search above
            s.append((x2, x, y-1))



#Flood colors in the image.
#   c = 0 #color index
#   for y in range(ymax):
#       print(y)
#       for x in range(xmax):
#           if( img[y,x] == 255 ): # Not filled yet
#               c = c + 1
#               flood(img, c, x, y)

flood(img,128,296,250)

#Create an indexed-color image to show the different regions
#colored = cv.applyColorMap(img, cv.COLORMAP_PLASMA)
cv.imshow('filled',img)
cv.waitKey(0)
cv.destroyAllWindows()
#cv.imwrite("filled.png", colored)
