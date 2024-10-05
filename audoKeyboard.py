import pyautogui, time

time.sleep(3)
pyautogui.write(["p", "y", "a", "p", "enter"], 0.2)
print(pyautogui.KEYBOARD_KEYS)

pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

pyautogui.hotkey("ctrl", "c")
output = pyautogui.alert("This is very important")
print(output)

prompt = pyautogui.prompt("What is your pets name?")
print(prompt)

pword = pyautogui.password("Enter password")
print(pword)pyap
$