import os
import json
import colorama
from typing import List





colorama.init(autoreset=True)
def main():
        current_file_path = os.path.abspath(__file__)

        current_dir = os.path.dirname(current_file_path)

        print("The current directory is:", current_dir)
        print("add this path to your zshrc if your are following the optional steps. ---> ",current_dir+"/code/key.py")
        with open(current_dir+"/json files/export.json", 'r') as file:
           key_bind = json.load(file)

        keyboard_binding_in1=input(f"{colorama.Fore.GREEN}which keys should be used for activate the text mode . right the key name with a comma . example:control,shift. --->  ")
        short_key1=keyboard_binding_in1.split(",")
        print(key_bind["key_binding1"])
        print(f"{colorama.Fore.WHITE}{short_key1[0],short_key1[1]}")
        key_bind["key_binding1"]=[]
        with open(current_dir+"/json files/export.json", 'w') as file:
            json.dump(key_bind, file)
        key_bind["key_binding1"].append(short_key1[0])
        key_bind["key_binding1"].append(short_key1[1])

        with open(current_dir+"/json files/export.json", 'w') as file:
            json.dump(key_bind, file)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
