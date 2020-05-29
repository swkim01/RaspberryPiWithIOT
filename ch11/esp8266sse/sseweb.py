#-*- coding: utf-8 -*-
from flask import Flask, Response, render_template
try:
    from urllib.request import urlopen #python 3
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib2 import urlopen #python 2
    from urllib2 import HTTPError, URLError
import json, time

#deviceIp = "<장치IP>"
#deviceIp = "192.168.1.112"
deviceIp = "192.168.0.16"
portnum = "80"

base_url = "http://" + deviceIp + ":" + portnum
led_url = base_url + "/led"
events_url = base_url + "/events"

app = Flask(__name__, template_folder=".")

@app.route('/led', methods=['POST'])
def ledcontrol():
    u = urlopen(led_url)
    data = ""
    try:
        data = u.read()
    except HTTPError as e:
        print("HTTP error: %d" % e.code)
    except URLError as e:
        print("Network error: %s" % e.reason.args[1])
    print(data)
    return "OK"

def getevents():
    '''this could be any function that block'''
    u = urlopen(events_url)
    data = ""
    try:
        msg = json.loads(u.read())
    except HTTPError as e:
        print("HTTP error: %d" % e.code)
    except URLError as e:
        print("Network error: %s" % e.reason.args[1])
    for key, value in msg.items():
        #data += "event: {0}\ndata: \"{1}\"\n\n".format(key, value)
        data += "event: {0}\ndata: {1}\n\n".format(key, json.dumps({'data': value}))
    print(data)
    return data

@app.route('/events')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            #yield 'data: {}\n\n'.format(get_message())
            time.sleep(5)
            yield getevents()
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ssechart')
def dht11chart():
    return render_template("ssechart.html")

if __name__ == '__main__':
    #app.run(host="192.168.1.109", port=8008)
    app.run(host="192.168.0.15", port=8008)
