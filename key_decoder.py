import json
import os
import threading
from setup import string_print
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)


check_list=["delete","command","option","escape","capslock"]
with open(current_dir+"/json files/config.json", 'r') as file:
  key_list = json.load(file)





def m1(list,index):
   for i in range(len(check_list)):
        if check_list[i] in key_list[f"{list}"][index]:
            string_print(f"true{index,list}",0.02,"")
            if index ==0:
                key_coder=[key_list[f"{list}"][index],key_list[f"{list}"][1]]
                print(key_coder)
            if index ==1:
                key_coder=[key_list[f"{list}"][0],key_list[f"{list}"][index]]
                print(key_coder)

def t1(list_):
    for i in range(len(key_list[f"{list_}"])):
        thread = threading.Thread(target=m1(f"{list_}",i))
        thread.start()

t1("key_binding1")
t1("key_binding2")
