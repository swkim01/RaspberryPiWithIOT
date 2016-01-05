import smbus
import os, sys
import datetime

I2C_ADDRESS = 0x51
bus = smbus.SMBus(1)  # if rev 1, use SMBus(0)
 
#Set all ports in input mode
#bus.write_byte(I2C_ADDRESS,0xFF)

#Read all the unput lines
#value=bus.read_byte(I2C_ADDRESS)
#print "%02X" % value

#dt = datetime.datetime.now()
#tm = dt.timetuple()

#data = [tm.tm_sec, tm.tm_min, tm.tm_hour, tm.tm_mday, tm.tm_wday, tm.tm_mon, tm.tm_year]
#bus.write_i2c_block_data(I2C_ADDRESS, 0x02, data)

rdata = bus.read_i2c_block_data(I2C_ADDRESS, 0x02)
print rdata
#os.system("hwclock --set -s %s" % str(dt))
