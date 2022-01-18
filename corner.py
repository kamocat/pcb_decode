import cv2 as cv
import numpy as np

corners_window = 'Corners detected'
def Harris(val, img):
    src_gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)[:,:,1]
    thresh = val
    # Detector parameters
    blockSize = 2
    apertureSize = 3
    k = 0.04
    # Detecting corners
    dst = cv.cornerHarris(src_gray, blockSize, apertureSize, k)
    # Normalizing
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    dst_norm_scaled = cv.convertScaleAbs(dst_norm)
    # Drawing a circle around corners
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i,j]) > thresh:
                print(f'{i},{j}: {dst_norm[i,j]}')
                cv.circle(dst_norm_scaled, (j,i), 5, (0), 2)
    # Showing the result
    cv.namedWindow(corners_window)
    cv.imshow(corners_window, dst_norm_scaled)

def ShiTomasi(val, img):
    src_gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)[:,:,1]
    maxCorners = max(val, 1)
    # Parameters for Shi-Tomasi algorithm
    qualityLevel = 0.01
    minDistance = 10
    blockSize = 3
    gradientSize = 3
    useHarrisDetector = False
    k = 0.04
    # Apply corner detection
    corners = cv.goodFeaturesToTrack(src_gray, maxCorners, qualityLevel, minDistance, None, \
        blockSize=blockSize, gradientSize=gradientSize, useHarrisDetector=useHarrisDetector, k=k)
    # Draw corners detected
    print('** Number of corners detected:', corners.shape[0])

def fast(val, img):
    src_gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)[:,:,1]
    # Initiate FAST object with default values
    fast = cv.FastFeatureDetector_create()
    # find and draw the keypoints
    kp = fast.detect(src_gray,None)
    img2 = cv.drawKeypoints(src_gray, kp, None, color=(255,0,0))
    # Print all default params
    print( "Threshold: {}".format(fast.getThreshold()) )
    print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
    print( "neighborhood: {}".format(fast.getType()) )
    print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
    cv.imwrite('fast_true.png', img2)
    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
    img3 = cv.drawKeypoints(src_gray, kp, None, color=(255,0,0))

