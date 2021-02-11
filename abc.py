import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('volume',1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hello bhaskar how are you")
engine.say('The quick brown fox jumped over the lazy dog.')
   

engine.runAndWait()