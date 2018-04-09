import spidev, time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000
#spi.mode - 3

def ee_write(offset, value):
    #spi.xfer2([0x84, 0xff, offset>>8, offset&0xff, value],3000000,12)
    spi.xfer2([0x84, 0xff, offset>>8, offset&0xff, value])

def ee_read(offset):
    #value = spi.xfer2([0xd4, 0xff, offset>>8, offset&0xff, 0xff, 0xff],3000000,12)
    value = spi.xfer2([0xd4, 0xff, offset>>8, offset&0xff, 0xff, 0xff])[5]
    return value

for i in range(256):
    ee_write(i, i)
if ee_read(1) != 1:
    print "open error"
else:
    for i in range(256):
        print ee_read(i)
        time.sleep(0.005)

spi.close()
