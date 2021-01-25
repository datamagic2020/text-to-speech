import pyttsx3

msg="Hello Everyone"
player = pyttsx3.init()
voices = player.getProperty('voices')
player.setProperty('voice', voices[1].id)
player.say(msg)
player.runAndWait()
print(msg)