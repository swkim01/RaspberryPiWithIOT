# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from pytg.receiver import Receiver
from pytg.sender import Sender

import logging
logging.basicConfig()

#receiver = Receiver(host="localhost", port=4458)
sender = Sender(host="localhost", port=4458)
#receiver.start()

#sender.send_msg("username_surname", "Hello")
sender.send_photo("username_surname", "/home/pi/lecture/ch12/telegram/bot/gem1.png")
