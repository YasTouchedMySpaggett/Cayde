import json
import os
import google.speech as speech #type: ignore
import speech_recognition as sr #type: ignore
import pyttsx3 #type: ignore


r = sr.Recognizer()
r.recognize_sphinx() # works offline
#using this as a guide to do the recognition https://realpython.com/python-speech-recognition/
