import uasyncio as asyncio
from machine import Pin
import time
import dht

led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(4))
state = 0

default = 'index.html'

# Breaks an HTTP request into its parts and boils it down to a physical file (if possible)
def decode_path(req):
    cmd, headers = req.decode("utf-8").split('\r\n', 1)
    parts = cmd.split(' ')
    method, path = parts[0], parts[1]
    # remove any query string
    query = ''
    r = path.find('?')
    if r > 0:
        query = path[r:]
        path = path[:r]
    # check for use of default document
    if path == '/':
        path = default
    else:
        path = path[1:]
    # return the physical path of the response file
    return '/' + path

@asyncio.coroutine
def serve(reader, writer):
    try:
        file = decode_path((yield from reader.read()))
        if file is '/led' or file is '/events':
            yield from writer.awrite("HTTP/1.0 200 OK\r\n")
            yield from writer.awrite("Content-Type: text/plain\r\n")
            yield from writer.awrite("\r\n")

            if file is '/led':
                global led, state
                led.value(state)
                state = (state + 1) % 2
                buffer = 'OK'
                yield from writer.awrite(buffer)
            else:
                global d
                d.measure()
                temp = d.temperature()
                humi = d.humidity()
                buffer = '{\"temperature\": ' + str(temp) + ', \"humidity\": ' + str(humi) + '}'
                yield from writer.awrite(buffer)
        else:
            yield from writer.awrite("HTTP/1.0 404 NA\r\n\r\n")
    except:
        raise
    finally:
        yield from writer.aclose()

def start():
    import logging
    logging.basicConfig(level=logging.ERROR)

    loop = asyncio.get_event_loop()
    loop.call_soon(asyncio.start_server(serve, "0.0.0.0", 80, 20))
    loop.run_forever()
    loop.close()

start()