#-*- coding: utf-8 -*-
from bottle import get, template, run
try:
    from urllib.request import urlopen #python 3
except ImportError:
    from urllib2 import urlopen #python 2
#import json

deviceIp = "<장치 IP>"
portnum = "80"

base_url = "http://" + deviceIp + ":" + portnum
events_url = base_url + "/events"

@get('/events')
def getevents():
    u = urlopen(events_url)
    data = ""
    try:
        data = u.read()
    except urllib2.HTTPError as e:
        print("HTTP error: %d" % e.code)
    except urllib2.URLError as e:
        print("Network error: %s" % e.reason.args[1])
    return data

@get('/')
def dht22chart():
    return template("dhtchart")

if __name__ == '__main__':
    run(host="<서버 IP>", port=<PORT>)
