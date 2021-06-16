#-*- coding: utf-8 -*-
from flask import Flask, request, Response, render_template
try:
    from urllib.request import urlopen #python 3
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib2 import urlopen #python 2
    from urllib2 import HTTPError, URLError
import json, time

deviceIp = "192.168.0.45"
portnum = "80"

base_url = "http://" + deviceIp + ":" + portnum
led_url = base_url + "/led"
events_url = base_url + "/events"

app = Flask(__name__, template_folder=".")

@app.route('/led', methods=['POST'])
def controlled():
    l = request.get_data()
    if l == "ON":
        u = urlopen(led_url, "on")
    elif l == "OFF":
        u = urlopen(led_url, "off")
    return ""

@app.route('/events')
def getevents():
    u = urlopen(events_url)
    data = ""
    try:
        #data = u.readlines()
        data = u.read()

        #js = json.JSONDecoder()
        #d = js.decode(data)
        #print d
    except HTTPError as e:
        print("HTTP error: %d" % e.code)
    except URLError as e:
        print("Network error: %s" % e.reason.args[1])
    return data

@app.route('/dhtchart')
def dht22chart():
    return render_template("dhtchart.html")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="192.168.0.15", port=8008)
