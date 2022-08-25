
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('I am listening')
            voice = listener.listen(source)
            order = listener.recognize_google(voice)
            order = order.lower()
            if 'Joan' in order:
                order = order.replace('Joan', '')
                print(order)

    except:
        pass
    return order


def run_Joan():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'bye' in command:
        print('Shutting down')
        talk('Shutting down')
        quit()

    elif 'tell me your name' in command:
        print('I am Joan..i am at your service')
        talk('I am Joan...I am at your service')
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    
    elif 'who' or 'where' in command:
        answer = command.replace('who' or 'where', '')
        fact= wikipedia.summary(answer, 3)
        print(fact)
        talk(fact)

    else:
        print("I can't understand what you are saying, please come again")
        talk("I can't understand what you are saying, please come again")
    
    

while True:
    run_Joan()


