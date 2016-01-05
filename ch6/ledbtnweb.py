from bottle import route, run, template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pins = [26, 12]
led_states = [0, 0]
btn_pin = 5
GPIO.setup(led_pins[0], GPIO.OUT)
GPIO.setup(led_pins[1], GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def update_leds():
    for i, value in enumerate(led_states):
        GPIO.output(led_pins[i], value)

control_page = """
<script>
function changed(led)
{
 window.location.href='/' + led
}
</script>
<h1>GPIO Control</h1>
<h2>Button
% if btnState:
  =Up
% else:
  =Down
% end
</h2>
<h2>LEDs</h2>
<input type='button' onClick='changed({{led0}})' value='LED{{led0}}'/>
<input type='button' onClick='changed({{led1}})' value='LED{{led1}}'/>
"""

@route('/')
@route('/<led>')
def index(led="n"):
    if led != "n" and led != "favicon.ico":
        num = int(led)
        led_states[num] = not led_states[num]
        update_leds()
    state = GPIO.input(btn_pin)
    return template(control_page, btnState=state, led0=0, led1=1)

run(host='localhost', port=8080)
