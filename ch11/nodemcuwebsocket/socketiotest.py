#-*- coding: utf-8 -*-
import math, time
import socketio
import json

sio = socketio.Client()

@sio.event
def message(data):
    print('I received a message!')

@sio.on('led_control')
def on_connect(data):
    print("I reeived led_control")

@sio.event
def connect():
    print("I'm connected!")
    sio.emit('join_dev', {'room': 'DEV'})

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

n = 0
def send_event(my_args):
    global n
    while True:
        n += 1
        temp = 25.0 + n % 10
        humi = 30.0 + (n + 1) % 20
        data = json.dumps({'temperature': temp, 'humidity': humi})
        print(data)
        sio.emit('events', {'data': data})
        time.sleep(5)

base_url = "http://"
serverIp = "192.168.1.109"
port = 8010
sio.connect(base_url+serverIp+":"+str(port), transports='websocket')

time.sleep(2)
sio.start_background_task(send_event, 123)
sio.wait()
