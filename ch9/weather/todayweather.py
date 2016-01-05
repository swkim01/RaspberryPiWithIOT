#!/usr/bin/python
import kma
import RPi.GPIO as GPIO
import time

redPin = 18
yellowPin = 23
greenPin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

GPIO.output(redPin, False)
GPIO.output(yellowPin, False)
GPIO.output(greenPin, False)

lat = 35.0
lon = 129.0
mincount = 0
wcode = 0

while mincount < 1:
    data = kma.getWeather(lat, lon)
    for item in data:
        day = int(item[1])
        hour = int(item[0])
        if day == 0 and hour >= 12:
            wcode = kma.getWeatherCode(item[2])
            break
    if wcode >= 1 and wcode <= 2:
        GPIO.output(greenPin, True)
    elif wcode >= 3 and wcode <= 4:
        GPIO.output(yellowPin, True)
    elif wcode >= 5:
        GPIO.output(redPin, True)
    mincount += 1
    time.sleep(60)

GPIO.output(redPin, False)
GPIO.output(yellowPin, False)
GPIO.output(greenPin, False)
