import serial

con - serial.Serial('/dev/serial0', 9600)
while True:
    print(con.readline())
