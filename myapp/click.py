import pyautogui
import time
import pygetwindow as gw

inputBoxCoord = [1209,733]
# inputBoxCoord = [1183,287]
time.sleep(3)
game_window = gw.getWindowsWithTitle("Client Version 82.2.0(40268)")[0]
game_window.activate()

pyautogui.moveTo(inputBoxCoord[0], inputBoxCoord[1], duration=0)
pyautogui.mouseDown()
time.sleep(0.3)
pyautogui.mouseUp()


# pyautogui.click(inputBoxCoord[0],inputBoxCoord[1])

print("Input Click")