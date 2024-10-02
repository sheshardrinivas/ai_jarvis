
import speech_recognition as sr
import subprocess

def question_1_0(q,ans):

    with sr.Microphone() as source:
        print(f"{ans[0]}:{ans[1]}")
        recognition2=sr.Recognizer()
        recognition2.adjust_for_ambient_noise(source)
        subprocess.call(["say","-v", "Daniel",f"{q}"])
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
def learn():
    with sr.Microphone() as source:

        recognition2=sr.Recognizer()
        recognition2.adjust_for_ambient_noise(source)

        try:
            print("say the q")
            audio2=recognition2.listen(source,timeout=False,phrase_time_limit=10)
            response2=recognition2.recognize_google(audio2)
            print(response2)
            print("lowercase: ",response2.lower())
            q=response2
            with sr.Microphone() as source:

                recognition3=sr.Recognizer()
                recognition3.adjust_for_ambient_noise(source)
                try:
                    print("say the answer")
                    audio3=recognition3.listen(source,timeout=False,phrase_time_limit=20)
                    response3=recognition3.recognize_google(audio3)
                    print(response3)
                    print("lowercase: ",response3.lower())
                    ans=response3
                    print(q,":",ans)
                except sr.UnknownValueError:
                    pass

        except sr.UnknownValueError:
            pass
