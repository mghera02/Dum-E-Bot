import speech_recognition as sr

r = sr.Recognizer()

def speechToText():
    with sr.Microphone() as source:
        print("talk")
        audio_text = r.listen(source)
    
        try:
            print("Text: " + r.recognize_google(audio_text))
        except:
            print("didnt work")
