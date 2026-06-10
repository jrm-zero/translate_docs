from tkinter import *
from tkinter import ttk

def build_window(self):
    window = Tk()
    greeting = Label(
        text="Hello, World!",
        foreground="white",
        background="black"
    )
    testing = StringVar()
    entry = Entry(textvariable=testing)
    entry.pack()
    greeting.pack()
    response = entry.get()
    print(response)
    window.mainloop()
    return response
