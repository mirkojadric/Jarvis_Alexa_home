""" Install all pip's to terminal of pycharm,
    follow all input
    find and download PyAudio-0.2.11-cp310-cp310-win_amd64.whl on Google
"""
# pip install SpeechRecognition
# pip install pyaudio
""" pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl-- you need this if you want to use microphone as your source -
download PyAudio-0.2.11-cp310-cp310-win_amd64.whl and place it in to your PycharmProjects file"""
# pip install pywhatkit - you need to install pip3 install pywhatkit
# pip install flask - so PyAudio could run without errors
# pip install gtts --google text to speech
# pip install playsound -- install playsound==1.2.2

import pywhatkit
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random

jarvis_sounds=["./sounds/Ironman_Jarvis_2.mp3",  "./sounds/Jarvis_Confirm_02.mp3", "./sounds/Jarvis_Confirm_male.mp3"]
knock_knock=["Knock, Knock Who’s there? Nobel. Nobel who? Nobel…that’s why I knocked!", "Knock, knock. Who’s there? Figs. Figs who? Figs the doorbell, it’s not working!",
"Knock, knock. Who’s there? A little old lady. A little old lady who? Hey, you can yodel!", "Knock! Knock! Who's there? Scold. Scold who? Scold outside, let me in!"]

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    #playsound(random.choice(jarvis_sounds))
    output.save("./sounds/output.mp3")
    #playsound("./sounds/output.mp3")

def get_audio():
    while True:
        recorder = sr.Recognizer()
        # microphone is our source for recording
        with sr.Microphone() as source:
            audio = recorder.listen(source)


        speech_text = recorder.recognize_google(audio)
        print(speech_text)

        if "Jarvis" in speech_text:
            speech("\tStarting program!")
            playsound("./sounds/Startup_Sound.mp3")
        else:
            break


    return speech_text

text = get_audio()

playsound(random.choice(jarvis_sounds))

if "youtube" in text.lower():
    speech("\tLoading YouTube...")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech(random.choice(knock_knock))
else:
    pywhatkit.search(text)
    speech("\tSearching Google...")