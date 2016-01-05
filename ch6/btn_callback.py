import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
count = 0
def handler(channel):
    global count
    count = count + 1
    print count
    
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24, GPIO.RISING, callback=handler)
while True:
    time.sleep(1)
