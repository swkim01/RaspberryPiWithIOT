import smbus, time

address = 0x48
cmd = 0x40
bus = smbus.SMBus(1)

def read(channel):
    try:
        bus.write_byte(address, cmd+channel) 
        bus.read_byte(address) # dummy read
    exception Exception as e:
        print(e)
    return bus.read_byte(address)

def write(val):
    try:
        bus.write_byte_data(address, cmd, int(val))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while True:
        reading = read(3)
        voltage = reading * 3.3 / 256
        print("읽은 값은 %d\t전압은 %f V" % (reading, voltage))
        time.sleep(1)

