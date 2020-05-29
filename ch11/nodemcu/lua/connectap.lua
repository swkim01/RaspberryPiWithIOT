wifi.setmode(wifi.STATION)
wifi.sta.config("<SSID>","<PASSWORD>")
print(wifi.sta.getip())
