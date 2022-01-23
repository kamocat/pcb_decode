import cv2 as cv
import numpy as np

hue = (0,10,20,25,30,35,40,60,70,80,90,98,105,112,120,127)
sat = (255,255,255,255,255,255,255,255,107,107,107,107,107,107,107,107)
value = (255,210,190,160,130,110,90,70,255,210,190,160,130,110,90,70)
colormap = np.empty((16,16,3), dtype=np.uint8)
for y in range(16):
    for x in range(16):
        colormap[y,x,:] = (hue[x],sat[y],value[y])
colormap = cv.cvtColor(colormap, cv.COLOR_HSV2BGR)
mycolors = colormap.reshape((256,3))

if (__name__ == '__main__'):
    img = np.arange(0,256,1, dtype=np.uint8)
    img = img.reshape((16,16))
    colored = cv.applyColorMap(img, mycolors)
    cv.waitKey(0)
    cv.destroyAllWindows()
