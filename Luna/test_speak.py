import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print("Available voices:", [v.name for v in voices])  # see what’s available
engine.setProperty('voice', voices[1].id)  
engine.say("Test, one, two, three")
engine.runAndWait()

