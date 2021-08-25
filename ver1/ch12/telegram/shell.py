# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from pytg import Telegram
#tg = Telegram(telegram="/home/pi/lecture/ch10/telegram/tg/bin/telegram-cli",
#            pubkey_file="/home/pi/lecture/ch10/telegram/tg/tg-server.pub")
#receiver = tg.receiver
#sender = tg.sender
from pytg.sender import Sender
from pytg.receiver import Receiver
from pytg.utils import coroutine
import pexpect

receiver = Receiver(host="localhost", port=4458)
sender = Sender(host="localhost", port=4458)

@coroutine
def main_loop():
    QUIT = False
    try:
        while not QUIT:
            msg = (yield)
            sender.status_online()
            if msg.event != "message" or msg.own:
                continue
            print "Message: ", msg.text
            if msg.text != None:
                child = pexpect.spawn('bash', ['-c', msg.text])
                index = child.expect(pexpect.EOF)
                body = child.before.strip()
                sender.send_msg(msg.peer.cmd, body.decode('utf-8'))
    except GeneratorExit:
        pass
    else:
        pass

receiver.start()
receiver.message(main_loop())
receiver.stop()
