from tkinter import *
from tkinter import ttk

window = Tk()
weekday = StringVar()
weekCombo = ttk.Combobox(window, textvariable=weekday)
weekCombo.pack()
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
weekCombo.config(values=weekdays)

day = StringVar()
Spinbox(window, from_=1, to=30, textvariable=day).pack()

progressbar = ttk.Progressbar(window, orient=HORIZONTAL, length=250)
progressbar.pack()
progressbar.config(mode="indeterminate")
progressbar.start()
progressbar.stop()
progressbar.config(mode='determinate', maximum=10, value=2.2)
progressbar.config(value=0.0)
progressbar.step(5)


window.mainloop()