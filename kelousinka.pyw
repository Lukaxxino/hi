image = "python_and_check_logo.gif"
import easygui as e

import os
os.system("@echo off")
msg = "Do you like Kellydog?"
choices = ["Yes","No","Kellydog"]
target = rf"C:\Users\JAGYM\Downloads\kelly.jpg"

import shutil
os.system("python3 -m pip install EasyGUI")
import random
i = 1
f = 1
while i != 160:
    reply = e.buttonbox(msg, "Je Kellydog hodný", choices=choices)
    i = 1 + i
    if reply == "Yes":
        break
    elif reply == "Kellydog":
        e.msgbox("správná odpověd")
        break
    elif reply == "No":
        u = 0
        e.msgbox(f"Ok I will create {f} more Kelly fotos next time 8x that")
        while u != f:
            u = u + 1
            original = rf"C:\Users\JAGYM\Desktop\kelly{random.randint(0,100000)}.jpg"
            shutil.copyfile(target, original)
            #os.system("copy C:/Users/JAGYM/Downloads/kelly.jpg C:/Users/JAGYM/Plocha")
            
            
        f = 8 * f

    