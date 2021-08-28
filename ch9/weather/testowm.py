import pyowm
import time

# create client
owm = pyowm.OWM('API Key')
mgr = owm.weather_manager()

lat = 35.0
lon = 129.0

# iterate results
o1 = mgr.weather_at_coords(lat, lon)
loc = o1.location
weat = o1.weather
print("< Current Weather >")
print('location:', str(loc.name))
print('weather:', weat.status, "at", weat.reference_time('iso'))
print('temperature:', weat.temperature(unit='celsius')['temp'], 'degree')

wc = weat.weather_code
print('weathercode:', wc)
#print(weat.weather_icon_name)
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

fc1 = mgr.forecast_at_place(str(loc.name), 'daily')
fore = fc1.forecast
print("< Forecast Weather on", time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(fore.reception_time())), ">")
#print(fore.reception_time(str('ico')))
for item in fore:
    #print(item.__dict__.values())
    lt = time.localtime(item.reference_time())
    print(time.strftime("%a, %d %b %H:%M", lt), item.status, item.weather_code)
