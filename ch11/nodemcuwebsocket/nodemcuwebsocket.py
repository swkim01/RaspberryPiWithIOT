#-*- coding: utf-8 -*-
from flask import Flask, Response, render_template, session
from flask_socketio import SocketIO, emit, join_room
import json, time, os

app = Flask(__name__, template_folder=".")
#app.config['SECRET_KEY'] = 'secret!'
#socketio = SocketIO(app=app, async_mode=None)
#socketio = SocketIO(app=app, logger=True)
#socketio = SocketIO(app=app, logger=True, enginio_logger=True, cors_allowed_origins=[])
socketio = SocketIO(app=app, logger=True, cors_allowed_origins='*')

#user_no = 1
#@app.before_request
#def before_request():
#    global user_no
#    if 'session' in session and 'user-id' in session:
#        pass
#    else:
#        session['session'] = os.urandom(24)
#        session['username'] = 'user'+str(user_no)
#        user_no += 1
#
#@socketio.on('connect')
#def connect():
#    emit("response", {'data': 'Connected', 'username': session['username']})

@socketio.on('join_web')
def join_web(message):
    print('on_join_web');
    join_room('WEB');

@socketio.on('join_dev')
def join_dev(message):
    print('on_join_dev');
    join_room('DEV');

@socketio.on('led')
def controlled(message):
    l = message['data']
    if l == "ON":
        emit('led_control', {'data': 'on'}, room='DEV');
    elif l == "OFF":
        emit('led_control', {'data': 'off'}, room='DEV');

@socketio.on('events')
def getevents(message):
    #data = message['data']
    #data = json.loads(message['data'])
    #obj = "{" + "temperature: {0}, humidity: {1}".format(data['temperature'], data['humidity']) + "}"
    #print(obj)
    #emit('dht_chart', {'temperature': data['temperature'], 'humidity': data['humidity']}, room='WEB');
    emit('dht_chart', {'data': message}, room='WEB');

@socketio.on_error()
def chat_error_handler(e):
    print('An error has occurred: ' + str(e))

@app.route('/dhtchart')
def dht22chart():
    return render_template("dhtchart.html")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app=app, host="192.168.1.109", port=8010)
