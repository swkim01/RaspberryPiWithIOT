import RPi.GPIO as GPIO
import time

pwm_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)
angle = 4
pwm.start(angle)

while True:
    cmd = input("Command, f/r: ")
    direction = cmd[0]
    if direction == "f":
        angle += 1
    else:
        angle -= 1
    if angle < 4:
        angle = 4
    elif angle > 22:
        angle = 22
    print("angle=", (angle-4)*10)
    pwm.ChangeDutyCycle(angle)
