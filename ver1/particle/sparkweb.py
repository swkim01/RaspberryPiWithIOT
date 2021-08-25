#-*- coding: utf-8 -*-
from bottle import get, template, run

deviceId = "<장치ID>"
token = "<접근토큰>"

@get('/ssechart')
def dht11chart():
    return template("ssechart", device_id=deviceId, access_token=token)

@get('/')
def index():
    return template("index", device_id=deviceId, access_token=token)

if __name__ == '__main__':
    run(host="192.168.0.45", port=8008)
