import os
from typing_extensions import final
from AUDIO import speak
from AUDIO import get_audio
from sys import exit

from TEXT_ELEMENT import TR

class change(object):
    def __init__(self, name_of_text_file, ask ,restart = False):
        self.name_of_text_file = name_of_text_file
        self.ask = ask
        self.restart = restart

    def verify(self):
        if os.path.exists(self.name_of_text_file) and os.stat(self.name_of_text_file).st_size != 0:
            f = open(self.name_of_text_file, "rt")
            text = f.read()
            return text
            exit()
        else:
            f = open(self.name_of_text_file, "a")
            speak(self.ask)
            text = get_audio().capitalize()
            f.write(text)
            f.close()
            return text
            exit()

    def change(self):
        if os.path.exists(self.name_of_text_file):
            f = open(self.name_of_text_file, "w")
            speak(self.ask)
            text = get_audio().capitalize()
            f.write(text)
            f.close()
            if self.restart:
                change.restart_assistant_confimation(self, text)

        else:
            change.verify(self)

    def restart_assistant_confimation(self, text):
        speak(f" {TR(12)}")
        answer = get_audio()
        if 'da' in answer or 'yes' in answer:
            os.system("Romana.exe")
            exit()
        else:
            speak(' Am înțeles')