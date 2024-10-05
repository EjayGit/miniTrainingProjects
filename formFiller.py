import pyautogui, time

form_data = [{'name': 'Alice', 'position': 'Python Developer', 'language': 'Python', 'agree_disagree': 4,
              'comments': 'I Love Python.'},
             {'name': 'John', 'position': 'IT Analyst', 'language': 'Swift', 'agree_disagree': 4, 'comments': 'n/a'},
             {'name': 'Edy', 'position': 'Project Manager', 'language': 'Java', 'agree_disagree': 1,
              'comments': 'I prefer Java over Python'},
             {'name': 'Redy', 'position': 'QA Tester', 'language': 'Python', 'agree_disagree': 5,
              'comments': 'Python is the best'},
             ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')
time.sleep(5)


for person in form_data:
    pyautogui.write("\t\t\t")
    pyautogui.write(person["name"])
    pyautogui.write("\t")
    pyautogui.write(person["position"])
    pyautogui.write("\t")
    if person['language'] == 'Python':
        pyautogui.write(["space"], 0.5)
    elif person['language'] == 'Java':
        pyautogui.write(["down"], 0.5)
    elif person['language'] == 'Javascript':
        pyautogui.write(["down", "down"], 0.5)
    elif person['language'] == 'Swift':
        pyautogui.write(["down","down","down"], 0.5)
    pyautogui.write("\t\t")
    if person['agree_disagree'] == 1:
        pyautogui.write(["space"], 0.5)
    elif person['agree_disagree'] == 2:
        pyautogui.write(["right"], 0.5)
    elif person['agree_disagree'] == 3:
        pyautogui.write(["right", "right"], 0.5)
    elif person['agree_disagree'] == 4:
        pyautogui.write(["right","right","right"], 0.5)
    elif person['agree_disagree'] == 5:
        pyautogui.write(["right","right","right","right"], 0.5)
    pyautogui.write("\t\t")
    pyautogui.write(person["comments"])
    pyautogui.write("\t", 0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.write("\t")
    pyautogui.press("enter")
    time.sleep(0.5)