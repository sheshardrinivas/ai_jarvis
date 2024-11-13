from key import mode1
import json
import os
current_file_path = os.path.abspath(__file__)

current_dir = os.path.dirname(current_file_path)
path_location=current_dir.replace("code","")
with open(path_location+"/json files/config.json","r") as f:
    data=json.loads(f.read())
mode=mode1
data["mode"]=""
with open(path_location+"/json files/learn.json", 'w') as file:
    json.dump(data, file, indent=2)
data["mode"]=mode1
with open(path_location+"/json files/learn.json", 'w') as file:
    json.dump(data, file, indent=2)