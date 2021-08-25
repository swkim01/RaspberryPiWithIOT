from bottle import route, run
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pins = [18, 23]
led_states = [0, 0]
btn_pin = 24
GPIO.setup(led_pins[0], GPIO.OUT)
GPIO.setup(led_pins[1], GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def btn_status():
    state = GPIO.input(btn_pin)
    if state:
        return 'Up'
    else:
        return 'Down'
def html_for_led(led):
    l = str(led)
    result = "<input type='button' onClick='changed(" + l + ")' value='LED " + l + "'/>"
    return result
def update_leds():
    for i, value in enumerate(led_states):
        GPIO.output(led_pins[i], value)

@route('/')
@route('/<led>')
def index(led="n"):
    if led != "n":
        led_num = int(led)
        led_states[led_num] = not led_states[led_num]
        update_leds()
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += " window.location.href='/' + led"
    response += "}"
    response += "</script>"
    response += '<h1>GPIO Control</h1>'
    response += '<h2>Button=' + btn_status() + '</h2>'
    response += '<h2>LEDs</h2>'
    response += html_for_led(0)
    response += html_for_led(1)
    return response

run(host='localhost', port=8080)
