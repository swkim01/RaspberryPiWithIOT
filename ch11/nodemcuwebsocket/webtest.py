#-*- coding: utf-8 -*-
import math, time
try:
    from urllib.request import urlopen #python 3
except ImportError:
    from urllib2 import urlopen #python 2
import json

base_url = "http://192.168.0.35/"
led_url = base_url + "led"
events_url = base_url + "events"

print led_url
u = urlopen(led_url, "on")

time.sleep(2)

u = urlopen(led_url, "off")

time.sleep(2)

print events_url

u = urlopen(events_url)
try:
    #data = u.readlines()
    data = u.read()
    #print data, len(data)

    js = json.JSONDecoder()
    d = js.decode(data)
    print d
except urllib2.HTTPError, e:
    print "HTTP error: %d" % e.code
except urllib2.URLError, e:
    print "Network error: %s" % e.reason.args[1]
