from bottle import route, run, get, response
import cv2, cv

# setup video capture
cam = cv2.VideoCapture(0)
cam.set(cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

@get('/stream.mjpg')
def do_stream():
    response.set_header('Content-Type', 'multipart/x-mixed-replace; boundary=--MjpgBound')
    while True:
        ret,img = cam.read()
        jpegdata=cv2.imencode(".jpeg",img)[1].tostring()
        string = "--MjpgBound\r\n"
        string += "Content-Type: image/jpeg\r\n"
        string += "Content-length: "+str(len(jpegdata))+"\r\n\r\n"
        string += jpegdata
        string += "\r\n\r\n\r\n"
        yield string

@route('/')
def do_route():
   return "<HTML><BODY><img src=\"stream.mjpg\" width=320 height=240></BODY></HTML>"

run(host='192.168.0.48', port=8008)
