from __future__ import print_function
import datetime
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import webbrowser
import random
import time
from time import ctime
import datetime
import wikipedia
import subprocess
import pytz 
import selenium
from selenium import webdriver
import io
import sys

from SET_LANGUAGE import set_language
from CHANGE import change
from AUDIO import speak
from AUDIO import get_audio
from READ import language
from TEXT_ELEMENT import TR


set_language(f"{language('language.txt')}")
output_language = language()

hour = datetime.datetime.now().hour
last_test_hour = hour - 2
check = 1

WAKE = [f"{TR(1)}",f"{TR(2)}",f"{TR(3)}",f"{TR(4)}",f"{TR(5)}"]
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = [f"{TR(6)}", f"{TR(7)}", f"{TR(8)}", f"{TR(9)}", f"{TR(10)}", f"{TR(11)}", f"{TR(12)}", f"{TR(13)}", f"{TR(14)}", f"{TR(15)}", f"{TR(16)}", f"{TR(17)}"]
DAYS = [f"{TR(18)}", f"{TR(19)}", f"{TR(20)}", f"{TR(21)}", f"{TR(22)}", f"{TR(23)}", f"{TR(24)}"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
THIS_WEEK_EXTENTION = [f"{TR(25)}",f"{TR(26)}",f"{TR(27)}"]
classroom_url = 'https://classroom.google.com/u/1/h'

"""
def authenticate_google():
    
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service
"""
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Close_Second_window():
    os.system("taskkill /f /im geckodriver.exe /T")

def diabetes(last_test_hour):
        CONFIRAMTION = [f"{TR(28)}",f"{TR(29)}",f"{TR(30)}"]
        WAIT = [f"{TR(31)}",f"{TR(32)}",f"{TR(33)}",f"{TR(34)}"]

        last_test_hour = hour

        if last_test_hour >= 24:
            last_test_hour = last_test_hour - 24

        speak(f" {TR(35)}")
        while True:
            text = get_audio()
            repete_count = 1
            digits = 0
            am_luat = 0
            wait = 0
            number = 0

            for phrase in CONFIRAMTION:
                if phrase in text:
                    am_luat = 1
    
            for phrase in WAIT:
                if phrase in text:
                    wait = 1

            for word in text.split():
                if word.isdigit():
                    digits = digits + 1
                    number = int(word)

            if digits == 1 or am_luat == 1 or wait == 1 :
                if am_luat == 1:
                    speak(f" {TR(35)}")
                elif wait == 1:
                    speak(f" {TR(36)}")
                    time.sleep(10)
                    speak(f" {TR(37)}")
                    if f"{TR(38)}" in text:
                        speak(f" {TR(39)}")
                else:
                    if number >= 0 and number < 91:
                        speak(f" {TR(40)}")
                    elif number >= 91 and number < 131:
                        speak(f" {TR(41)}")
                    else:
                        speak(f" {TR(42)}")
                    return last_test_hour

            elif digits == 2:
                speak(f" {TR(43)}")

            elif digits == 0 and repete_count == 1: 
                    repete_count = repete_count + 1
                    speak(f" {TR(44)}")

def get_events(day, service):
    # Call the Calendar API
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        speak(f"{TR(45)}")
    else:
        if len(events) > 1:
            speak(f"{f'{TR(46)}'} {len(events)} {f'{TR(47)}'}")
        else:
            speak(f"{TR(48)}")

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_time = str(start.split("T")[1].split("-")[0])

            if int(start_time.split(":")[0]) < 13:
                start_time = str(int(start_time.split(":")[0])) + ":" + start_time.split(":")[1]
                start_time = start_time + f" {TR(49)}"
            else:
                start_time = str(int(start_time.split(":")[0])-12) + ":" + start_time.split(":")[1]
                start_time = start_time + f" {TR(50)}"

            speak(event["summary"] + f"{TR(51)}" + start_time)

def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count(f"{TR(52)}") or text.count (f"{TR(53)}")> 0:
        return today
    
    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)

    # THE NEW PART STARTS HERE
    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year+1

    # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month
    
    # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count(f"{TR(54)}") or text.count(f"{TR(55)}") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:
        return datetime.date(month=month, day=day, year=year)

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def number_preposition(number):
    if number >= 20:
        return(f"{TR(56)}")
    else:
        return("")

