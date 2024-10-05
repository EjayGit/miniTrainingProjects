import tkinter

window = tkinter.Tk()
window.title("Welcome to Tkinter")
window.minsize(300,200)
button = tkinter.Button(window, text="Click on me")
button.pack()
print(button["text"])
button["text"] = "ok"
button.config(text="press on me")
print(button["text"])
label = tkinter.Label(window, text="I am a label", font=("Arial", 25, "bold"))
label.pack(side="right")


window.mainloop()