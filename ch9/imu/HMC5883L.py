#!/usr/bin/python
import smbus
import math

class HMC5883L(object):

    # Minimal constants carried over from Arduino library
    HMC5883_ADDRESS   = (0x3C >> 1)  # 0011110x
    address = HMC5883_ADDRESS
                                             # Default    Type
    HMC5883_REGISTER_RA_CONFIG_A   = 0x00    # samples<<5|rate<<2
    HMC5883_REGISTER_RA_CONFIG_B   = 0x01    # gain<<5
    HMC5883_REGISTER_RA_MODE       = 0x02    # mode
    HMC5883_REGISTER_OUT_X_H_M     = 0x03

    HMC5883_SAMPLE_RATE = { 0:0.75, 1:1.5, 2:3, 3:7.5, 4:15, 5:30, 6:75, 7:-1 }
    HMC5883_SAMPLE_MODE = { 0:"continuous", 1:"single", 2:"idle", 3:"idle" }
    HMC5883_MAGGAIN = { 0 : [ 0.88, 1370, 0.73 ],
                        1 : [ 1.30, 1090, 0.92 ],
                        2 : [ 1.90, 820, 1.22 ],
                        3 : [ 2.50, 660, 1.52 ],
                        4 : [ 4.00, 440, 2.27 ],
                        5 : [ 4.70, 390, 2.56 ],
                        6 : [ 5.60, 330, 3.03 ],
                        7 : [ 8.10, 230, 4.35 ] } # gain, gauss, scale

    m = [0., 0., 0.]

    def __init__(self, debug=False):

        # addresses, so invoke a separate I2C instance for each
        self.bus = smbus.SMBus(1)  # if rev 1, use SMBus(0)

        # Enable the magnetometer
        self.bus.write_byte_data(self.address,
            self.HMC5883_REGISTER_RA_CONFIG_A, 0x70) # 8 samples, rate 15Hz
        self.bus.write_byte_data(self.address,
            self.HMC5883_REGISTER_RA_CONFIG_B, 0x20) # 1.3 gain / Gauss 1090
        self.bus.write_byte_data(self.address,
            self.HMC5883_REGISTER_RA_MODE, 0x00)     # continuous

    # Interpret signed 16-bit magnetometer component from list
    def mag16(self, dlist, idx):
        n = (dlist[idx] << 8) | dlist[idx+1]   # High, low bytes
        return n if n < 32768 else n - 65536 # 2's complement signed


    def read(self):
        # Read the magnetometer
        dlist = self.bus.read_i2c_block_data(self.address,
          self.HMC5883_REGISTER_OUT_X_H_M, 6)
        res = [ self.mag16(dlist, 0),
                self.mag16(dlist, 4),
                self.mag16(dlist, 2)]
        self.m[0] = res[0]
        self.m[1] = res[1]
        self.m[2] = res[2]

        return res

    def calcTiltHeading(self, ax, ay, az):
        fNormAcc = math.sqrt(ax*ax + ay*ay + az*az)
        fSinRoll = ay/fNormAcc
        fCosRoll = math.sqrt(1.0-(fSinRoll * fSinRoll))
        fSinPitch = ax/fNormAcc
        fCosPitch = math.sqrt(1.0-(fSinPitch * fSinPitch))

        fTiltedX = self.m[0]*fCosPitch + self.m[2]*fSinPitch
        fTiltedY = self.m[0]*fSinRoll*fSinPitch + self.m[1]*fCosRoll - self.m[2]*fSinRoll*fCosPitch

        fcosf= fTiltedX / math.sqrt(fTiltedX*fTiltedX+fTiltedY*fTiltedY)
        if fTiltedY>0:
          HeadingValue = math.acos(fcosf)*180/math.pi
        else:
          HeadingValue =360-math.acos(fcosf)*180/math.pi

        import geomag
        HeadingValue -= geomag.declination(37,128)
        if HeadingValue>360:
          HeadingValue=HeadingValue-360

        return HeadingValue

# Simple example prints accel/mag data once per second:
if __name__ == '__main__':

    from time import sleep
    import MPU6050

    mpu = MPU6050.MPU6050()
    hmc = HMC5883L()

    print '[(Magnetometer X, Y, Z)]'
    while True:
        print hmc.read()
        data = mpu.read()
        print data
        print hmc.calcTiltHeading(data[0], data[1], data[2])
        sleep(1) # Output is fun to watch if this is commented out
