import cv2
#import numpy

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 7)
#cv2mat = numpy.array([])

while True:
    ret,im = cam.read()
    #ret1=cv2.imencode(".jpeg",im,cv2mat)
    #JpegData=cv2mat.tostring()
    #print JpegData
    cv2.imshow('video test',im)
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('capture.jpg',im)

