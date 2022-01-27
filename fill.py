import numpy as np
import cv2 as cv
import pudb; pu.db
img = cv.imread('bw2.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('colored',img)
cv.waitKey(0)
cv.destroyAllWindows()

ymax = img.shape[0]-1
xmax = img.shape[1]-1
print(f'xmax: {xmax} ymax: {ymax}')

def Inside(x, y):
    if x<0 or x>xmax:
        return False
    return (img[y,x] == 255)

# scan-and-fill implementation from Wikipedia
# https://en.wikipedia.org/wiki/Flood_fill#Span_Filling
def flood(img, mark, x, y):
    if not Inside(x,y):
        return
    s = []
    s.append((x,x,y, 1))
    while( len(s) > 0 ):
        # (span_start, span_end, y, direction)
        (x1, x2, y, d) = s.pop()
        print(f'{x1}:{x1}, {y} {"up" if d<1 else "down"}')
        if( x2 < x1 ):
            continue #empty span
        if( y<0 or y>ymax):
            continue # y is out of range
        x = x1
        span_end = x1-1
        # Fill to the left
        while Inside(x-1, y):
            x = x-1
        span_start = x
        # Search above left
        s.append((span_start, span_end, y-d, -d))
        while (x < x2):
            x = span_end + 1
            # Fill to the right
            while Inside(x,y):
                x = x + 1
            # Search below
            span_end= x-1
            s.append((span_start, span_end, y+d, d))
            img[y, span_start:span_end] = mark
            # Continue searching designated span
            while not Inside(x,y):
                x = x + 1
            span_start = x
        # Search above right
        s.append((x2, span_end, y-d, -d))



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
