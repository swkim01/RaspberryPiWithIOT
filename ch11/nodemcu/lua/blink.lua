led = 2
on = false
gpio.mode(led, gpio.OUTPUT)
tmr.alarm(0, 1000, 1, function()
    if not on then
        gpio.write(led, gpio.HIGH)
    else
        gpio.write(led, gpio.LOW)
    end
    on = not on
end)
