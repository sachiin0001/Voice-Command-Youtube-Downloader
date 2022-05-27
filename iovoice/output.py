"""
THIS MODULE IS DESIGNED TO SPEAK THE GIVEN STRING.
"""
# importing the dependencies for pyttsx
import pyttsx3

# created the engine for text to speech conversion.
engine = pyttsx3.init()

# slow-down the speaking speed
engine.setProperty('rate',135)

# changing the voice
voices = engine.getProperty('voices')
# print(voice)
engine.setProperty('voice', voices[1].id)

def speak(msg,/):
    """
    accepts a msg and speaks that msg out.
    """
    print(msg)
    engine.say(msg)
    engine.runAndWait()

