import pyautogui, pyscreeze

pyautogui.screenshot("apple.png", region=(0,0,70,45))
apple = pyautogui.locateAllOnScreen("apple.png")
print(list(apple))
pyautogui.click('apple.png')
pyautogui.click((0,0,70,45))
colour = pyautogui.pixel(100,100)
print(colour)
result=pyautogui.pixelMatchesColor(180,180,(62,67,67))