"""
    THIS MODULE IS DESIGNED TO HAVE VOICE INPUT FROM USER
"""
# speech to text conversion regarding imports
import speech_recognition as sr 

# from iovoice.output import speak
from .output import speak

# Initialize the recognizer  
reg = sr.Recognizer()  

def voiceinput(msg=None):
    """
    this function can print an optional msg onto the screen and then 
    allows the user to give input in form of voice
    """
    if msg:
        # if msg is given then speak and write it.
        speak(msg)
    print("listening....")
    # activating mic and recording a segment of speech.
    with sr.Microphone() as source:
        audio = reg.listen(source,phrase_time_limit=3)
    
    text = reg.recognize_google(audio)
    return text.lower()
