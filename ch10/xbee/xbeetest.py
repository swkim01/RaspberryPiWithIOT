import serial

con = serial.Serial('/dev/ttyAMA0', 9600, timeout=3)

while True:
    msg = con.read(5)
    print msg
    if msg[:3] == 'REQ':
        print "Requested by Arduino"
        con.write("ACK"+'\r\n')
