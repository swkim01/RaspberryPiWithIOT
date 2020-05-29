import logging
import usocketio.client
from machine import Pin
import time
import dht

logging.basicConfig(level=logging.DEBUG)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(4))
state = 0

serverIp = '192.168.1.109'
port = '8010'

with usocketio.client.connect('http://'+serverIp+':'+port+'/') as socketio:
    @socketio.on('led_control')
    def on_led(self, message):
        state = (state + 1) % 2
        led.value(state)
        print("led", state)

    @socketio.at_interval(5)
    def sendevent(self, message):
        d.measure()
        temp = d.temperature()
        humi = d.humidity()
        socketio.emit("events", "{\"temperature\": " +str(temp)+", \"humidity\": " + str(humi) + "}")

    socketio.emit("join_dev", "{\"room\": \"DEV\"}")

    socketio.run_forever()
