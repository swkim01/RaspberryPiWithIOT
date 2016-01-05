import serial

con - serial.Serial('/dev/ttyAMA0', 9600)
while True:
    print con.readline()
