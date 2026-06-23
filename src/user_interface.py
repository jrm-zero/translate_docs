from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Translate Documents")
        self.setvar(name="filename", value="No path found.")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)

        txt_edit = Entry(self)
        frm_buttons = Frame(master=self, relief=RAISED, bd=2)
        
        btn_open = Button(self, text="Open", command=self.get_filename)
        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        frm_buttons.grid(row=0, column=0, sticky="ns")
        txt_edit.grid(row=0, column=1, sticky="nsew")

    def get_filename(self):
        filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.setvar(name="filename", value=filepath)
        return self.getvar(name="filename")
 
def main(self):
    testobj = window()
    testobj.mainloop()
    return testobj.getvar(name="filename")