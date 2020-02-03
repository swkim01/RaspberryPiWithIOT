#-*- coding: utf-8 -*-
import math
try:
    from urllib.request import urlopen #python 3
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib2 import urlopen #python 2
    from urllib2 import HTTPError, URLError
from xml.dom import minidom

RE = 6371.00877 # 지구 반경(km)
GRID = 5.0	# 격자 간격(km)
SLAT1 = 30.0	# 투영 위도1(degree)
SLAT2 = 60.0	# 투영 위도2(degree)
OLON = 126.0	# 기준점 경도(degree)
OLAT = 38.0	# 기준점 위도(degree)
XO = 43		# 기준점 X좌표(GRID)
YO = 136	# 기준점 Y좌표(GRID)
DEGRAD = math.pi / 180.0
RADDEG = 180.0 / math.pi
re = RE / GRID
slat1 = SLAT1 * DEGRAD
slat2 = SLAT2 * DEGRAD
olon = OLON * DEGRAD
olat = OLAT * DEGRAD
sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5)
sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
sf = math.pow(sf, sn) * math.cos(slat1) / sn
ro = math.tan(math.pi * 0.25 + olat * 0.5)
ro = re * sf / math.pow(ro, sn)
rs = {}

def dfs_xy2ll(x, y):
    rs['x'] = x
    rs['y'] = y
    xn = x - XO
    yn = ro - y + YO
    ra = math.sqrt(xn * xn + yn * yn)
    if (sn < 0.0): ra = -ra
    alat = math.pow((re * sf / ra), (1.0 / sn))
    alat = 2.0 * math.atan(alat) - math.pi * 0.5
     
    if (math.abs(xn) <= 0.0):
        theta = 0.0;
    else:
        if (math.abs(yn) <= 0.0):
            theta = math.pi * 0.5
            if (xn < 0.0): theta =  -theta
        else:
            theta = math.atan2(xn, yn)

    alon = theta / sn + olon
    rs['lat'] = alat * RADDEG
    rs['lng'] = alon * RADDEG
    return rs

def dfs_ll2xy(lat, lon):
    rs['lat'] = lat
    rs['lng'] = lon
    ra = math.tan(math.pi * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / math.pow(ra, sn)
    theta = lon * DEGRAD - olon
    if (theta > math.pi): theta -= 2.0 * math.pi
    if (theta < -math.pi): theta += 2.0 * math.pi
    theta *= sn
    rs['x'] = int(math.floor(ra * math.sin(theta) + XO + 0.5))
    rs['y'] = int(math.floor(ro - ra * math.cos(theta) + YO + 0.5))
    return rs

def getWeather(lat, lon):
    base_url = "http://www.kma.go.kr/wid/queryDFS.jsp"
    rsd = dfs_ll2xy(lat, lon)
    url = base_url + '?gridx=' + str(rsd['x']) + '&gridy=' + str(rsd['y'])
    u = urlopen(url)
    wdata = []
    try:
        #data = u.readlines()
        data = u.read()
        #print(len(data))
        #print(u.info())
        dom = minidom.parseString(data)
        items = dom.getElementsByTagName("data")
        for item in items:
            hour = item.getElementsByTagName("hour")[0]
            day = item.getElementsByTagName("day")[0]
            wfKor = item.getElementsByTagName("wfKor")[0]
            temp = item.getElementsByTagName("temp")[0]
            wdata.append([ hour.firstChild.data.strip(), \
                  day.firstChild.data.strip(), \
                  wfKor.firstChild.data.strip(), \
                  temp.firstChild.data.strip() ])
    except HTTPError as e:
        print("HTTP error: %d" % e.code)
    except URLError as e:
        print("Network error: %s" % e.reason.args[1])

    return wdata

# 1. 맑음, 2. 구름 조금, 3. 구름 많음, 4. 흐림, 5. 비, 6. 눈/비, 7. 눈
# 1. Clear, 2. Partly Cloudy, 3. Mostly Cloudy, 4. Cloudy, 5. Rain, 6. Snow/Rain, 7. Snow
codes = ['맑음', '구름 조금', '구름 많음', '흐림', '비', '눈/비', '눈']
def getWeatherCode(wfKor):
    for i, code in enumerate(codes):
        if wfKor.encode('utf-8') == code:
            return i + 1

if __name__ == '__main__':
    lat = 35.0
    lon = 129.0
    data = getWeather(lat, lon)
    print(data)
    for d in data:
        print(d[0], d[1], d[2], d[3], getWeatherCode(d[2]))
