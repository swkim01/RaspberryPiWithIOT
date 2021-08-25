#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=2, sample_rate=44100) as source:
#with sr.Microphone(device_index=2) as source:
    print("Say something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio, language = "ko-KR"))
    #print("You said: " + r.recognize_google_cloud(audio, language = "ko-KR"))
    #print("You said: " + r.recognize_google_cloud(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
