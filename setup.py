import os
import json
import colorama
import time
import progressbar


def string_print(string_,time_,color_):
  for i in range(len(string_)):
    print(f"{color_}{string_[i]}",end="")
    time.sleep(time_)


keyslist=["shift" , "control" , "option" , "command" , "tab" , "delete" , "capslock" , "escape" , "enter" , "end" , "home" , "f1" , "f2" , "f3" ,"f4" , "f5" , "f6" , "f7" , "f8" , "f9" ," f10 ", "f11 ", "f12"]

colorama.init(autoreset=True)


def main():


        print('\033c', end='')


        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file_path)


        string_print("The current directory is:"+current_dir,0.02,"")
        print("  ")
        string_print("add this path to your zshrc if your are following the optional steps. ---> "+current_dir+"/code/key.py",0.02,"")
        print("  ")


        with open(current_dir+"/json files/config.json", 'r') as file:
           key_bind = json.load(file)


        string_print("Do need help --->",0.02,colorama.Fore.MAGENTA)
        in1=input(f"{colorama.Fore.GREEN} ")
        print("__")
        if "y" in in1:
            string_0="keys  : [shift , control , option , command , tab , delete , capslock , escape , enter , end , home , f1 , f2 , f3 ,f4 , f5 , f6 , f7 , f8 , f9 , f10 , f11 , f12]"
            string_print(string_0,0.02,colorama.Fore.WHITE)
        print("")
        print(f"{colorama.Fore.GREEN}__")


        print(" ")
        try:

            string_1="which keys should be used for activating the text mode . type the key name with a comma . example:shift,control.  ---> "
            string_print(string_1,0.04,colorama.Fore.GREEN)

            keyboard_binding_in1=input(f"{colorama.Fore.BLUE} ")

            short_key1=keyboard_binding_in1.split(",")
            print(key_bind["key_binding1"])
            print(f"{colorama.Fore.WHITE}{short_key1[0],short_key1[1]}")


            with open(current_dir+"/json files/config.json", 'w') as file:
                json.dump(key_bind, file)
            key_bind["key_binding1"]=[short_key1[0],short_key1[1]]
            with open(current_dir+"/json files/config.json", 'w') as file:
              json.dump(key_bind, file)
#voice
            print("  ")
            string_2="which keys should be used for activating the voice mode . type the key name with a comma . example: shift,f1.  ---> "
            string_print(string_2,0.04,colorama.Fore.BLUE)
            keyboard_binding_in2=input(f"{colorama.Fore.MAGENTA} ")

            short_key2=keyboard_binding_in2.split(",")
            print(key_bind["key_binding2"])
            print(f"{colorama.Fore.WHITE}{short_key2[0],short_key2[1]}")


            key_bind["key_binding2"]=[short_key2[0],short_key2[1]]


            with open(current_dir+"/json files/config.json", 'w') as file:
                json.dump(key_bind, file)
        except IndexError:
            string_print("Error: ",0.02,colorama.Fore.RED)
            string_print("value missing",0.02,colorama.Fore.YELLOW)
            print(" ")

            string_print("do want restart has the missing value can an cause error in your configuration. ---> ",0.02,colorama.Fore.RED)

            in_fail=input(f"{colorama.Fore.GREEN} ")
            print(" ")
            if  "y" in in_fail:
                string_print("Restarting...",0.02,colorama.Fore.GREEN)
                bar = progressbar.ProgressBar(maxval=100, widgets=[progressbar.Bar('#', '', ''), ' ', progressbar.Percentage()])
                bar.start()

                for i in range(100):
                    time.sleep(0.1)
                    bar.update(i+1)
                bar.finish()
                time.sleep(0.1)
                main()
            else:
                pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
