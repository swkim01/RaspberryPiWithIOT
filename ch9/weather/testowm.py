import pyowm
import time

# create client
owm = pyowm.OWM('API Key')

lon = 129.0
lat = 35.0

# iterate results
o1 = owm.weather_at_coords(lat, lon)
loc = o1.get_location()
weat = o1.get_weather()
print("< Current Weather >")
print('location:', str(loc.get_name()))
print('weather:', weat.get_status(), "at", weat.get_reference_time('iso'))
print('temperature:', weat.get_temperature(unit='celsius')['temp'], 'degree')
wc = weat.get_weather_code()
print('weathercode:', wc)
#print(weat.get_weather_icon_name())

if int(wc/100) == 2:
  print('Thunderstorm')
elif int(wc/100) == 3:
  print('Drizzle')
elif int(wc/100) == 5:
  print('Rain')
elif int(wc/100) == 7:
  print('Atmosphere')
elif int(wc/100) == 8:
  print('Clouds')
elif int(wc/100) == 9:
  print('Extreme')

print("")

fc1 = owm.daily_forecast(str(loc.get_name()))
fore = fc1.get_forecast()

print("< Forecast Weather on", time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(fore.get_reception_time())), ">")
#print(time.localtime(fore.get_reception_time()))
for item in fore:
    #print(item.__dict__.values())
    lt = time.localtime(item.get_reference_time())
    print(time.strftime("%a, %d %b %H:%M", lt), item.get_status(), item.get_weather_code())
