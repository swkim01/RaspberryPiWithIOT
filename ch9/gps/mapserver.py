#!/usr/bin/python
from bottle import route,run,get,response,static_file,request
import threading
import gps
import time
import gpsreceiver

gpsr = gpsreceiver.GpsReceiver()
gpsr.daemon = True
gpsr.start()

#respone json for gps location
@get('/getLocation')
def get_location():
    return gpsr.getLocation()

@route('/')
@route('/osm.html')
def do_route():
    return static_file("osm.html", root=".")

@route('/googlemap.html')
def do_googlemap():
    return static_file("googlemap.html", root=".")

@route('/geolocation_marker.png')
def do_marker():
    return static_file("geolocation_marker.png", root=".")

run(host='192.168.0.31', port=8008)
