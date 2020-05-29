from flask import Flask, abort, make_response, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
#app.config['DEBUG'] = True
socketio = SocketIO(app, engineio_logger=True, cors_allowed_origins=[])

@socketio.on('connect')
def test_connect():
    print("Hello")
    emit('my response', {'data': 'Connected'})

@socketio.on('message')
def test_message():
    print("Hello2")

@app.route("/")
def hello():
    print("Starting")
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host="192.168.1.109", port=8010)
