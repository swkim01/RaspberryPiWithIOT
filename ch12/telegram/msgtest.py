# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pytg.sender import Sender

sender = Sender(host="localhost", port=4458)
sender.send_msg("username_surname", "Hello World!")

