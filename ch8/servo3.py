from RPIO as GPIO
import time

pwm_pin = 18
servo = GPIO.PWM.Servo()
angle = 4
servo.set_servo(pwm_pin, angle * 100)

while True:
    cmd = raw_input("Command, f/r: ")
    direction = cmd[0]
    if direction == "f":
        angle += 1
    else:
        angle -= 1
    if angle < 4:
        angle = 4
    elif angle > 23:
        angle = 23
    print "angle=", (angle-4)*10
    servo.set_servo(pwm_pin, angle * 100)

GPIO.cleanup()
