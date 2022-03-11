import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import sys

print("Initializing jarvis")
MASTER = "vea chea"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print("Initializing jarvis...")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)  
    if hour >= 0 and hour < 12 :
        speak("Good morning" + MASTER + "May i help you")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon" + MASTER )
    else:
        speak("Good night" + MASTER )  
    speak("I am your assistant. How can i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query} ") 
    except Exception as e:
        speak("Say that again")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak(results)
        elif 'my academy' in query:
            academic = "C:\\Users\\Asus\\Desktop\\newapp"
            speak("Okay")
            os.system("start " + academic)
        elif 'google classroom' in query:
            speak("Okay")
            webbrowser.open("https://classroom.google.com/h")
        elif 'google calendar' in query.lower():
            speak("Okay")
            webbrowser.open("https://calendar.google.com/calendar/u/0/r")
        elif 'play my favorite song' in query.lower():
            speak("Okay, How your felt rightnow")
            fe = takeCommand().lower()
            if 'i\'m happy' in fe:
                speak("okay")
                webbrowser.open("https://youtu.be/-TXtyYZIiWc")           
            elif 'i\'m not happy' in fe:
                speak("okay")
                webbrowser.open("https://youtu.be/xxecU5M5hdA")  
        elif 'to work' in query.lower():
            speak(MASTER + "Don’t tell people your plans. Show them your results") 
            codePath = "D:\\Microsoft VS Code\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Current Time is" + current_time)
        
        elif 'open google' in query.lower():
            webbrowser.open("https://google.com")
            # chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            # speak("sir, what do you want to search on google")
            # os.startfile(chrome_path)
            # cm = takeCommand().lower()
            # webbrowser.open(f"{ cm }")
        elif 'day' in query.lower():
            today = str(datetime.datetime.now().day)
            speak(" Okay sir today is " + today)
        elif 'open gmail' in query.lower():
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox")
        elif 'open discord' in query.lower():
            webbrowser.open("https://discord.com/channels/@me")
        elif 'shut down please' in query:
            speak("thank")
            sys.exit()
        speak(" sir, do you have any task to assign ")
