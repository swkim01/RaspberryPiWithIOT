import network
import time

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('<SSID>', '<PASSWORD>')
time.sleep(1)
sta_if.ifconfig()
