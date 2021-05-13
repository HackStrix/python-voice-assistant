import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import sys
import os
import psutil # for cpu usage
from newsapi import NewsApiClient
import time as times



engine = pyttsx3.init()

def speak(audio):
    voices = engine.getProperty("voices")
    # print(voices)
    engine.setProperty('voice',voices[1].id)
    if type(audio) == str:
        engine.say(audio)
        engine.runAndWait()
    else:
        print("Enter Valid String")
def time():
    Time = datetime.datetime.now().strftime("%I:%M") # %I is hour %M minute %S is second
    speak('The current time is '+Time)
def date():
    Date = datetime.datetime.now().strftime("%d %B %Y") # %d is day %B is month in name %Y is year
    speak("Today is " + Date)
def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

def Mic2Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    try:
        print("Processing...")
        query = r.recognize_google(audio,language="en-in")
        print(query)
        return query
    except Exception as e:
        print(e)
        speak("Please repeat")
        return None

# def ListenInBg():
#     r = sr.Recognizer()
#     r.listen_in_background(sr.Microphone(),callback,phrase_time_limit=2)
  
#     try:
#         print("You said " + recognizer.recognize_google(audio,language='en-in'))  # received audio data, now need to recognize it
#     except LookupError:
#         print("Oops! Didn't catch that")


def news():
    newsapi = NewsApiClient(api_key='7ce30be6648348dbaad6e0148c27db59')
    speak('Please specify a topic ')
    topic  = Mic2Text()
    data = newsapi.get_top_headlines(q=topic,language='en',page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("You're now fully updated on the news")

def executecommand():
    query = None
    while True:
        query = Mic2Text()
        if query != None:
            for i in query.split():
                if i.lower() == "exit":
                    sys.exit()
                else:
                    try:
                        globals()[i.lower()]()
                    except:
                        pass
        else:
            pass
def clear():
    os.system('cls')

def cpu():
    usage = str(psutil.cpu_percent())
    speak(usage)
    print(usage)
    

def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(str(battery.percent))
    

executecommand()
