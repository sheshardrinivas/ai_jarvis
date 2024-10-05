from pynput import keyboard
import pynput
import speech_recognition as sr
import subprocess
import colorama
import random
from colorama import Fore
from webbrowser import open_new
from playsound import playsound
import datetime
import json
from def_1 import question_1_0,learn
counter=0
l=True
colorama.init(autoreset=True)
def start():
    if counter==0:
        current_hour = datetime.datetime.now().hour
        print(f"The time is {current_hour:02d}:00")
        with open("r.json","r") as f:
            data=json.loads(f.read())
        if 5 <= current_hour < 12:
            g=data["start"][0]["greeting"]
            q=data["start"][random.randint(0,2)]["question"]
            t=data["start"][random.randint(0,2)]["tell"]
            print(g)
            print(t)
            print(q)
            subprocess.call(["say","-v", "Daniel",f"{g}"])
            subprocess.call(["say","-v", "Daniel",f"{t}"])
            subprocess.call(["say","-v", "Daniel",f"{q}"])
        elif 12 <= current_hour < 18:
            g=data["start"][1]["greeting"]
            q=data["start"][random.randint(0,2)]["question"]
            t=data["start"][random.randint(0,2)]["tell"]
            print(g)
            print(t)
            print(q)
            subprocess.call(["say","-v", "Daniel",f"{g}"])
            subprocess.call(["say","-v", "Daniel",f"{t}"])
            subprocess.call(["say","-v", "Daniel",f"{q}"])
        elif 18 <= current_hour < 22:
            g=data["start"][2]["greeting"]
            q=data["start"][random.randint(0,2)]["question"]
            t=data["start"][random.randint(0,2)]["tell"]
            print(g)
            print(t)
            print(q)
            subprocess.call(["say","-v", "Daniel",f"{g}"])
            subprocess.call(["say","-v", "Daniel",f"{t}"])
            subprocess.call(["say","-v", "Daniel",f"{q}"])
        activate()
    elif counter>=0:
        activate()
def learn_fun(q,a,q1):
    q_value=question_1_0(q,a)
    if q_value ==1:
        print("ok")
        learn(q1)
def detect(text,data):


     if "lumos" in text.lower() :
            subprocess.call(["say","-v", "Daniel","lumos"])
            print(f"{Fore.WHITE}/////"*5)
     elif "imperio" in text.lower() :
            subprocess.call(["say","-v", "Albert","imperio"])
            print(f"{Fore.GREEN}/////"*5)
     elif "wingardium leviosa" in text.lower() :
            subprocess.call(["say","-v", "Daniel","wingardium leviosa"])
            print(f"{Fore.BLUE}/////"*5)
     elif "go to sleep" in text.lower() or "sleep" in text.lower() :
            subprocess.call(["say","-v", "Daniel","going to sleep, if you need any kind help. I am at your service sir."])
            print("going to sleep...")
            sleep1()

     elif "jarvis" in text.lower()  and "youtube" in text.lower() :
         open_new("https://www.youtube.com")

     elif "jarvis" in text.lower()  and   "what is the time" in text.lower():
         strtime=datetime.datetime.now().strftime("%H:%M:%S")
         print(f"the time is {strtime}")
         subprocess.call(["say","-v", "Daniel",f"the time is {strtime}"])
     elif "what is" in text.lower():
         with open("learn.json", 'r') as file:
            data = json.load(file)

         match_found = False
         for i in range(len(data["questions"])):
             if text.lower() in data["questions"][i].lower():
                 print(data["questions"][i] + ":" + data["ans"][i])
                 subprocess.call(["say", "-v", "Daniel", data['ans'][i]])
                 match_found = True
                 break  # Exit the loop once a match is found

         if not match_found:
             print("No matching question found.")
             subprocess.call(["say", "-v", "Daniel", "No matching question found."])
             learn_fun("should I start the machine learning protocol?",["no","start"],text.lower())



     else :
            say_1=data["IDK"][random.randint(0,2)]["tell"]
            subprocess.call(["say","-v","Daniel", f"{say_1}"])
            print(f"{say_1}")
def activate():
 with open("r.json","r") as f:
        data=json.loads(f.read())
 playsound("jug-pop-2-186887.mp3")
 print("wake")
 print("listening.....")

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


              detect(text=response2.lower(),data=data)


             except sr.UnknownValueError:
              counter=counter+0.5
              if counter >=2:
                  subprocess.call(["say","-v", "Daniel","good bye sir."])
                  print("going to sleep...")
                  counter=+1
                  key_detect()
def sleep1():
    playsound("notification-sound-7062.mp3")

    print("listening.....")

    while True:
     with sr.Microphone() as source:
      recognition=sr.Recognizer()
      recognition.adjust_for_ambient_noise(source)


      try:


          audio=recognition.listen(source,timeout=False,phrase_time_limit=2)

          response=recognition.recognize_google(audio)
          print(response)
          if "jarvis" in response.lower()  and "wake up" in response.lower():
              activate()
              break
          if "jarvis" in response.lower()  and "goodbye" in response.lower():
              counter=+1
              key_detect()
              break

      except sr.UnknownValueError:
         pass
def key_detect():
    playsound("notification-sound-7062.mp3")

    HOTKEY1 = {keyboard.Key.shift, keyboard.KeyCode(176)}
    HOTKEY2 = {keyboard.Key.ctrl,keyboard.Key.esc}


    current_keys = set()

    def on_press(key):
        current_keys.add(key)

        if all(k in current_keys for k in HOTKEY1):
            print("Hotkey 1 activated!")
            start()







    def on_release(key):
        try:
            current_keys.remove(key)
        except KeyError:
            pass


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("listening for key press .....")
        listener.join()
if __name__ == "__main__":
    try:
        key_detect()
    except KeyboardInterrupt:
        print("Program terminated.")
