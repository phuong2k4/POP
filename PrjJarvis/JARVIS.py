import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

jarvis = pyttsx3.init()
voice = jarvis.getProperty('voices')
jarvis.setProperty('voice',voice[1].id)

def speak(audio):
    print("Jarvis: " + audio)
    jarvis.say(audio)
    jarvis.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I : %M : %p")
    speak("The current time is: " + Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good moring sir!")
    elif hour >=12 and hour <=18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("Nice to see u here. How can i help you?")
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio= c.listen(source)
    try:
        query=c.recognize_google(audio, language='en')
        print("User said:" + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command!")
        query=str(input('Your order is: '))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What do u want to know sir?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'This your google search for {search}')
        if "youtube" in query:
            speak("What do u want to know sir?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'This your google search for {search}')
        if"open video" in query:
            meme=r""
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Jarvis is quiting sir. Goodbye sir")
            quit()

#last of update
            