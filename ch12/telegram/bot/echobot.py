# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import telegram

token = '<token>'

bot = telegram.Bot(token=token)
#print bot.getMe()

#updates = bot.getUpdates()
#print [u.message.text for u in updates]

last_update_id = None

try:
    last_update_id = bot.getUpdates()[-1].update_id
except IndexError:
    last_update_id = None

while True:
    for update in bot.getUpdates(offset=last_update_id, timeout=10):
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')
        if message == u"hello":
            print chat_id
            bot.sendMessage(chat_id=chat_id, text="world")
            last_update_id = update.update_id + 1
