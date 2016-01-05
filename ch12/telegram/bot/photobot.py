# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import telegram

token = '<TOKEN>'

bot = telegram.Bot(token=token)
last_update_id = None

try:
    last_update_id = bot.getUpdates()[-1].update_id
except IndexError:
    last_update_id = None

while True:
    for update in bot.getUpdates(offset=last_update_id, timeout=10):
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')
        print(message)
        if message == b'hello':
            bot.sendPhoto(photo=open("./gem1.png", 'rb'),
                          caption='Invader is Coming!',
                          chat_id=chat_id)
            #bot.sendDocument(document=open("./testbot.py", 'rb'),
            #              chat_id=chat_id)
        last_update_id = update.update_id + 1
