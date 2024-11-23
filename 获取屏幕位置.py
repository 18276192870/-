import pyautogui
import keyboard

while True:
    keyboard.wait('esc')  # 按下esc键后获取一个位置
    print(pyautogui.position())
