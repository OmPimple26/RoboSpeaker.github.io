import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")

print("Welcome to RoboSpeaker 1.1. Created by Om")
while True:
    x = input("Enter what you want to me speak: ")
    if x=="q":
        speak.Speak("Bye bye friend")
        break
    speak.Speak(x)