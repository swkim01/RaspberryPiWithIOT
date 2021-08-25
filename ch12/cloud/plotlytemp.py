import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import Adafruit_DHT

username = 'your_plotly_username'
api_key = 'your_api_key'
stream_token = 'your_stream_token'
DEBUG = True
sensor = Adafruit_DHT.DHT22
pin = 18

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title="RPi Temperature"
)

fig = Figure(data=[trace1], layout=layout)
print(py.plot(fig, filename="RPi Streaming Example"))

i = 0
stream = py.Stream(stream_token)
stream.open()

def read_temp():
  if DEBUG:
    print("reading temp")
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  return temperature


while True:
    temp = read_temp()
    stream.write({"x": i, "y": temp})
    i += 1
    time.sleep(10)
