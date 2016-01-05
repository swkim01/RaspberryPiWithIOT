import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(24, GPIO.IN)
count = 0
while True:
    value = GPIO.input(24)
    #value = GPIO.input(24)
    if value == True:
        count = count + 1
        print count
    time.sleep(0.1)
