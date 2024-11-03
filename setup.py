import os
import json
import colorama
import time





colorama.init(autoreset=True)
def main():
        current_file_path = os.path.abspath(__file__)

        current_dir = os.path.dirname(current_file_path)

        print("The current directory is:", current_dir)
        print("add this path to your zshrc if your are following the optional steps. ---> ",current_dir+"/code/key.py")
        with open(current_dir+"/json files/config.json", 'r') as file:
           key_bind = json.load(file)
        in1=input(f"{colorama.Fore.GREEN}Do need help --->  ")
        print("__")
        if "y" in in1:
            string_="keys  : [shift , control , option , command , tab , delete , capslock , escape , enter , end , home]"
            for i in range(len(string_)):
                print(string_[i],end="")
                time.sleep(0.03)
            print("__")


        string_1="which keys should be used for activating the text mode . type the key name with a comma . example:control,shift."
        for i in range(len(string_1)):
            print(f"{colorama.Fore.GREEN}{string_1[i]}",end="")
            time.sleep(0.02)

        keyboard_binding_in1=input(f"{colorama.Fore.GREEN} --->  ")
        short_key1=keyboard_binding_in1.split(",")
        print(key_bind["key_binding1"])
        print(f"{colorama.Fore.WHITE}{short_key1[0],short_key1[1]}")
        key_bind["key_binding1"]=[]
        with open(current_dir+"/json files/config.json", 'w') as file:
            json.dump(key_bind, file)
        key_bind["key_binding1"].append(short_key1[0])
        key_bind["key_binding1"].append(short_key1[1])

        with open(current_dir+"/json files/config.json", 'w') as file:
            json.dump(key_bind, file)

        string_2="which keys should be used for activating the voice mode . type the key name with a comma . example: shift,f1."
        for i in range(len(string_2)):
            print(f"{colorama.Fore.BLUE}{string_2[i]}",end="")
            time.sleep(0.02)


        keyboard_binding_in2=input(f"{colorama.Fore.BLUE} --->  ")
        short_key2=keyboard_binding_in2.split(",")
        print(key_bind["key_binding2"])
        print(f"{colorama.Fore.WHITE}{short_key2[0],short_key2[1]}")
        key_bind["key_binding2"]=[]
        with open(current_dir+"/json files/config.json", 'w') as file:
            json.dump(key_bind, file)
        key_bind["key_binding2"].append(short_key2[0])
        key_bind["key_binding2"].append(short_key2[1])

        with open(current_dir+"/json files/config.json", 'w') as file:
            json.dump(key_bind, file)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
