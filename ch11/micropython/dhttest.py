from machine import Pin
import time
import dht

led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(4))

state = 0
led.value(state)
time.sleep(1)
state = (state + 1) % 2
led.value(state)
time.sleep(1)
d.measure()
temp = d.temperature()
humi = d.humidity()
print(temp, humi)
