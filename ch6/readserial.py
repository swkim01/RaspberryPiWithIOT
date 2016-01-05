import serial

con = serial.Serial('/dev/ttyAMA0', 9600)

while True:
    text = con.readlines()
    print text+'\r\n'