def remove_geckodriver_log():
    try:
        os.remove("geckodriver.log") 
    except:
        pass

def RockPaperScissors():
    OUTCOMES=[f"{TR(57)}",f"{TR(58)}",f"{TR(59)}"]
    while True:
        choise = random.choice(OUTCOMES)
        speak(f"{TR(60)}")
        text = get_audio()
        speak(f"{TR(61)}" + choise)
        speak(f"{TR(62)}")
        text = get_audio()
        if f"{TR(63)}" in text:
            speak(f"{TR(64)}")
            break

def workout():
    EXERCICES = [f" {TR(65)}",f" {TR(66)}",f" {TR(67)}"]
    pushups = 0
    pullups = 0
    abdomens = 0
    speak(f"{TR(68)}")
    time.sleep(1)
    while True:
        number = random.randint(1,30)
        exercices = random.choice(EXERCICES)
        de = number_preposition(number)

        speak(f"{f'{TR(69)}'} {number}{de}{exercices}")
        
        if f"{TR(65)}" in exercices:
            pushups = pushups + number
        if f"{TR(66)}" in exercices:
            abdomens = abdomens + number
        if f"{TR(67)}" in exercices:
            pullups = pullups + number

        speak(f"{TR(70)}")
        while True:
            text = get_audio()
            if f"{TR(71)}" in text:
                break
        speak(f"{TR(72)}")    
        text = get_audio()
        if f"{TR(63)}" in text:
            speak(f"{TR(73)}")
            if pushups != 0:
                de = number_preposition(pushups)
                speak(f"{pushups}{de} {f'{TR(65)}'}")
            if abdomens != 0:
                de = number_preposition(abdomens)
                speak(f"{abdomens}{de} {f'{TR(66)}'}")
            if pullups != 0:
                de = number_preposition(pullups)
                speak(f"{pullups}{de} {f'{TR(67)}'}")
            break

def workout_check(a):
    check = 0
    speak(f"{TR(74)}")
    text = get_audio()
    if not f"{TR(63)}" in text:
        workout()
    else:
        speak(f"{TR(75)}")
    return check

def wishMe():
    if hour >= 4 and hour<11:
        speak(f"\n {TR(76)} {Nume}.")
    elif hour >=11 and hour<18:
        speak(f"\n {TR(77)} {Nume}.")
    else:
        speak(f"\n {TR(78)} {Nume}.")

name = change('name of owner.txt', f" {TR(79)}")
language = change('language.txt', f" {TR(80)}", True)


#SERVICE = authenticate_google()
Nume = name.verify()

remove_geckodriver_log()
clear_terminal()
wishMe()

