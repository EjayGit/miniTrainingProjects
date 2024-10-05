from tkinter import *
from tkinter import ttk

window = Tk()
button = ttk.Button(window, text="Click me")
button.pack() # packs the item into the window

def buttonPress():
    print("the button is pressed")

button.config(command=buttonPress)
button.state(["!disabled"]) # button.state(["!disabled"])
print(button.instate(["disabled"]))
#button.invoke()

#logo = PhotoImage(file="python.gif")
#smallLogo = logo.subsample(5,5)
#button.config(image=smallLogo, compound=CENTER)

checkButton = ttk.Checkbutton(window, text="Agree")
checkButton.pack()
agree = StringVar()
checkButton.config(variable=agree, onvalue="agree", offvalue="disagree")

def buttonPress():
    print(agree.get())

checkButton.config(command=buttonPress)

language = StringVar()
ttk.Radiobutton(window, text="Python", variable=language, value="python").pack()
ttk.Radiobutton(window, text="Java", variable=language, value="java").pack()
ttk.Radiobutton(window, text="C++", variable=language, value="C++").pack()

checkButton.config(textvariable=language)

entry = ttk.Entry(window, width=20)
entry.pack()
entry.insert(0, "Hello Erik")
entry.config(show="*") # entry.state(["!disabled"])

window.mainloop()