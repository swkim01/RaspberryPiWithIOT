import RPi.GPIO as GPIO
import lirc
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

ON = "on"
OFF = "off"

socketid = lirc.init("ledcontrol", blocking=False)

while (True):
    codeIR = lirc.nextcode()
    if len(codeIR) != 0:
        print codeIR
        if codeIR[0] == ON:
            GPIO.output(18, True)
        elif codeIR[0] == OFF:
            GPIO.output(18, False)
