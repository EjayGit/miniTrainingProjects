from tkinter import *
from tkinter import ttk

window = Tk()
label = ttk.Label(window, text="Hello TK")
label.pack()
label.config(text="Hello Erik")
label.config(wraplength=200)
label.config(justify=CENTER)
label.config(foreground="red")
label.config(font=("Arial", 20, "bold"))

# logo = PhotoImage(file="imageName.jpg")
# label.img = logo
# label.config(image=label.img)

displayImage()
label.config(compound="image") # or, 'top', 'bottom' to place text rel to logo

window.mainloop()