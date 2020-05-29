import time
import ttn

app_id = 'ttn_app_2'
dev_id = 'ttgo_dev_1'
access_key = 'ttn-account-v2.dJwCIEucyd2Qyk3AgVkt8fDsbt0jpGdpQnV9MxwaSAg'

def uplink_callback(msg, client):
    print("\nReceived uplink from ", msg.dev_id)
    print(msg.payload_fields)

def downlink_callback(mid, client):
    print("Send ", mid, " to downlink")

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
while True:
    value = input("Input command(0:LED Off, 1:LED On, others:Quit)? ") 
    if value == '0':
        ledstate = False
    elif value == '1':
        ledstate = True
    else:
        break
    mqtt_client.send(dev_id, {"led": ledstate})
mqtt_client.close()

# using application manager client
#app_client =  handler.application()
#my_app = app_client.get()
#print(my_app)
#my_devices = app_client.devices()
#print(my_devices)

#asia-se.thethings.network -t 'ttn_app_2/devices/ttgo_dev_1/down' -u '
#-m '{"payload_fields":{"led":true}}'

