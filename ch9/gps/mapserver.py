#!/usr/bin/python3
from flask import Flask, render_template
import threading
import gps
import time
import gpsreceiver
import json

gpsr = gpsreceiver.GpsReceiver()
gpsr.daemon = True
gpsr.start()

app = Flask(__name__, template_folder=".", static_url_path='')

#respone json for gps location
@app.route('/getLocation')
def get_location():
    return json.dumps(gpsr.getLocation())

@app.route('/')
@app.route('/osm.html')
def do_route():
    return render_template("osm.html")

@app.route('/googlemap.html')
def do_googlemap():
    return render_template("googlemap.html")

if __name__ == '__main__':
    app.run(host='localhost', port=8008)
