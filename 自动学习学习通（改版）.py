import pyautogui
import keyboard
import time

xy_list = ['x=1669, y=349', 'x=1671, y=385', 'x=1671, y=417', 'x=1671, y=513',
           'x=1671, y=539', 'x=1664, y=592', 'x=1653, y=667', 'x=1652, y=701', 'x=1652, y=788',
           'x=1671, y=829', 'x=1675, y=876', 'x=1668, y=958', 'x=1659, y=994']
sleeptime = 60  # 1分钟

while True:
    if keyboard.is_pressed('k'):  # 当我按下k时执行以下命令
        while True:
            for i in xy_list:
                x = int(i[2:6])
                y = int(i[10:])
                pyautogui.click(x=x, y=y)  # 列表xy位置
                time.sleep(8)
                pyautogui.click(x=740, y=709)  # 视频暂停键位置

                time.sleep(sleeptime * 30)
