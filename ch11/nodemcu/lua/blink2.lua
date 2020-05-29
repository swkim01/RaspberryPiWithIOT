led = 0
gpio.mode(led, gpio.OUTPUT)
while 1 do
  gpio.write(pin, gpio.HIGH)
  tmr.delay(1000000)   -- wait 1,000,000 us = 1 second
  gpio.write(pin, gpio.LOW)
  tmr.delay(1000000)   -- wait 1,000,000 us = 1 second
end
