import cv2
import numpy as np

def diffImage(i):
    diff0 = cv2.absdiff(i[0], i[1])
    diff1 = cv2.absdiff(i[1], i[2])
    return cv2.bitwise_and(diff0, diff1)

def getGrayCameraImage(cam):
    img=cam.read()[1]
    gimg=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return gimg

def updateCameraImage(cam, i):
    i[0] = i[1]
    i[1] = i[2]
    i[2] = getGrayCameraImage(cam)

# setup video capture
if __name__ == "__main__":
    thresh = 32
    cam = cv2.VideoCapture(0)
    i = [None, None, None]
    for n in range(3):
        i[n] = getGrayCameraImage(cam)

    while True:
        diff = diffImage(i)
        ret,thrimg=cv2.threshold(diff, thresh, 1, cv2.THRESH_BINARY)
        count = cv2.countNonZero(thrimg)
        if (count > 20):
            nz = np.nonzero(thrimg)
            cv2.rectangle(diff,(min(nz[1]),min(nz[0])),(max(nz[1]),max(nz[0])),(255,0,0),2)
            cv2.rectangle(i[0],(min(nz[1]),min(nz[0])),(max(nz[1]),max(nz[0])),(0,0,255),2)
            cv2.imwrite('detect.jpg',i[0])

        cv2.imshow('Detecting Motion', diff)

        # process next image
        updateCameraImage(cam, i)

        key = cv2.waitKey(10)
        if key == 27:
            break
