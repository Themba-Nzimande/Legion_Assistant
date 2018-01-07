from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    #os.system('mpg123 audio.mp3')
    webbrowser.open("audio.mp3")

#Listens for commands
def MyCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Waiting for command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(command)

    #loop back to listening for commands if speech isnt recognized

    except sr.UnknownValueError:
        assistant(MyCommand())

    return command

#Actual commands
def assistant(command):

    if 'Legion open 9GAG' in command:
        chrome_path = 'c:\\program files\\internet explorer\\iexplore.exe'
        url = "https://www.9gag.com"
        #print(webbrowser._browsers)
        webbrowser.get(chrome_path).open(url)

    if 'Legion close 9GAG' in command:
        os.system('TASKKILL /F /IM iexplore.exe')

    if 'Legion open reddit' in command:
        chrome_path = 'c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s'
        url = "https://www.reddit.com/"
        #print(webbrowser._browsers)
        webbrowser.get(chrome_path).open(url)

    if 'Legion close reddit' in command:
        os.system("TASKKILL /F /IM chrome.exe")

    if 'Legion details' in command:
        talkToMe('I am Legion version one with basic prototype of voice command framework')

talkToMe('Waiting for command')
while True:
    assistant(MyCommand())
