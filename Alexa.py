'''Alexa Using Python Programming'''

'''Importing Essential Files For The Ai'''
#importing speech recognition for recognize the user voice
import speech_recognition as sr
#importing pyttsx3 for convert voice to text
import pyttsx3 as vt
#importing pywhatkit for direct connect with the source
import pywhatkit as pwk
#importing date time for show date and time 
import datetime as dt
#importing jokes for displaying jokes
import pyjokes as jokes 
#importing wikipedia for huge detais about something
import wikipedia as wk 
#importing google search enginee for search
from googlesearch import search
#importing webbrowser
import webbrowser


'''Creating class for setup voice recognation and enginee'''
class Alexa(object):
   listner = sr.Recognizer()
   vc = sr.Microphone()
   enginee = vt.init()
   voices = enginee.getProperty('voices')
   enginee.setProperty('voice', voices[1].id)

   '''Method for say something'''
   def Text2Talk(self,text):
      self.enginee.say(text)
      self.enginee.runAndWait()

      return 0
   
   def UserCommands(self):
      self.Text2Talk('i am an ai chat bot and my name is bloody marry, What can I do for you, sir')
      try:
         with self.vc:
            print('Listening...')
            voice_commands = self.listner.listen(self.vc)
            text_commands = self.listner.recognize_google(voice_commands)
            commands = text_commands.lower()
            print("Your Commands: ",commands)

      except:
         error_msg = 'Something went wrong, please try again with correct direction.'
         print(error_msg)
         self.Text2Talk('Sorry can you command me again')

      return commands   

   def Actions(self):
      command = self.UserCommands()
      if 'how are you' in command:
         self.Text2Talk('I am fine, thank you and how are you')

      elif 'song' in command:
         index = command.index('song')
         song_start = index+4
         song = command[song_start:]
         pwk.playonyt(song)

      elif 'time' in command:
         cTime = dt.datetime.now().strftime('%I:%M %p')
         self.Text2Talk('Its ',cTime,' O clock')

      elif 'about' in command:
         index = command.index('about')
         start_about = index+5
         person = command[start_about:]
         info = wk.summary(person)
         print(info)
         self.Text2Talk(info)

      elif 'joke' in command:
         jokesss = jokes.get_joke()
         print(jokesss)
         self.Text2Talk(jokesss)

      elif 'i love you' in command:
         self.Text2Talk('i love you too')

      elif 'number' in command:
         print('+8801729-602502')
         self.Text2Talk('as an ai bot i have no contact number but i can give you my owner number and the number is +8801729602502, his name is monirul islam')

      elif 'search' in command:
         index = command.index('search')
         search_item = command[index+6]
         url = "https://www.google.com/search?q=" + search_item + "&hl=" + "en"
         webbrowser.open_new_tab(url)

      elif 'open ai' in command:
         webbrowser.open_new_tab('https://chat.openai.com/chat')

      elif 'open facebook' in command:
         webbrowser.open_new_tab('https://www.facebook.com/')

      elif 'owner' in command:
         self.Text2Talk('He is a very much cute and intelligent person in the world and his name is Monirul Islam. Dont take him easily, he is cold war commander. ha ha ha ha ha ha ha, i am just joking. my owner is Monirul islam and he is very simple person. I am opening his facebook id for you')
         webbrowser.open_new_tab('https://www.facebook.com/profile.php?id=100087187981300')

      else:
         self.Text2Talk('Something Wrong Happening')


      return 0


class Test:
   obj = Alexa()
   obj.Actions()