from tkinter import *
from tkinter import ttk

def build_window(self):
    window = Tk()
    frame_file_path = Frame()
    #frame_src_lang = Frame()
    lbl_file_path = Label(
        master=frame_file_path,
        text="Enter Location",
        foreground="white",
        background="black",
    )
    ent_file_path = Entry(master=frame_file_path)
    frame_file_path.pack()
    lbl_file_path.pack()
    ent_file_path.pack()
    window.mainloop()
    return


