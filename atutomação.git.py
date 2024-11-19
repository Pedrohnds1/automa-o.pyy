import pyautogui as auto
import time

time.sleep(2)
auto.click(x=547, y=1045)
auto.moveTo(x=749, y=452)
auto.click(x=749, y=452)
auto.write("google pacman", interval=0.25 )
auto.press("enter")
auto.moveTo(x=584, y=674)
auto.sleep(1)
auto.click(x=543, y=605)
auto.press("a")
auto.sleep(1)
auto.press("w")
auto.sleep(1)
auto.press("a")
time.sleep(1)
