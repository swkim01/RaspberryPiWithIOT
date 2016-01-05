import spidev, time

class L3G4200D(object):

    WHO_AM_I = 0x0F
    CTRL_REG1 = 0x20
    CTRL_REG2 = 0x21
    CTRL_REG3 = 0x22
    CTRL_REG4 = 0x23
    CTRL_REG5 = 0x24
    OUT_X_L = 0x28
    OUT_X_H = 0x29
    OUT_Y_L = 0x2A
    OUT_Y_H = 0x2B
    OUT_Z_L = 0x2C
    OUT_Z_H = 0x2D

    def read_register(self, address):
        data = self.spi.xfer2([address|0x80, 0xFF])[1]
        return data

    def write_register(self, address, data):
        self.spi.xfer2([address, data])

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        #print "mode=%d, max_speed_hz=%d" % (self.spi.mode, self.spi.max_speed_hz)

        if self.read_register(self.WHO_AM_I)&0xFF is not 0xD3:
            print "error"
        # Enable x, y, z and bandwidth 800Hz, cutoff 30Hz and turn off power down
        self.write_register(self.CTRL_REG1, 0xCF)
        # adjust/use the HPF cutoff 30Hz
        self.write_register(self.CTRL_REG2, 0x01)
        # No interrupts used on INT1, Data Ready on INT2
        self.write_register(self.CTRL_REG3, 0x08)
        # full-scale range
        self.write_register(self.CTRL_REG4, 0x00)
        # output selection 
        self.write_register(self.CTRL_REG5, 0x02)

    def close(self):
        spi.close()

    def readList(self):
        x = ((self.read_register(self.OUT_X_H)&0xFF)<<8)|self.read_register(self.OUT_X_L)
        if x & 0x8000: x -= 65536
        y = ((self.read_register(self.OUT_Y_H)&0xFF)<<8)|self.read_register(self.OUT_Y_L)
        if y & 0x8000: y -= 65536
        z = ((self.read_register(self.OUT_Z_H)&0xFF)<<8)|self.read_register(self.OUT_Z_L)
        if z & 0x8000: z -= 65536
        fs=self.read_register(self.CTRL_REG4)&0x30
        c1=self.read_register(self.CTRL_REG1)

        s = 0.
        if fs == 0x00: s=8.75
        elif fs == 0x10: s=17.5
        elif fs == 0x20: s=70
        elif fs == 0x30: s=70
        return [x * s / 1000, y * s / 1000, z * s / 1000]


if __name__ == '__main__':

    l3d4200d = L3G4200D()

    while True:
        data = l3d4200d.readList()
        print("read value is %f,\t %f,\t %f" % (data[0], data[1], data[2]))
        time.sleep(1)

    l3d4200d.close()
