import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import win32clipboard
import os
from os import listdir

keyboard = Controller()

image_dir = (r"C:\Users\gusta\Pictures\scripts")
excel_dir = (r"C:\Users\gusta\Documents\bot.xlsx")

f = open(excel_dir, "r")
print(f.readlines(), encoding="utf8")

def send_whatsapp_message():
    msg="Test message from a Python script!"
    image_dir = (r"C:\Users\gusta\Pictures\scripts")
    while (True):
        for images in os.listdir(image_dir):
            print(images)
            try:
                pywhatkit.sendwhats_image(
                    receiver="",
                    img_path=(image_dir + '//' + images), 
                    caption=msg,
                    tab_close=True
                )
                time.sleep(10)
                pyautogui.click()
                time.sleep(2)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                print("Message sent!")
            except Exception as e:
                print(str(e))
            time.sleep(30)


if __name__ == "__main__":
    send_whatsapp_message()