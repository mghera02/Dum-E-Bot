import speech_recognition as sr
from espeak import espeak
import time

import lcdText as lcd

recorder = sr.Recognizer()

def listen1():
    with sr.Microphone(device_index = 2) as source:
        recorder.adjust_for_ambient_noise(source)
        print("Listening:...");
        lcd.printToLCD('Listening...')
        try:
            audio = recorder.listen(source,timeout=6, phrase_time_limit=6)
            print("Finished listening");
        except:
            return "none"
    return audio

def voice(audio1):
    print(audio1)
    if(audio1 != "none"):
        try: 
            text1 = recorder.recognize_google(audio1) 
            print ("Received: " + text1);
            return text1; 
        except sr.UnknownValueError: 
            return "Error" 
    else:
        return "Error"

def respond(text):
    response = ''
    action = ''
    text = text.split()

    if("hey" in text and "dummy" in text):
        response = 'Yes?'
        action = ''
    if(("stop" in text and "listening" in text) or ("switch" in text and "modes" in text)):
        response = "Switching modes"
        action = 'switch modes'
    if("turn" in text and "light" in text and "off" in text):
        response = "Turning off the light"
        action = 'turn light off'
    if("turn" in text and "light" in text and "on" in text):
        response = "Turning on the light"
        action = 'turn light on'
    if("sleep" in text):
        response = "Good night"
        action = 'sleep turn light off'
    if("play" in text and "music" in text):
        response = ""
        action = 'play music'
    if(("stop" in text or "pause" in text) and "music" in text):
        response = "stopping the music"
        action = 'stop music'
    if("wake" in text and "up" in text and "home" in text):
        response = "welcome home sir"
        action = 'play music wake up should i stay or should i go'
    elif("wake" in text and "up" in text):
        response = "Hello there"
        action = 'wake up'
    elif("turn" in text and "right" in text):
        response = "Turning right"
        action = 'turn right'
    elif("turn" in text and "left" in text):
        response = "Turning left"
        action = 'turn left'
    elif("go" in text and "up" in text):
        response = "Moving up"
        action = 'move up'
    elif("go" in text and "down" in text):
        response = "Moving down"
        action = 'move down'
    if response:
        espeak.synth(response)
    return response, action

if __name__ == '__main__':
    while(1):
        audio1 = listen1() 
        text = voice(audio1)
