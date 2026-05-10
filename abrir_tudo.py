import pyautogui as pi
import time
import pygetwindow as gw



pi.press("win")
pi.write("edge")
pi.press("enter")

pi.sleep(2.5)

pi.hotkey("ctrl", "l")

pi.sleep(1)

pi.write("www.gmail.com")
pi.press("enter")

pi.sleep(1)

pi.hotkey('ctrl', 't')

pi.sleep(2.5)

pi.hotkey("ctrl", "l")
pi.write("www.globo.com")
pi.press("enter")

pi.sleep(1)

pi.press("win")
pi.write("whatsApp")
pi.press("enter")