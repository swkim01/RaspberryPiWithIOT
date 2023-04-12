import serial

con = serial.Serial(port='/dev/ttyS0',
                   baudrate=115200,
                   parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   bytesize=serial.EIGHTBITS,
                   timeout=1)

while True:
    text = con.readlines()
    if text:
        print(text[0].decode())
