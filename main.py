#pip install pyautogui in command prompt
import pyautogui
import time
time.sleep(4)
for i in range(1000):
    pyautogui.typewrite("hell we are in auto mode")
    pyautogui.press('enter')
    time.sleep(0.1)
