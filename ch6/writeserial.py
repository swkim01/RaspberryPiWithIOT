import serial

con = serial.Serial(port='/dev/ttyUSB0',
                   baudrate=115200,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   bytesize=serial.EIGHTBITS,
                   timeout=1)

while True:
    text = raw_input("Input any text message: ")
    con.write(text.encode())
