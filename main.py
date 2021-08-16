import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty("rate")
print(rate)
engine.setProperty("rate", 150)
def  talk(text):
  engine.say(text)
  engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:


            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'biscuit' in command:
                command = command.replace('biscuit', '')
                print(command)

    except:
       pass
    return command


def run_biscuit():

      command = take_command()
      print(command)
      if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

      elif 'time' in command:
          time = datetime.datetime.now().strftime('%I:%M %p')
          talk('current time is' + time)

      elif 'who is' in command:
          person = command.replace('who is', '')
          info = wikipedia.summary(person, 1)
          print(info)
          talk(info)
      elif 'how are you' in command:
          talk('I am great,what about you?')

      elif 'what are you doing' in command:
          talk('nothing much,just waiting for you')
      elif 'who are you' in command:
          talk("I am biscuit, your virtual assistant sir.")

      elif 'are you free' in command:
          talk('Yes, what can I do for you?')
      elif 'open youtube' in command:
          webbrowser.open("youtube.com")
      elif 'open google' in command:
          webbrowser.open("google.com")
      elif 'joke' in command:
          talk(pyjokes.get_jokes())
      elif 'cook' in command:
          talk("Mrunal's Kitchenette cooks better than me,please ask her to cook for you sir")
      elif 'you cook better' in command:
          talk('Yes I do,I was just trying to be modest')
      elif 'andu pandu' in command:
          talk('OnduBhondu also known as Sanidhya Shenwai is a melodramatic girl.')
      elif 'call bobo' in command:
          talk('bobochiki chiki chiki chiki chiki come here')
      else:
          talk('I could not understand,can you please say it again?')

while True:
    run_biscuit()
