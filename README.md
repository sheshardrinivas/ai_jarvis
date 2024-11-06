# A.I J.A.R.V.I.S

J.A.R.V.I.S




## How to use

Follow the commands down, Then press control+shift for text-mode if you want to activate vioce controlled mode press shift+🎙️. the 🎙️ button on mac is the f5 key.

## Mac os

Make sure that [Python](https://www.python.org) and [Homebrew](https://brew.sh) are installed.

open your terminal and paste this command in it.

1. brew install portaudio

2. cd ~/documents

3. git clone https://github.com/sheshadarinivas/ai_jarvis.git

4. pip install -r requirements.txt

Now run the setup wizard by run the command.

5. python3 setup.py

After that run jarvis by this command.

python3 code/key.py 


## optional steps :

1. open your ~/.zshrc file with nano or vim.

 nano ~/.zshrc or vim ~/.zshrc

2. Now paste this command.

 alias jarvis="python3 ~/documents/ai_jarvis/code/key.py"

 now press control+x , y , enter.

3. restart your terminal and paste this command.

   source ~/.zshrc
