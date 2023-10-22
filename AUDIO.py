from READ import language_abreviation as la
from READ import language
import sys
import os
import random

#sys.path.insert(1,"venv/lib/site-packages/gtts")


from gtts import gTTS
import playsound
import speech_recognition as sr


def speak(text):
    r = random.randint(1,10000000)
    tts = gTTS(text=text, lang= f'{la()}')
    audio_file = f"{language()} "+str(r)+".mp3"
    tts.save(audio_file)
    print('\n'+ text)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def get_audio(lg="language 2.txt"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\n ascultă...')
        audio = r.listen(source)
        voice_data=""

        try:
            f = open("name of owner.txt", "rt")
            Name = f.read()
            voice_data = r.recognize_google(audio, language = f"{la(lg)}")
            print(f"\n {Name}: {voice_data}")

        except Exception as e:
            print("\n îmi cer scuze dar nu am înțeles. Vă rog să repetați "+ str(e))

    return voice_data.lower()
