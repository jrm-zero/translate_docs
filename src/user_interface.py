from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from translation_functions import get_supported_languages

class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Translate Documents")
        self.setvar(name="filename", value="")
        self.setvar(name="source_lang", value="")
        self.frames = {}

        for F in ([MainEntry, SecondaryWindow]):
            frame = F(self)
            self.frames[F] = frame

        self.show_frame(MainEntry)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        #raises the current frame to the top
        frame.tkraise()
        frame.grid(row=0, column=0, sticky=(N,S,E,W))

class MainEntry(Frame):
    def __init__(self, controller):
        Frame.__init__(self, controller)
        self.controller = controller
        frm_file_selection = Frame(master=self, bd=2)
        frm_source_lang_selection = Frame(master=self, bd=2)
        frm_dest_lang_selection = Frame(master=self, bd=2)

        frm_file_selection.rowconfigure(0, weight=1)
        frm_file_selection.columnconfigure([0,1], minsize=200, weight=1)
        frm_source_lang_selection.rowconfigure(0, weight=1)
        frm_source_lang_selection.columnconfigure([0,1], minsize=200, weight=1)
        frm_dest_lang_selection.rowconfigure(0, weight=1)
        frm_dest_lang_selection.columnconfigure([0,1], minsize=200, weight=1)

        self.lbl_display_file = Label(
            master=frm_file_selection, 
            background= "black",
            foreground= "white",
            relief=GROOVE, 
            text=self.controller.getvar(name="filename"),
        )
        self.btn_file_select = Button(
            master=frm_file_selection, 
            text="Select File", relief=RAISED, 
            command=self.get_filename
        )

        self.lst_source_lang = Listbox(
            master=frm_source_lang_selection, 
            listvariable=StringVar(value=get_supported_languages()),
            height=5
        )
        self.btn_source_lang = Button(
            master=frm_source_lang_selection, 
            text="Save Source Language", 
            relief=RAISED, 
            command=self.store_source_lang
        )

        self.lst_dest_lang = Listbox(
            master=frm_dest_lang_selection, 
            listvariable=StringVar(value=get_supported_languages()),
            height=5
        )
        self.btn_dest_lang = Button(
            master=frm_dest_lang_selection, 
            text="Save Destination Language", 
            relief=RAISED, 
            command=self.get_filename)

        frm_file_selection.grid(row=0, column=0, sticky=(E,W))
        frm_source_lang_selection.grid(row=1, column=0, sticky=(E,W))
        frm_dest_lang_selection.grid(row=2, column=0, sticky=(E,W))

        self.lbl_display_file.grid(row=0, column=1, sticky=(E,W))
        self.btn_file_select.grid(row=0, column=0, sticky=(E,W), padx=5, pady=5)
        self.lst_source_lang.grid(row=0, column=1, sticky=(E,W))

        self.btn_source_lang.grid(row=0, column=0, sticky=(E,W), padx=5, pady=5)
        self.lst_dest_lang.grid(row=0, column=1, sticky=(E,W))
        self.btn_dest_lang.grid(row=0, column=0, sticky=(E,W), padx=5, pady=5)
    
    def store_source_lang(self):
        lang = "black"
        self.controller.setvar(name="source_lang", value=lang)
        self.controller.show_frame(SecondaryWindow)
        return
    
    def store_dest_lang(self):
        lang = self.ent_source_lang.get()
        self.controller.setvar(name="source_lang", value=lang)
        return
    
    def get_filename(self):
        filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")]
        )
        if not filepath:
            return
        self.controller.setvar(name="filename", value=filepath)
        self.lbl_display_file["text"] = filepath
        self.controller.show_frame(MainEntry)
        return
    
class SecondaryWindow(Frame):
    def __init__(self, controller):
        Frame.__init__(self, controller)
        self.controller = controller
        frm_test = Frame(master=self, bd=2)

        self.btn_display_test = Button(
            master=frm_test,
            bg="black",
            fg="white",
            text="click me!",
            command=self.go_back
        )
        self.lbl_display_test = Label(
            master=frm_test,
            bg="black",
            fg="white",
            text="blahhhhhhhh",
        )

        frm_test.grid(row=0, column=0, sticky=(N,S,E,W))

        self.btn_display_test.grid(row=0, column=0, sticky=(N,S,E,W))
        self.lbl_display_test.grid(row=0, column=1, sticky=(N,S,E,W))

    def go_back(self):
        self.controller.show_frame(MainEntry)
        return

def main(self):
    testobj = window()
    testobj.mainloop()