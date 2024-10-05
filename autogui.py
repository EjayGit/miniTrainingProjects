import pyautogui, time

wh = pyautogui.size()
print(wh[1])
pyautogui.FAILSAFE = False
for x in range(5):
    pyautogui.moveTo(20,20,0.1)
    pyautogui.moveTo(600,20,0.1)

position = pyautogui.position()
print(position[1])

time.sleep(2)
pyautogui.click()
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.drag(100,0,duration=0.5,button='left') # relaive to current pos
pyautogui.mouseInfo()