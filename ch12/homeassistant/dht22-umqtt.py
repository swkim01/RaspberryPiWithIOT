import time, ubinascii
from umqtt.simple import MQTTClient
from machine import Pin, unique_id
import dht

SERVER = "<IP 주소>"
CLIENT_ID = ubinascii.hexlify(unique_id())
TOPIC = b"home/temperature"

def main(server=SERVER):
    d = dht.DHT22(Pin(4))
    c = MQTTClient(CLIENT_ID, SERVER)
    c.connect()
    fail = False
    while True:
        d.measure()
        try:
            c.publish(TOPIC, str(d.temperature()).encode('UTF8'))
            print('Publish')
            fail = False
        except OSError:
            fail = True
        time.sleep_ms(10000)
        try:
            if fail:
                print('Attempt to reconnect')
                c.connect()
                print('Reconnected to nodemcu')
        except OSError:
            print('Reconnect fail')
    c.disconnect()
main()
