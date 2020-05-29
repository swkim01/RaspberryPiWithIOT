#-*- coding: utf-8 -*-
from bottle import get, post, request, template, run
try:
    from urllib.request import urlopen #python 3
except ImportError:
    from urllib2 import urlopen #python 2
#import json

deviceIp = "192.168.0.45"
portnum = "80"

base_url = "http://" + deviceIp + ":" + portnum
led_url = base_url + "/led"
events_url = base_url + "/events"

@post('/led')
def controlled():
    l = request.body.read()
    if l == "ON":
        u = urlopen(led_url, "on")
    elif l == "OFF":
        u = urlopen(led_url, "off")

@get('/events')
def getevents():
    u = urlopen(events_url)
    data = ""
    try:
        #data = u.readlines()
        data = u.read()

        #js = json.JSONDecoder()
        #d = js.decode(data)
        #print d
    except urllib2.HTTPError, e:
        print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
        print "Network error: %s" % e.reason.args[1]

    return data

@get('/dhtchart')
def dht22chart():
    return template("dhtchart")

@get('/')
def index():
    return template("index")

if __name__ == '__main__':
    run(host="192.168.0.31", port=8008)
