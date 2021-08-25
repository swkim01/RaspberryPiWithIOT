#!/usr/bin/python3
from pushbullet import PushBullet
from pushbullet import Listener
import RPi.GPIO as GPIO
import time

api_key = "<API KEY>"
HTTP_PROXY_HOST = None
HTTP_PROXY_PORT = None

redPin = 18
yellowPin = 23
greenPin = 24

def init_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(redPin, GPIO.OUT)
    GPIO.setup(yellowPin, GPIO.OUT)
    GPIO.setup(greenPin, GPIO.OUT)

def leds_off():
    GPIO.output(redPin, False)
    GPIO.output(yellowPin, False)
    GPIO.output(greenPin, False)

def on_push(data):
    pushes = pb.get_pushes()
    latest = pushes[1][0]
    if 'TodaysWeather' in latest.get('title'):
        body = latest.get('body')
        if any(x in body for x in ['Sunny', 'Clear']):
            GPIO.output(greenPin, True)
        elif 'Cloud' in body:
            GPIO.output(yellowPin, True)
        elif any(x in body for x in ['Rain', 'Shower', 'Snow']):
            GPIO.output(redPin, True)
        # sleep 1 hour
        time.sleep(3600)
        leds_off()

if __name__ == "__main__":
    pb = PushBullet(api_key)
    s = Listener(account=pb, on_push=on_push,
                 http_proxy_host=HTTP_PROXY_HOST,
                 http_proxy_port=HTTP_PROXY_PORT)
    init_leds()

    try:
        s.run_forever()
    except KeyboardInterrupt:
        s.close()
        leds_off()
