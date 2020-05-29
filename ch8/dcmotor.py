import RPi.GPIO as GPIO
import time

en_pin = 18
m1a_pin = 23
m1b_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(en_pin, GPIO.OUT)
GPIO.setup(m1a_pin, GPIO.OUT)
GPIO.setup(m1b_pin, GPIO.OUT)
pwm = GPIO.PWM(en_pin, 500)
pwm.start(0)

speed=0
while True:
    cmd = raw_input("Command, f/r :")
    direction = cmd[0]
    if direction == "f":
        if speed < 100: speed+=10
        else: speed=100
    else:
        if speed > -100: speed-=10
    if speed > 0:
        GPIO.output(m1a_pin, True)
        GPIO.output(m1b_pin, False)
    elif speed < 0:
        GPIO.output(m1a_pin, False)
        GPIO.output(m1b_pin, True)
    else:
        GPIO.output(m1a_pin, True)
        GPIO.output(m1b_pin, False)
    print("speed=", speed)
    pwm.ChangeDutyCycle(abs(speed))
