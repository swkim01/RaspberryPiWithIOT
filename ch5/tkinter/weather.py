#-*- coding: utf-8 -*-
try:
    from urllib.request import urlopen #python 3
except ImportError:
    from urllib2 import urlopen #python 2
from Tkinter import *

def get_weather(city):
    page = urlopen("http://www.kma.go.kr/weather/observation/currentweather.jsp")
    text = page.read().decode("euckr")
    text = text[text.find(">"+city):]
    for i in range(5):
        text = text[text.find("<td>")+1:]
    start = 3
    end = text.find("</td>")
    tempV.set(u'온도: '+text[start:end])
    print(text[start:end])

def refresh(*args):
    get_weather(cities.get())

app = Tk()
app.title("현재 기온")
app.geometry("200x150+200+200")

Label(app, text="도시: ").pack(side="left")

city_list = ["서울", "부산", "대구", "광주", "제주"]
cities = StringVar()
cities.set(city_list[0])
cities.trace("w", refresh)
OptionMenu(app, cities, *city_list).pack(side="right")

tempV = StringVar()
tempV.set("온도: ")
Label(app, textvariable=tempV).pack(pady=10, side="top")

Button(app, text="Refresh", command=refresh).pack(pady=10, side="bottom")

app.mainloop()
