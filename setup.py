import os
import json
import colorama


colorama.init(autoreset=True)
def main():
        current_file_path = os.path.abspath(__file__)

        current_dir = os.path.dirname(current_file_path)
        print("The current directory is:", current_dir)
        with open(current_dir+"/json files/export.json", 'r') as file:
            data = json.load(file)
        data["exports"]=current_dir
        with open(current_dir+"/json files/export.json", 'w') as file:
            json.dump(data, file, indent=2)
        keyboard_binding_in1=input(f"{colorama.Fore.GREEN}which keys should be used for activate the text mode . right the key name with a comma . example:control,shift. --->  ")
        short_key1=keyboard_binding_in1.split(",")
        print(short_key1[0],short_key1[1])
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
