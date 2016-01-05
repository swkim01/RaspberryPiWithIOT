# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import telegram
import pexpect

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
        if message != None:
            child = pexpect.spawn('bash', ['-c', message])
            index = child.expect(pexpect.EOF)
            body = child.before.strip()
            bot.sendMessage(chat_id=chat_id, text=body)
            last_update_id = update.update_id + 1
