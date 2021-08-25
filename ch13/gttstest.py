#-*- coding: utf-8 -*-
from gtts import gTTS
import os, time
from pygame import mixer

tts = gTTS(text='안녕하세요', lang='ko')
tts.save('hello.mp3')
mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
#os.system("mpg123 hello.mp3")
