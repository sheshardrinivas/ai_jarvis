from time import sleep
from pynput import keyboard
import pynput
import speech_recognition as sr
import subprocess
import colorama
import random
import os
from colorama import Fore
from webbrowser import  Error, open_new
from playsound import playsound
import datetime
import json
from def_1 import question_1_0,learn
import wikipedia
import requests
import sys
import os

def is_connected():
    try:
        requests.head('https://www.google.com', timeout=1)
        return True
    except requests.RequestException:
        return False
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from setup import main

mode1=0
counter=0
l=True
from key_decoder import key_value,string_print
current_file_path = os.path.abspath(__file__)

current_dir = os.path.dirname(current_file_path)
path_location=current_dir.replace("code","")
colorama.init(autoreset=True)
with open(path_location+"/json files/config.json","r") as f:
    keybinders=json.loads(f.read())
def start(mode):

        current_hour = datetime.datetime.now().hour

        with open(path_location+"/json files/r.json","r") as f:
            data=json.loads(f.read())
        if 5 <= current_hour < 12:
            g=data["start"][0]["greeting"]
            q=data["start"][random.randint(0,2)]["question"]
            t=data["start"][random.randint(0,2)]["tell"]
            string_print(g,0.02,"")
            print(" ")
            string_print(t,0.02,"")
            print(" ")
            string_print(q,0.02,"")
            print(" ")
            if mode=="voice":
             subprocess.call(["say","-v", "Daniel",f"{g}"])
             subprocess.call(["say","-v", "Daniel",f"{t}"])
             subprocess.call(["say","-v", "Daniel",f"{q}"])
        elif 12 <= current_hour < 18:
            g=data["start"][1]["greeting"]
            q=data["start"][random.randint(0,2)]["question"]
            t=data["start"][random.randint(0,2)]["tell"]
            string_print(g,0.02,"")
            print(" ")
            string_print(t,0.02,"")
            print(" ")
            string_print(q,0.02,"")
            print(" ")
            if mode=="voice":
                subprocess.call(["say","-v", "Daniel",f"{g}"])
                subprocess.call(["say","-v", "Daniel",f"{t}"])
                subprocess.call(["say","-v", "Daniel",f"{q}"])
        elif 18 <= current_hour < 22:
            g=data["start"][2]["greeting"]
            q=data["start"][random.randint(0,2)]["question"]
            t=data["start"][random.randint(0,2)]["tell"]
            string_print(g,0.02,"")
            print(" ")
            string_print(t,0.02,"")
            print(" ")
            string_print(q,0.02,"")
            print(" ")
            if mode=="voice":
                subprocess.call(["say","-v", "Daniel",f"{g}"])
                subprocess.call(["say","-v", "Daniel",f"{t}"])
                subprocess.call(["say","-v", "Daniel",f"{q}"])
        if mode=="voice":
         activate()
        if mode=="text":
          text_mode()
def learn_fun(q,a,q1):
    q_value=question_1_0(q,a)
    if q_value ==1:
        string_print("ok",0.01,"")
        learn(q1)
    if q_value==0:
        subprocess.call(["say","-v", "Daniel","ok"])
def has_string(var):
            return isinstance(var, str)
def detect(text,data,mode):


     if "lumos" in text.lower() :
            if mode==False:
             subprocess.call(["say","-v", "Daniel","lumos"])
            print("")
            string_print("/////"*5,0.02,Fore.WHITE)
            print("")
            string_print("lumos",0.02,Fore.WHITE)
     elif "clear" in text.lower():
             print('\033c', end='')
             text_mode()
     elif "imperio" in text.lower() :
            if mode==False:
             subprocess.call(["say","-v", "Albert","imperio"])
            print("")
            string_print("/////"*5,0.01,Fore.GREEN)
            print("")
            string_print("imperio",0.01,Fore.WHITE)
     elif "wingardium leviosa" in text.lower() :
            if mode==False:
             subprocess.call(["say","-v", "Daniel","wingardium leviosa"])
            print("")
            string_print("/////"*5,0.02,Fore.BLUE)
            print("")
            string_print("wingardium leviosa",0.02,Fore.WHITE)
     elif "go to sleep" in text.lower() or "sleep" in text.lower() :
            if mode==False:
             subprocess.call(["say","-v", "Daniel","going to sleep, if you need any kind help. I am at your service sir."])
            print("")
            string_print("going to sleep...",0.01,Fore.WHITE)
            sleep1()

     elif "jarvis" in text.lower()  and "youtube" in text.lower() :

           open_new("https://www.youtube.com")


     elif "what is the time" in text.lower() or "what's the time" in text.lower() or "what's the time ?" in text.lower() or  "what is the time ?" in text.lower():
         strtime=datetime.datetime.now().strftime("%H:%M:%S")
         print("")
         string_print(f"the time is {strtime}",0.02,Fore.WHITE)
         if mode==False:
          subprocess.call(["say","-v", "Daniel",f"the time is {strtime}"])

     elif "how to" in text.lower() or "how" in text.lower() or "who is" in text.lower() or "what is" in text.lower() or "where is" in text.lower() or "what are" in text.lower()  :
         with open(path_location+"/json files/learn.json", 'r') as file:
            data = json.load(file)

         match_found = False
         for i in range(len(data["questions"])):
             if text.lower() in data["questions"][i].lower():
                 if mode==False:
                       subprocess.call(["say", "-v", "Daniel", data['ans'][i]])
                 print("")
                 string_print(data['ans'][i]+"f",0.02,Fore.BLUE)
                 match_found = True
                 break
         if not match_found:
                try:
                    q=text.lower()
                    r1=wikipedia.summary(q,10)
                    r2=wikipedia.summary(q,2)
                    if has_string(r1) == True :



                            print("")
                            string_print(r1,0.02,Fore.BLUE)
                            if mode==False:

                                subprocess.call(["say", "-v", "Daniel", f"{r2}" ])
                    else:
                        print("")
                        print("No matching question found.")
                        if mode==False:
                            subprocess.call(["say", "-v", "Daniel", "No matching question found."])
                        learn_fun("should I start the machine learning protocol?",["no","start"],text.lower())

                except:
                    if is_connected ==True:
                        print("")
                        string_print("Error:missing value",0.02,Fore.RED)
                        print("")
                        print("No matching question found.")
                        if mode==False:
                            subprocess.call(["say", "-v", "Daniel", "No matching question found."])
                        learn_fun("should I start the machine learning protocol?",["no","start"],text.lower())

                    else:
                        print("")
                        string_print("check if your are conected to the internet 🛜",0.02,Fore.RED)


     elif "understand" in text.lower() or "learn" in text.lower():
                q = text.lower().replace("unserstand", " ")
                q = text.lower().replace("learn", " ")
                learn(q)


     else :

            if mode==True:
              say_1=data["IDK"][random.randint(0,1)]["tell"]
              print(f"{say_1}")
            if mode==False:
                say_2=data["IDK"][random.randint(0,3)]["tell"]
                print(f"{say_2}")
                subprocess.call(["say","-v","Daniel", f"{say_2}"])
