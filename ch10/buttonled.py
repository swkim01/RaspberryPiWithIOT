import pyfirmata
import time
board = pyfirmata.Arduino('/dev/ttyACM0')
led_pin = board.get_pin('d:5:o')
switch_pin = board.get_pin('d:4:i')
pyfirmata.util.Iterator(board).start()
switch_pin.enable_reporting()
while True:
    input_state = switch_pin.read()
    if input_state == True:
        led_pin.write(1)
    else:
        led_pin.write(0)
    time.sleep(0.2)
board.exit()
