# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import telegram

token = '<TOKEN>'

bot = telegram.Bot(token=token)

print(bot.getMe())

updates = bot.getUpdates()
print([(u.message.chat_id, u.message.text) for u in updates])

bot.sendMessage(chat_id=<id>, text="Hello World!")
