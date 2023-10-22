import os
from gtts import gTTS
import speech_recognition as sr
import playsound
from os import system
import ctypes
from sys import exit

def speak(text):
    
    tts = gTTS(text=text, lang='en')
    audio_file = "voice.mp3"
    tts.save(audio_file)
    print('\n'+ text)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\n listening...')
        audio = r.listen(source)
        voice_data=""

        try:
            try:
                f = open("name of owner.txt","rt")
                Name = f.read()
            except:
                Name="You"
            voice_data = r.recognize_google(audio)
            print(f"\n {Name}: {voice_data}")

        except Exception as e:
            print("\n I am sorry but i could not understand, please say it again "+ str(e))

    return voice_data.lower()

    
if __name__ == "__main__":
    while True:
        if os.path.exists('language.txt') and os.stat("language.txt").st_size != 0:
            f = open("language.txt", "rt")
            Language = f.read()
            os.system("Romana.exe")
            exit()
        else:
            f = open("language.txt", "a")
            speak(' What language would you like to use?')
            Language = get_audio().capitalize()
            f.write(Language)
            f.close()
            os.system("Romana.exe")
            exit()

    