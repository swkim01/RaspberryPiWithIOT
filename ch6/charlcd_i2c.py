from time import sleep
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8674', address=0x27, port=1, cols=16, rows=2)
i = 0
while True:
    lcd.clear()
    lcd.write_string('Counting: ' + str(i))
    sleep(1)
    i = i + 1
