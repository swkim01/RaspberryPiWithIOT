import RPIO
import time
RPIO.setmode(RPIO.BCM)
RPIO.setup(18, RPIO.OUT)
while (True):
    RPIO.output(18, True)
    time.sleep(1)
    RPIO.output(18, False)
    time.sleep(1)
