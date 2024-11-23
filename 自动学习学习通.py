import pyautogui
import keyboard
import time

sleeptime = 60  # 1分钟
#56
n = 67  # 初始第一个视频

while True:
    if keyboard.is_pressed('k'):  # 当我按下k时执行以下命令
        while True:
            if n == 79:
                n = 67
            pyautogui.press('Tab', n)
            pyautogui.press('Enter')
            time.sleep(8)
            pyautogui.click(x=759, y=769)
            n += 1

            time.sleep(sleeptime * 25)  # 睡眠23分钟
            #time.sleep(30)