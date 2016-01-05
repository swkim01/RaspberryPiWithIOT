#!/usr/bin/python
import smbus
import math

class LSM303DLHC(object):

    # Minimal constants carried over from Arduino library
    LSM303_ADDRESS_ACCEL = (0x32 >> 1)  # 0011001x
    LSM303_ADDRESS_MAG   = (0x3C >> 1)  # 0011110x
    acc = LSM303_ADDRESS_ACCEL
    mag = LSM303_ADDRESS_MAG
                                             # Default    Type
    LSM303_REGISTER_ACCEL_CTRL_REG1_A = 0x20 # 00000111   rw
    LSM303_REGISTER_ACCEL_CTRL_REG4_A = 0x23 # 00000000   rw
    LSM303_REGISTER_ACCEL_OUT_X_L_A   = 0x28
    LSM303_REGISTER_MAG_CRB_REG_M     = 0x01
    LSM303_REGISTER_MAG_MR_REG_M      = 0x02
    LSM303_REGISTER_MAG_OUT_X_H_M     = 0x03

    # Gain settings for setMagGain()
    LSM303_MAGGAIN_1_3 = 0x20 # +/- 1.3
    LSM303_MAGGAIN_1_9 = 0x40 # +/- 1.9
    LSM303_MAGGAIN_2_5 = 0x60 # +/- 2.5
    LSM303_MAGGAIN_4_0 = 0x80 # +/- 4.0
    LSM303_MAGGAIN_4_7 = 0xA0 # +/- 4.7
    LSM303_MAGGAIN_5_6 = 0xC0 # +/- 5.6
    LSM303_MAGGAIN_8_1 = 0xE0 # +/- 8.1

    a = [0., 0., 0.]
    m = [0., 0., 0.]

    def __init__(self, debug=False, hires=False):

        # Accelerometer and magnetometer are at different I2C
        # addresses, so invoke a separate I2C instance for each
        self.bus = smbus.SMBus(1)  # if rev 1, use SMBus(0)

        # Enable the accelerometer
        self.bus.write_byte_data(self.acc,
            self.LSM303_REGISTER_ACCEL_CTRL_REG1_A, 0x27)
        # Select hi-res (12-bit) or low-res (10-bit) output mode.
        # Low-res mode uses less power and sustains a higher update rate,
        # output is padded to compatible 12-bit units.
        if hires:
            self.bus.write_byte_data(self.acc,
                self.LSM303_REGISTER_ACCEL_CTRL_REG4_A, 0b00001000)
        else:
            self.bus.write_byte_data(self.acc,
                self.LSM303_REGISTER_ACCEL_CTRL_REG4_A, 0)
  
        # Enable the magnetometer
        self.bus.write_byte_data(self.mag,
            self.LSM303_REGISTER_MAG_CRB_REG_M, 0xa0)
        self.bus.write_byte_data(self.mag,
            self.LSM303_REGISTER_MAG_MR_REG_M, 0x00)

    # Interpret signed 12-bit acceleration component from list
    def accel12(self, dlist, idx):
        n = dlist[idx] | (dlist[idx+1] << 8) # Low, high bytes
        if n > 32767: n -= 65536           # 2's complement signed
        return n >> 4                      # 12-bit resolution


    # Interpret signed 16-bit magnetometer component from list
    def mag16(self, dlist, idx):
        n = (dlist[idx] << 8) | dlist[idx+1]   # High, low bytes
        return n if n < 32768 else n - 65536 # 2's complement signed


    def read(self):
        # Read the accelerometer
        dlist = self.bus.read_i2c_block_data(self.acc,
          self.LSM303_REGISTER_ACCEL_OUT_X_L_A | 0x80, 6)
        res = [self.accel12(dlist, 0),
                self.accel12(dlist, 2),
                self.accel12(dlist, 4)]
        self.a[0] = res[0]
        self.a[1] = res[1]
        self.a[2] = res[2]

        # Read the magnetometer
        dlist = self.bus.read_i2c_block_data(self.mag,
          self.LSM303_REGISTER_MAG_OUT_X_H_M, 6)
        res.append(self.mag16(dlist, 0))
        res.append(self.mag16(dlist, 4))
        res.append(self.mag16(dlist, 2))
        self.m[0] = res[3]
        self.m[1] = res[4]
        self.m[2] = res[5]

        return res

    def setMagGain(gain=LSM303_MAGGAIN_1_3):
        self.bus.write_byte_data(self.mag,
            LSM303_REGISTER_MAG_CRB_REG_M, gain)

    def calcTiltHeading(self):
        fNormAcc = math.sqrt(sum(i*i for i in self.a))
        fSinRoll = self.a[1]/fNormAcc
        fCosRoll = math.sqrt(1.0-(fSinRoll * fSinRoll))
        fSinPitch = self.a[0]/fNormAcc
        fCosPitch = math.sqrt(1.0-(fSinPitch * fSinPitch))

        fTiltedX = self.m[0]*fCosPitch + self.m[2]*fSinPitch
        fTiltedY = self.m[0]*fSinRoll*fSinPitch + self.m[1]*fCosRoll - self.m[2]*fSinRoll*fCosPitch

        fcosf= fTiltedX / math.sqrt(fTiltedX*fTiltedX+fTiltedY*fTiltedY)
        if fTiltedY>0:
          HeadingValue = math.acos(fcosf)*180/math.pi
        else:
          HeadingValue =360-math.acos(fcosf)*180/math.pi

        import geomag
        #HeadingValue -= -8
        HeadingValue -= geomag.declination(37,128)
        if HeadingValue>360:
          HeadingValue=HeadingValue-360

        return HeadingValue

# Simple example prints accel/mag data once per second:
if __name__ == '__main__':

    from time import sleep

    lsm = LSM303DLHC()

    print '[(Accelerometer X, Y, Z), (Magnetometer X, Y, Z, orientation)]'
    while True:
        print lsm.read()
        print lsm.calcTiltHeading()
        sleep(1) # Output is fun to watch if this is commented out
