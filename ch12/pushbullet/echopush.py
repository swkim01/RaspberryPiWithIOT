from pushbullet import PushBullet
from pushbullet import Listener

api_key = "<API KEY>"
HTTP_PROXY_HOST = None
HTTP_PROXY_PORT = None
phone = None

def on_push(data):
    pushes = pb.get_pushes()
    latest = pushes[1][0]
    print latest
    if latest.get('source_device_iden') == phone.device_iden:
        print 'Got a message.'
        body = latest.get('body')
        if 'hello' in body:
            push = pb.push_note('raspberrypi', "world", device=phone)

if __name__ == "__main__":
    pb = PushBullet(api_key)
    print pb.devices
    phone = pb.devices[0]
    s = Listener(account=pb, on_push=on_push,
                 http_proxy_host=HTTP_PROXY_HOST,
                 http_proxy_port=HTTP_PROXY_PORT)
    try:
        s.run_forever()
    except KeyboardInterrupt:
        s.close()