def activate():
 with open(path_location+"/json files/r.json","r") as f:
        data=json.loads(f.read())
 playsound(path_location+"/sounds/jug-pop-2-186887.mp3")

 string_print("listening.....",0.02,Fore.GREEN)
 global counter

 while True:

         with sr.Microphone() as source:
             recognition2=sr.Recognizer()
             recognition2.adjust_for_ambient_noise(source)

             try:



              audio2=recognition2.listen(source,timeout=False,phrase_time_limit=10)
              response2=recognition2.recognize_google(audio2)
              print(response2)
              print("lowercase: ",response2.lower())


              detect(text=response2.lower(),data=data,mode=False)


             except sr.UnknownValueError:
              counter=counter+0.5
              if counter >=2:
                  subprocess.call(["say","-v", "Daniel","good bye sir."])
                  print("going to sleep...")
                  counter=+1
                  key_detect()
def text_mode():
    text_histroy=[]
    playsound(path_location+"/sounds/jug-pop-2-186887.mp3")
    with open(path_location+"/json files/r.json","r") as f:
           data=json.loads(f.read())
    while True:
        print("")
        string_print(">>>",0.02,Fore.WHITE)
        q=input(" ")
        q=str(q)
        q=q.lower()
        detect(text=q,data=data,mode=True)




def sleep1():
    playsound(path_location+"/sounds/notification-sound-7062.mp3")
    print(" ")
    string_print("listening.....",0.02,Fore.GREEN)

    while True:
     with sr.Microphone() as source:
      recognition=sr.Recognizer()
      recognition.adjust_for_ambient_noise(source)


      try:



          audio=recognition.listen(source,timeout=False,phrase_time_limit=2)

          response=recognition.recognize_google(audio)
          print(response)
          if "jarvis" in response.lower()  and "wake up" in response.lower()  or "wake up" in response.lower() or "jarvis" in response.lower():
              activate()
              break
          if "jarvis" in response.lower()  and "goodbye" in response.lower() or "goodbye" in response.lower():
              counter=+1
              key_detect()
              break

          elif "jarvis" in response.lower()  and   "what is the time" in response.lower() or "jarvis" in response.lower()  and   "what's the time" in response.lower() or  "what's the time" in response.lower() :
              strtime=datetime.datetime.now().strftime("%H:%M:%S")
              print(f"the time is {strtime}")
              subprocess.call(["say","-v", "Daniel",f"the time is {strtime}"])

      except sr.UnknownValueError:
         pass
def key_detect():


    try:
        playsound(path_location+"sounds/notification-sound-7062.mp3")
        HOTKEY1 = {key_value[keybinders["key_binding2"][0]],key_value[keybinders["key_binding2"][1]]}
        HOTKEY2 = {key_value[keybinders["key_binding1"][0]],key_value[keybinders["key_binding1"][1]]}





        current_keys = set()

        def on_press(key):
            current_keys.add(key)

            if all(k in current_keys for k in HOTKEY1):
                print("voice assistant mode activated!")
                start(mode="voice")
            if all(k in current_keys for k in HOTKEY2):
                    print("text mode activated!")
                    start(mode="text")


        def on_release(key):
            try:
                current_keys.remove(key)
            except KeyError:
                pass


        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            print("listening for key press .....")
            listener.join()
    except KeyError:
        string_print("ERROR",0.02,Fore.RED)
        string_print(" : ",0.02,Fore.LIGHTYELLOW_EX)
        string_print("key mapping failed",0.02,Fore.YELLOW)
        print(" ")
        string_print("Try remapping the keys by running setup.py ",0.02,Fore.RED)
        print(" ")
        string_print("Do you want remap the keys if yes type y. -->",0.02,Fore.RED)
        in_1=input(" ")
        print(" ")
        if "y" in in_1:
            main()
if __name__ == "__main__":
    try:
        print(path_location)
        key_detect()
    except KeyboardInterrupt:
        print("")
