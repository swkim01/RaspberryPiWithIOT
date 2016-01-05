#!/usr/bin/python
import smbus
import time

class L3G4200D(object):

    # Minimal constants carried over from Arduino library
    L3G4200D_ADDRESS = 0x69   #t0110100x
    address = L3G4200D_ADDRESS

    L3G4200D_REGISTER_WHO_AM_I = 0x0F
    L3G4200D_REGISTER_CTRL_REG1 = 0x20
    L3G4200D_REGISTER_CTRL_REG2 = 0x21
    L3G4200D_REGISTER_CTRL_REG3 = 0x22
    L3G4200D_REGISTER_CTRL_REG4 = 0x23
    L3G4200D_REGISTER_CTRL_REG5 = 0x24
    L3G4200D_REGISTER_OUT_X_L = 0x28
    L3G4200D_REGISTER_OUT_X_H = 0x29
    L3G4200D_REGISTER_OUT_Y_L = 0x2A
    L3G4200D_REGISTER_OUT_Y_H = 0x2B
    L3G4200D_REGISTER_OUT_Z_L = 0x2C
    L3G4200D_REGISTER_OUT_Z_H = 0x2D

    g = [0., 0., 0.]

    def __init__(self, debug=False, hires=False):

        # addresses, so invoke a separate I2C instance for each
        self.bus = smbus.SMBus(1)  # if rev 1, use SMBus(0)

        if self.bus.read_byte_data(self.address,
                self.L3G4200D_REGISTER_WHO_AM_I)&0xFF is not 0xD3:
            print "error"
        # Enable x, y, z and bandwidth 800Hz, cutoff 30Hz and turn off power down
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG1, 0xCF)
        # adjust/use the HPF cutoff 30Hz
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG2, 0x01)
        # No interrupts used on INT1, Data Ready on INT2
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG3, 0x08)
        # full-scale range
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG4, 0x00)
        # output selection 
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG5, 0x02)


    def gyro16(self, high, low):
        n = (high << 8) | low   # High, low bytes
        return n # 2's complement signed

    def read(self):
        # Read the gyroscope
        low = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_X_L)
        high = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_X_H)
        x = self.gyro16(high, low)
        low = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Y_L)
        high = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Y_H)
        y = self.gyro16(high, low)
        low = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Z_L)
        high = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Z_H)
        z = self.gyro16(high, low)
        if x & 0x8000: x -= 65536
        if y & 0x8000: y -= 65536
        if z & 0x8000: z -= 65536

        fs=self.bus.read_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG4)&0x30
        c1=self.bus.read_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG1)

        s = 0.
        if fs == 0x00: s=8.75
        elif fs == 0x10: s=17.5
        elif fs == 0x20: s=70
        elif fs == 0x30: s=70
        self.g[0] = float(x) * s / 1000.
        self.g[1] = float(y) * s / 1000.
        self.g[2] = float(z) * s / 1000.

        return self.g

if __name__ == '__main__':

    l3d4200d = L3G4200D()

    while True:
        data = l3d4200d.read()
        print("read value is %f,\t %f,\t %f" % (data[0], data[1], data[2]))
        time.sleep(1)

    l3d4200d.close()
