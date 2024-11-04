from pynput import keyboard
import pynput
import time
def string_print(string_,time_,color_):
  for i in range(len(string_)):
    print(f"{color_}{string_[i]}",end="")
    time.sleep(time_)
key_value={"shift":keyboard.Key.shift,"control":keyboard.Key.ctrl,"tab":keyboard.Key.tab,"delete":keyboard.Key.backspace,"command":keyboard.Key.cmd,"option":keyboard.Key.alt,"escape":keyboard.Key.esc,"capslock":keyboard.Key.caps_lock,"home":keyboard.Key.home,"end":keyboard.Key.end,"enter":keyboard.Key.enter,"f1":keyboard.Key.f1,"f2":keyboard.Key.f2,"f3":keyboard.Key.f3,"f4":keyboard.Key.f4,"f5":keyboard.Key.f5,"f6":keyboard.Key.f6,"f7":keyboard.Key.f7,"f8":keyboard.Key.f8,"f9":keyboard.Key.f9,"f10":keyboard.Key.f10,"f11":keyboard.Key.f11,"f12":keyboard.Key.f12}
