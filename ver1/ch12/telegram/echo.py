# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pytg.sender import Sender
from pytg.receiver import Receiver
from pytg.utils import coroutine

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
            if msg.text == u'hello':
                sender.send_msg(msg.peer.cmd, u'world')
    except GeneratorExit:
        pass
    else:
        pass

receiver.start()
receiver.message(main_loop())
receiver.stop
