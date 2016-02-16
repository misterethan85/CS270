#!/usr/bin/env python3

##################################
# Program Name: HyperTyper       #
# Version: 2.1.8                 #
# Author: Ethan Hicks            #
# Published: 2/15/2016           #
################################## 


try:
    # for Python2
    from Tkinter import * 
except ImportError:
    # for Python3
    from tkinter import * 


class HyperType(Text):

    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        self.bind('<Control-c>', self.copy)
        self.bind('<Control-x>', self.cut)
        self.bind('<Control-v>', self.paste)
        self.bind('<Control-s>', self.save)
        self.bind('<Control-o>', self.Open_File)
        
        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="New")
        menu.add_command(label="Open")
        menu.add_command(label="Save")
        menu.add_command(label="Close")
        menu.add_command(label="Quit")

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Cut")
        menu.add_command(label="Copy")
        menu.add_command(label="Paste")

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="HALP MEH!!")
        menu.add_command(label="About...")
        
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)
            
    def copy(self, event=None):
        self.clipboard_clear()
        text = self.get("sel.first", "sel.last")
        self.clipboard_append(text)
    
    def cut(self, event=None):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event=None):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)
    
    def save(self, event=None):
        print('THIS SAVES SOMETHING')
    
    def new(self, event=None):
        print('This Will Create a new window')

    def Open_File(self, event=None):
        root.filename = filedialog.askopenfilename(filetypes = (("text files",".txt"),("All Files","*.*")))
        text = root.filename.split('/')
        filename = text[-1]
        entry1.insert(0,filename)
        #print(filename)

    def Save_File(self):
        root.filename = filedialog.asksaveasfilename(filetypes = (("text files",".txt"),("All Files","*.*")))
        text = root.filename.split('/') 
        filename = text[-1]
        entry2.insert(0,filename)



root = Tk()
session = HyperType(root)
session.pack(fill='both', expand=1)
root.mainloop()
