import os
 # Get the absolute path of the current script
current_file_path = os.path.abspath(__file__)
print("The current file is located at:", current_file_path)
 # To get the directory of the current file
current_dir = os.path.dirname(current_file_path)
print("The current directory is:", current_dir)
