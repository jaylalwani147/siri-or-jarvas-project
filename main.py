from calendar import c
import speech_recognition as sr
import pyttsx3
import webbrowser
#import musiclib



recognizer = sr.Recognizer()
engine = pyttsx3.init()
  
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if"open google" in c.lower():
        webbrowser.open("https://google.com")  
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"sorry song" in c.lower():
        webbrowser.open("https://youtu.be/fRh_vgS2dFE?si=vSWFhwHp0mYpuorn")    
    elif"play friend song" in c.lower():
        webbrowser.open("https://youtu.be/jzD_yyEcp0M?si=t36MNQUBeKkJqZsk")    
    elif"play " in c.lower():
        webbrowser.open("https://youtu.be/ou0phHbzz-0?si=y5PHM4hv340NH1q7") 
    
if __name__ == "__main__": 
    speak( "siri")
    while True :
        r = sr.Recognizer()
        print("recognizing...")
    # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=4, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "siri"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("siri Active...")
                    audio = r.listen(source , timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processcommand(command)
        except Exception as e:
            print("error; {0}".format(e)) 