while True:
    hour = datetime.datetime.now().hour

    if hour >= (last_test_hour + 2):
        remove_geckodriver_log()
        last_test_hour = diabetes(last_test_hour)

    if hour == 18 and check == 1:
       check = workout_check(check)
    if hour == 19: check = 1

    text = get_audio()

    for phrase in WAKE:
        if phrase in text:
            speak(f"{TR(81)}")
            text = get_audio()
            
            SHUT_DOWN = [f"{TR(82)}", f"{TR(83)}",f"{TR(84)}"]
            for phrase in SHUT_DOWN:
                if phrase in text:
                    speak(f"{TR(85)}")
                    text = get_audio() 
                    if f"{TR(63)}" in text or f"{TR(86)}" in text: 
                        speak(f"{TR(87)}")
                    else:
                        if hour >= 4 and hour < 11:
                            speak(f" {TR(88)}\n\n\n")
                            
                        elif hour >= 11 and hour < 18:
                            speak(f"{TR(89)}\n\n\n")   

                        elif hour >= 18 and hour < 22:
                            speak(f"{TR(90)}\n\n\n")

                        else:
                            speak(f"{TR(91)}\n\n\n")
                        
                        os.system("shutdown /s /t 1")

            """
            CALENDAR_STRS = [f"{TR(92)}", f"{TR(93)}", f"{TR(94)}",f"{TR(95)}", f"{TR(96)}"]
            for phrase in CALENDAR_STRS:
                if phrase in text:
                    date = get_date(text)
                    if date:
                        get_events(date, SERVICE)
                    else:
                        speak(f" {TR(97)}")
            """
            
            NOTE_STRS = [f"{TR(98)}", f"{TR(99)}"]
            for phrase in NOTE_STRS:
                if phrase in text:
                    speak(f" {TR(100)}")
                    note_text = get_audio()
                    note(note_text)
                    speak(f" {TR(101)}")

            CLOSE_STRS = [f"{TR(102)}", f"{TR(103)}"]
            for phrase in CLOSE_STRS:
                if phrase in text:

                    if("apex") in text:
                        speak(f"{TR(104)}")
                        os.system("taskkill /f /im r5apex.exe /T")   
                        os.system("taskkill /f /im origin.exe /T")  

            OPEN_STRS = [f"{TR(105)}", f"{TR(106)}"]
            for phrase in OPEN_STRS:
                if phrase in text:

                    if ("apex") in text:
                        speak(f"{TR(107)}")
                        subprocess.Popen(['F:\\Apex\\Apex\\r5apex.exe'])

                    if ("warframe") in text:
                        speak(f"{TR(108)}")
                        subprocess.Popen(['C:\\Users\\acobz\\OneDrive\\Desktop\\Jocuri\\Warframe.url'])

                    if ("classroom") in text:
                        webbrowser.get().open_new_tab(classroom_url)
                        Close_Second_window()
                        
            NAME_STRS = [f"{TR(109)}", f"{TR(110)}", f"{TR(111)}", f"{TR(112)}", f"{TR(113)}", f"{TR(114)}", f"{TR(115)}"]
            for phrase in NAME_STRS:
                if phrase in text:
                    if f"{TR(112)}" in text:
                        name.change()
                    speak(f"{TR(116)}")

            if f"{TR(117)}" in text:
                speak(f" {f'{TR(118)}'} {random.randint(1,10)}")

            if f"{TR(119)}" in text:
                speak(f"{TR(120)}")

            if f"{TR(121)}" in text:
                language.change()

            if f"{TR(122)}" in text:
                RockPaperScissors()

            if f"{TR(123)}" in text:
                speak(f"{TR(124)}")


            if f"{TR(125)}" in text or f"{TR(126)}" in text or f"{TR(127)}" in text:
                speak(f" {f'{TR(128)}'} {name.verify()}")

            if f"{TR(129)}" in text:
                speak(f"{TR(130)}")

            if f"{TR(131)}" in text or f"{TR(132)}" in text or f"{TR(133)}" in text or f"{TR(134)}" in text:
                speak(f"{TR(135)}")

            if f"{TR(136)}" in text or f"{TR(137)}" in text or f"{TR(138)}" in text:
                date = ctime()
                speak(date)
            
            if f"{TR(139)}" in text:
                workout()

            if f"{TR(140)}" in text or f"{TR(141)}" in text or f"{TR(142)}" in text:
                date = ctime()
                speak(date)

            if f"{TR(144)}" in text:
                speak(f"{TR(145)}")
                search = get_audio()
                url = 'https:///www.google.com/search?q=' + search
                webbrowser.get().open_new_tab(url)
                speak(f"{TR(146)}" + search )

            if f"{TR(146)}" in text:
                speak(f"{TR(147)}")
                location = get_audio()
                url = 'https:///www.google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get().open_new_tab(url)
                speak(f"{TR(145)}" + location )
            
            if f"{TR(148)}" in text or f"{TR(149)}" in text or f"{TR(150)}" in text:
                speak(f"{TR(151)}\n\n\n")
                break