from time import sleep
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

lcd = CharLCD(pin_rs=22, pin_e=11, pins_data=[23, 10, 9, 25],
                      numbering_mode=GPIO.BCM)
i = 0
while True:
    lcd.clear()
    lcd.write_string('Counting: ' + str(i))
    sleep(1)
    i = i + 1
