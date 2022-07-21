#Speech to text using notepad Dictation.

from logging.config import listen
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from pynput.keyboard import Controller as key_controller
from pynput.keyboard import Key
import time
import os
import datetime




r=sr.Recognizer()
translator= Translator()
keyboard = key_controller()

#step 1
#speech to text
print("Speak: ")
while True:
    # r=sr.Recognizer()
    with sr.Microphone() as source:
        # print("Speak Now",end=" ")
        audio=r.listen(source)#The phrase_time_limit parameter is the maximum number of seconds that this will allow a phrase to continue before stopping and returning the part of the phrase processed before the time limit was reached. The resulting audio will be the phrase cut off at the time limit. If phrase_timeout is None, there will be no phrase time limit.
        try:
            speech_text=r.recognize_google(audio,language="en")
            if speech_text=="exit" or speech_text=="एग्जिट": #when using translation comment if condition
                print("Dictation Stopped")
                break
            keyboard.type(speech_text)
            time.sleep(0.1)
            keyboard.press(Key.space)
  
            print("missed 1")
        except sr.RequestError:
            print("Could not find the request from google") 
        except sr.UnknownValueError:
            # print("Speech not Recognize1")


            audio=r.listen(source)
            try:
                speech_text=r.recognize_google(audio,language="en")
                if speech_text=="exit" or speech_text=="एग्जिट": #when using translation comment if condition
                    print("Dictation Stopped")
                    break
                keyboard.type(speech_text)
                time.sleep(0.1)

                keyboard.press(Key.space)
                print("22222")
            except sr.UnknownValueError:
                continue
                print("Speech not Recognize2")
                
            except sr.RequestError:
                print("Could not find the request from google")
    








