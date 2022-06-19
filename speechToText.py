import speech_recognition as sr
from espeak import espeak
import time

recorder = sr.Recognizer()

def listen1():
    with sr.Microphone(device_index = 2) as source:
               recorder.adjust_for_ambient_noise(source)
               print("Listening:...");
               audio = recorder.listen(source,timeout=6, phrase_time_limit=6)
               print("Finished listening");
    return audio

def voice(audio1):
    try: 
        text1 = recorder.recognize_google(audio1) 
        print ("Received: " + text1);
        return text1; 
    except sr.UnknownValueError: 
        return "Error" 

def respond(text):
    if(text == "hey dummy"):
        espeak.synth("Yes?")
    return 1,1

if __name__ == '__main__':
    while(1):
        audio1 = listen1() 
        text = voice(audio1)
