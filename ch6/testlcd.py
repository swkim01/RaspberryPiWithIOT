from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep

lcd = Adafruit_CharLCD(pin_rs=22, pin_e=11, pins_db=[23, 10, 9, 25])
lcd.begin(16,2)
i = 0
while True:
    lcd.clear()
    lcd.message('Counting: ' + str(i))
    sleep(1)
    i = i + 1
