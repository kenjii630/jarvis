import pyttsx3
import speech_recognition as sr 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

#speak engine
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait

#conver voice into text
def takeCommandd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print( " listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query2 = r.recognize_google(audio, language = 'en-US')
        print(f"User said: {query2} ") 
    except Exception as e:
        speak("Say that again")
        return "none"
    return query2


if __name__ == "__main__":
    takeCommandd()
    #speak("hello sir")
    # while True:
        