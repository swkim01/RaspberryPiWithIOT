import serial

con = serial.Serial('/dev/ttyAMA0', 9600)

while True:
    text = raw_input("Input any text message: ")
    con.write(text+'\r\n')
