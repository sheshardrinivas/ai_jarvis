
import speech_recognition as sr
import subprocess
import json
import progressbar
import time
def question_1_0(q,ans):

    with sr.Microphone() as source:
        print(q)
        subprocess.call(["say","-v", "Daniel",f"{q}"])
        print(f"{ans[0]}:{ans[1]}")
        recognition2=sr.Recognizer()
        recognition2.adjust_for_ambient_noise(source)

        try:
            audio2=recognition2.listen(source,timeout=False,phrase_time_limit=10)
            response2=recognition2.recognize_google(audio2)
            print(response2)
            print("lowercase: ",response2.lower())
            if ans[0] in response2.lower():
                return 0

            elif ans[1] in response2.lower():
                return 1

        except sr.UnknownValueError:
            print("not an opion!")
            return 404
def learn(q):
    try:
        with open("learn.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"questions": [], "ans": []}





    with sr.Microphone() as source:

                recognition3=sr.Recognizer()
                recognition3.adjust_for_ambient_noise(source)
                try:
                    subprocess.call(["say","-v", "Daniel","say the answer"])
                    print("say the answer")
                    audio3=recognition3.listen(source,timeout=False,phrase_time_limit=20)
                    response3=recognition3.recognize_google(audio3)
                    print(response3)
                    print("lowercase: ",response3.lower())
                    ans=response3.lower()
                    print(q,":",ans)
                    data["questions"].append(q)
                    data["ans"].append(ans)
                    with open("learn.json", 'w') as file:
                        json.dump(data, file, indent=2)
                    bar = progressbar.ProgressBar(maxval=100, widgets=[progressbar.Bar('>', '[', ']'), ' ', progressbar.Percentage()])
                    bar.start()

                    for i in range(100):
                        time.sleep(0.1)
                        bar.update(i+1)
                    bar.finish()
                    subprocess.call(["say","-v", "Daniel"," learnt successfully."])
                    print("Question and answer added successfully!")
                except sr.UnknownValueError:
                    pass
