#!/usr/bin/env python
import time
import smbus
import math

class MPU6050(object) :

    # Registers/etc.
    MPU6050_ADDRESS = 0x68
    address = MPU6050_ADDRESS

    MPU6050_RA_XG_OFFS_TC= 0x00       # [7] PWR_MODE, [6:1] XG_OFFS_TC, [0] OTP_BNK_VLD
    MPU6050_RA_YG_OFFS_TC= 0x01       # [7] PWR_MODE, [6:1] YG_OFFS_TC, [0] OTP_BNK_VLD
    MPU6050_RA_ZG_OFFS_TC= 0x02       # [7] PWR_MODE, [6:1] ZG_OFFS_TC, [0] OTP_BNK_VLD
    MPU6050_RA_X_FINE_GAIN= 0x03      # [7:0] X_FINE_GAIN
    MPU6050_RA_Y_FINE_GAIN= 0x04      # [7:0] Y_FINE_GAIN
    MPU6050_RA_Z_FINE_GAIN= 0x05      # [7:0] Z_FINE_GAIN
    MPU6050_RA_XA_OFFS_H= 0x06    # [15:0] XA_OFFS
    MPU6050_RA_XA_OFFS_L_TC= 0x07
    MPU6050_RA_YA_OFFS_H= 0x08    # [15:0] YA_OFFS
    MPU6050_RA_YA_OFFS_L_TC= 0x09
    MPU6050_RA_ZA_OFFS_H= 0x0A    # [15:0] ZA_OFFS
    MPU6050_RA_ZA_OFFS_L_TC= 0x0B
    MPU6050_RA_XG_OFFS_USRH= 0x13     # [15:0] XG_OFFS_USR
    MPU6050_RA_XG_OFFS_USRL= 0x14
    MPU6050_RA_YG_OFFS_USRH= 0x15     # [15:0] YG_OFFS_USR
    MPU6050_RA_YG_OFFS_USRL= 0x16
    MPU6050_RA_ZG_OFFS_USRH= 0x17     # [15:0] ZG_OFFS_USR
    MPU6050_RA_ZG_OFFS_USRL= 0x18
    MPU6050_RA_SMPLRT_DIV= 0x19
    MPU6050_RA_CONFIG= 0x1A
    MPU6050_RA_GYRO_CONFIG= 0x1B
    MPU6050_RA_ACCEL_CONFIG= 0x1C
    MPU6050_RA_FF_THR= 0x1D
    MPU6050_RA_FF_DUR= 0x1E
    MPU6050_RA_MOT_THR= 0x1F
    MPU6050_RA_MOT_DUR= 0x20
    MPU6050_RA_ZRMOT_THR= 0x21
    MPU6050_RA_ZRMOT_DUR= 0x22
    MPU6050_RA_FIFO_EN= 0x23
    MPU6050_RA_I2C_MST_CTRL= 0x24
    MPU6050_RA_I2C_SLV0_ADDR= 0x25
    MPU6050_RA_I2C_SLV0_REG= 0x26
    MPU6050_RA_I2C_SLV0_CTRL= 0x27
    MPU6050_RA_I2C_SLV1_ADDR= 0x28
    MPU6050_RA_I2C_SLV1_REG= 0x29
    MPU6050_RA_I2C_SLV1_CTRL= 0x2A
    MPU6050_RA_I2C_SLV2_ADDR= 0x2B
    MPU6050_RA_I2C_SLV2_REG= 0x2C
    MPU6050_RA_I2C_SLV2_CTRL= 0x2D
    MPU6050_RA_I2C_SLV3_ADDR= 0x2E
    MPU6050_RA_I2C_SLV3_REG= 0x2F
    MPU6050_RA_I2C_SLV3_CTRL= 0x30
    MPU6050_RA_I2C_SLV4_ADDR= 0x31
    MPU6050_RA_I2C_SLV4_REG= 0x32
    MPU6050_RA_I2C_SLV4_DO= 0x33
    MPU6050_RA_I2C_SLV4_CTRL= 0x34
    MPU6050_RA_I2C_SLV4_DI= 0x35
    MPU6050_RA_I2C_MST_STATUS= 0x36
    MPU6050_RA_INT_PIN_CFG= 0x37
    MPU6050_RA_INT_ENABLE= 0x38
    MPU6050_RA_DMP_INT_STATUS= 0x39
    MPU6050_RA_INT_STATUS= 0x3A
    MPU6050_RA_ACCEL_XOUT_H= 0x3B
    MPU6050_RA_ACCEL_XOUT_L= 0x3C
    MPU6050_RA_ACCEL_YOUT_H= 0x3D
    MPU6050_RA_ACCEL_YOUT_L= 0x3E
    MPU6050_RA_ACCEL_ZOUT_H= 0x3F
    MPU6050_RA_ACCEL_ZOUT_L= 0x40
    MPU6050_RA_TEMP_OUT_H= 0x41
    MPU6050_RA_TEMP_OUT_L= 0x42
    MPU6050_RA_GYRO_XOUT_H= 0x43
    MPU6050_RA_GYRO_XOUT_L= 0x44
    MPU6050_RA_GYRO_YOUT_H= 0x45
    MPU6050_RA_GYRO_YOUT_L= 0x46
    MPU6050_RA_GYRO_ZOUT_H= 0x47
    MPU6050_RA_GYRO_ZOUT_L= 0x48
    MPU6050_RA_EXT_SENS_DATA_00= 0x49
    MPU6050_RA_EXT_SENS_DATA_01= 0x4A
    MPU6050_RA_EXT_SENS_DATA_02= 0x4B
    MPU6050_RA_EXT_SENS_DATA_03= 0x4C
    MPU6050_RA_EXT_SENS_DATA_04= 0x4D
    MPU6050_RA_EXT_SENS_DATA_05= 0x4E
    MPU6050_RA_EXT_SENS_DATA_06= 0x4F
    MPU6050_RA_EXT_SENS_DATA_07= 0x50
    MPU6050_RA_EXT_SENS_DATA_08= 0x51
    MPU6050_RA_EXT_SENS_DATA_09= 0x52
    MPU6050_RA_EXT_SENS_DATA_10= 0x53
    MPU6050_RA_EXT_SENS_DATA_11= 0x54
    MPU6050_RA_EXT_SENS_DATA_12= 0x55
    MPU6050_RA_EXT_SENS_DATA_13= 0x56
    MPU6050_RA_EXT_SENS_DATA_14= 0x57
    MPU6050_RA_EXT_SENS_DATA_15= 0x58
    MPU6050_RA_EXT_SENS_DATA_16= 0x59
    MPU6050_RA_EXT_SENS_DATA_17= 0x5A
    MPU6050_RA_EXT_SENS_DATA_18= 0x5B
    MPU6050_RA_EXT_SENS_DATA_19= 0x5C
    MPU6050_RA_EXT_SENS_DATA_20= 0x5D
    MPU6050_RA_EXT_SENS_DATA_21= 0x5E
    MPU6050_RA_EXT_SENS_DATA_22= 0x5F
    MPU6050_RA_EXT_SENS_DATA_23= 0x60
    MPU6050_RA_MOT_DETECT_STATUS= 0x61
    MPU6050_RA_I2C_SLV0_DO= 0x63
    MPU6050_RA_I2C_SLV1_DO= 0x64
    MPU6050_RA_I2C_SLV2_DO= 0x65
    MPU6050_RA_I2C_SLV3_DO= 0x66
    MPU6050_RA_I2C_MST_DELAY_CTRL= 0x67
    MPU6050_RA_SIGNAL_PATH_RESET= 0x68
    MPU6050_RA_MOT_DETECT_CTRL= 0x69
    MPU6050_RA_USER_CTRL= 0x6A
    MPU6050_RA_PWR_MGMT_1= 0x6B
    MPU6050_RA_PWR_MGMT_2= 0x6C
    MPU6050_RA_BANK_SEL= 0x6D
    MPU6050_RA_MEM_START_ADDR= 0x6E
    MPU6050_RA_MEM_R_W= 0x6F
    MPU6050_RA_DMP_CFG_1= 0x70
    MPU6050_RA_DMP_CFG_2= 0x71
    MPU6050_RA_FIFO_COUNTH= 0x72
    MPU6050_RA_FIFO_COUNTL= 0x73
    MPU6050_RA_FIFO_R_W= 0x74
    MPU6050_RA_WHO_AM_I= 0x75

    CALIBRATION_ITERATIONS = 100

    ax_offset = 0
    ay_offset = 0
    az_offset = 0
    gx_offset = 0
    gy_offset = 0
    gz_offset = 0
    result_array = [0., 0., 0., 0., 0., 0., 0.]

    def __init__(self, debug=False):

        # addresses, so invoke a separate I2C instance for each
        self.bus = smbus.SMBus(1)  # if rev 1, use SMBus(0)

        #---------------------------------------------------------------
        # Reset all registers
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_CONFIG, 0x80)
        time.sleep(0.5)
    
        #---------------------------------------------------------------
        # ********************: Experimental :**************************
        # Sets sample rate to 1000/1+4 = 200Hz
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_SMPLRT_DIV, 0x04)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Sets clock source to gyro reference w/ PLL
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_PWR_MGMT_1, 0x02)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Controls frequency of wakeups in accel low power mode plus the sensor standby modes
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_PWR_MGMT_2, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # ********************: Experimental :**************************
        # Disable gyro self tests, scale of +/- 500 degrees/s
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_GYRO_CONFIG, 0x08)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # ********************: Experimental :**************************
        # Disable accel self tests, scale of +/-2g
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_ACCEL_CONFIG, 0x00)
        time.sleep(0.005)

        #---------------------------------------------------------------
        # Setup INT pin to latch and AUX I2C bypass for HMC5883L sensor
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_INT_PIN_CFG, 0x22)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # ********************: Experimental :**************************
        # Enable data ready interrupt
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_INT_ENABLE, 0x01)
        time.sleep(0.005)

        #---------------------------------------------------------------
        # ********************: Experimental :**************************
        # Disable FSync, 5Hz DLPF => 1kHz sample frequency used above divided by the
        # sample divide factor.
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_CONFIG, 0x06)   # 0x05 => 10Hz DLPF
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Freefall threshold of |0mg|
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_FF_THR, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Freefall duration limit of 0
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_FF_DUR, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Motion threshold of 0mg
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_MOT_THR, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Motion duration of 0s
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_MOT_DUR, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Zero motion threshold
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_ZRMOT_THR, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Zero motion duration threshold
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_ZRMOT_DUR, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Disable sensor output to FIFO buffer
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_FIFO_EN, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # AUX I2C setup
        # Sets AUX I2C to single master control, plus other config
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_MST_CTRL, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Setup AUX I2C slaves
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV0_ADDR, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV0_REG, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV0_CTRL, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV1_ADDR, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV1_REG, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV1_CTRL, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV2_ADDR, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV2_REG, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV2_CTRL, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV3_ADDR, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV3_REG, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV3_CTRL, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV4_ADDR, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV4_REG, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV4_DO, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV4_CTRL, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV4_DI, 0x00)
    
        #---------------------------------------------------------------
        # Slave out, dont care
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV0_DO, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV1_DO, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV2_DO, 0x00)
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_SLV3_DO, 0x00)
    
        #---------------------------------------------------------------
        # More slave config
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_I2C_MST_DELAY_CTRL, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Reset sensor signal paths
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_SIGNAL_PATH_RESET, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Motion detection control
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_MOT_DETECT_CTRL, 0x00)
        time.sleep(0.005)
    
        #--------------------------------------------------------------
        # Disables FIFO, AUX I2C, FIFO and I2C reset bits to 0
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_USER_CTRL, 0x00)
        time.sleep(0.005)
    
        #---------------------------------------------------------------
        # Data transfer to and from the FIFO buffer
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_FIFO_R_W, 0x00)
        time.sleep(0.005)

    def readSensorsRaw(self):
        #---------------------------------------------------------------
        # Clear the interrupt by reading the interrupt status register,
        #---------------------------------------------------------------
        self.bus.read_byte_data(self.address, self.MPU6050_RA_INT_STATUS)

        #---------------------------------------------------------------
        # Hard loop on the data ready interrupt until it gets set high
        #---------------------------------------------------------------
        while not (self.bus.read_byte_data(self.address, self.MPU6050_RA_INT_STATUS) == 0x01):
            time.sleep(0.001)
            continue

        #---------------------------------------------------------------
        # Disable the interrupt while we read the data
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_INT_ENABLE, 0x00)

        #---------------------------------------------------------------
        # For speed of reading, read all the sensors and parse to USHORTs after
        #---------------------------------------------------------------
        sensor_data = self.bus.read_i2c_block_data(self.address,
                         self.MPU6050_RA_ACCEL_XOUT_H, 14)

        for index in range(0, 14, 2):
            if (sensor_data[index] > 127):
                sensor_data[index] -= 256
            self.result_array[int(index / 2)] = (sensor_data[index] << 8) + sensor_data[index + 1]

        #---------------------------------------------------------------
        # Reenable the interrupt
        #---------------------------------------------------------------
        self.bus.write_byte_data(self.address,
                        self.MPU6050_RA_INT_ENABLE, 0x01)

        return self.result_array


    def read(self):
        #---------------------------------------------------------------
        # +/- 2g 2 * 16 bit range for the accelerometer
        # +/- 500 degrees * 16 bit range for the gyroscope
        #---------------------------------------------------------------
        [ax, ay, az, temp, gx, gy, gz] = self.readSensorsRaw()
        fax = float(ax * self.CALIBRATION_ITERATIONS - self.ax_offset) * 4.0 / float(65536 * self.CALIBRATION_ITERATIONS)
        fay = float(ay * self.CALIBRATION_ITERATIONS - self.ay_offset) * 4.0 / float(65536 * self.CALIBRATION_ITERATIONS)
        faz = float(az * self.CALIBRATION_ITERATIONS - self.az_offset) * 4.0 / float(65536 * self.CALIBRATION_ITERATIONS)
        fgx = float(gx * self.CALIBRATION_ITERATIONS - self.gx_offset) * 1000.0 / float(65536 * self.CALIBRATION_ITERATIONS)
        fgy = float(gy * self.CALIBRATION_ITERATIONS - self.gy_offset) * 1000.0 / float(65536 * self.CALIBRATION_ITERATIONS)
        fgz = float(gz * self.CALIBRATION_ITERATIONS - self.gz_offset) * 1000.0 / float(65536 * self.CALIBRATION_ITERATIONS)
        return [fax, fay, faz, fgx, fgy, fgz]
    
    def updateOffsets(self, file_name):
        ax_offset = 0
        ay_offset = 0
        az_offset = 0
        gx_offset = 0
        gy_offset = 0
        gz_offset = 0

        for loop_count in range(0, self.CALIBRATION_ITERATIONS):
            [ax, ay, az, temp, gx, gy, gz] = self.readSensorsRaw()
            ax_offset += ax
            ay_offset += ay
            az_offset += az
            gx_offset += gx
            gy_offset += gy
            gz_offset += gz

            time.sleep(0.05)

        self.ax_offset = ax_offset
        self.ay_offset = ay_offset
        self.az_offset = az_offset
        self.gx_offset = gx_offset
        self.gy_offset = gy_offset
        self.gz_offset = gz_offset

        #---------------------------------------------------------------
        # Open the offset config file
        #---------------------------------------------------------------
        cfg_rc = True
        try:
            with open(file_name, 'w+') as cfg_file:
                cfg_file.write('%d\n' % ax_offset)
                cfg_file.write('%d\n' % ay_offset)
                cfg_file.write('%d\n' % az_offset)
                cfg_file.write('%d\n' % gx_offset)
                cfg_file.write('%d\n' % gy_offset)
                cfg_file.write('%d\n' % gz_offset)
                cfg_file.flush()

        except IOError, err:
            print 'Could not open offset config file: %s for writing'.format(file_name)
            cfg_rc = False

        return cfg_rc


    def readOffsets(self, file_name):
        #---------------------------------------------------------------
        # Open the Offsets config file, and read the contents
        #---------------------------------------------------------------
        cfg_rc = True
        try:
            with open(file_name, 'r') as cfg_file:
                str_ax_offset = cfg_file.readline()
                str_ay_offset = cfg_file.readline()
                str_az_offset = cfg_file.readline()
                str_gx_offset = cfg_file.readline()
                str_gy_offset = cfg_file.readline()
                str_gz_offset = cfg_file.readline()

            self.ax_offset = int(str_ax_offset)
            self.ay_offset = int(str_ay_offset)
            self.az_offset = int(str_az_offset)
            self.gx_offset = int(str_gx_offset)
            self.gy_offset = int(str_gy_offset)
            self.gz_offset = int(str_gz_offset)

        except IOError, err:
            print 'Could not open offset config file: %s for reading'.format(file_name)
            cfg_rc = False

        return cfg_rc

    def getEulerAngles(self, fax, fay, faz):
        #---------------------------------------------------------------
        # What's the angle in the x and y plane from horizonal?
        #---------------------------------------------------------------
        theta = math.atan2(fax, math.pow(math.pow(fay, 2) + math.pow(faz, 2), 0.5))
        psi = math.atan2(fay, math.pow(math.pow(fax, 2) + math.pow(faz, 2), 0.5))
        phi = math.atan2(math.pow(math.pow(fax, 2) + math.pow(fay, 2), 0.5), faz)

        theta *=  (180 / math.pi)
        psi *=  (180 / math.pi)
        phi *=  (180 / math.pi)

        return theta, psi, phi

    def readTemp(self):
        hibyte = self.bus.read_byte_data(self.address,
                       self.MPU6050_RA_TEMP_OUT_H)
        if (hibyte > 127):
            hibyte -= 256
        lowbyte = self.bus.read_byte_data(self.address,
                       self.MPU6050_RA_TEMP_OUT_L)
        temp = (hibyte << 8) + lowbyte
        temp = (float(temp) / 340) + 36.53
        return temp

# Simple example prints accel/mag data once per second:
if __name__ == '__main__':

    from time import sleep

    mpu = MPU6050()

    print '[(Accelerometer X, Y, Z), Temperature, (Gyroscope X, Y, Z)]'
    while True:
        print mpu.read()
        time.sleep(1)
