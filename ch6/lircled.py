import RPi.GPIO as GPIO
from lirc import LircdConnection
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

ON = "on"
OFF = "off"

#old code
#import lirc
#socketid = lirc.init("ledcontrol", blocking=False)
#while (True):
#    codeIR = lirc.nextcode()
#    if len(codeIR) != 0:
#        print(codeIR)
#        if codeIR[0] == ON:
#            GPIO.output(18, True)
#        elif codeIR[0] == OFF:
#            GPIO.output(18, False)
with LircdConnection("ledcontrol") as conn:
    while (True):
        codeIR = conn.readline()
        if len(codeIR) != 0:
            print(codeIR)
            if codeIR == ON:
                GPIO.output(26, True)
            elif codeIR == OFF:
                GPIO.output(26, False)
