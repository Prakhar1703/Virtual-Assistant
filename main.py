import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):

    #engine.say("I am Jarvis")
    #engine.say("My master what I can do for you")
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Hearing.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace("Jarvis", "")
                print(command)


    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if "play" in command():
        song = command.replace("play", "")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")

        talk("Current time is" + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "let us go for" in command:
        talk("Sorry Master")
    elif "are you single" in command:
        talk("I only serve mY Master")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please give the command again')

while True:
    run_jarvis()





