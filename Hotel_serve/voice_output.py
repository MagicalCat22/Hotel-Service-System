import win32com.client as win

speak = win.Dispatch("SAPI.SpVoice")

def speak_sentence(str):
    speak.Speak(str) 
