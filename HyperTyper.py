#!/usr/bin/env python3

##################################
# Program Name: HyperTyper       #
# Version: 2.4.0                 #
# Author: Ethan Hicks            #
# Published: 2/17/2016           #
################################## 


try:
    # for Python2
    import TKinter
    from Tkinter import * 
except ImportError:
    # for Python3
    import tkinter
    from tkinter import * 
    from tkinter import filedialog
    from tkinter import messagebox


class HyperType(Text):

    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        self.bind('<Control-a>')
        self.bind('<Control-c>')
        self.bind('<Control-x>')
        self.bind('<Control-v>')
        self.bind('<Control-n>', self.new)
        self.bind('<Control-s>', self.Save_File)
        self.bind('<Control-o>', self.Open_File)
        self.bind('<Control-q>', self.quit)
        
        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=1)
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="New", command=self.new)
        menu.add_command(label="Open", command=self.Open_File)
        menu.add_command(label="Save", command=self.Save_File)
        menu.add_command(label="Save as", command=self.Save_as_File)
        menu.add_command(label="Close", command=self.destroy)
        menu.add_command(label="Quit", command=self.quit)

        menu = Menu(self.menubar, tearoff=1)
        self.menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Select All", command= self.Select_All)
        menu.add_command(label="Cut", command=self.Cut)
        menu.add_command(label="Copy")
        menu.add_command(label="Paste", command=self.Paste)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="About...", command = self.Get_Help)
        
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)

    def Select_All(self, event=None):
        text = self.get("1.0",'end-1c')
        
    def Copy(self, event=None):
        self.clipboard_clear()
        text = self.get("sel.first", "sel.last")
        self.clipboard_append(text)
    
    def Cut(self, event=None):
        self.clipboard_clear()
        self.Copy()
        self.delete("sel.first", "sel.last")

    def Paste(self, event=None):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)
    
    def new(self, event=None):
        Toplevel()

    def quit(self, event=None):
        root.quit()

    def close(self, event=None):
        print('close function on its way')

    def Open_File(self, event=None):
        self.filename = filedialog.askopenfilename(filetypes = (("All Files","*.*"),("Text Files",".txt")))
        f = open(self.filename)
        filedata = f.read()
        self.insert("end",filedata)

    def Save_File(self, event=None):
        try:
            filer = open(self.filename,'w')
            data = self.get("1.0",'end-1c')
            filedata = filer.write(data)
        except AttributeError:
            self.filename = filedialog.asksaveasfilename(filetypes = (("text Files",".txt"),("All Files","*.*")))
            f = open(self.filename, 'w')
            data = self.get("1.0",'end-1c')
            filedata = f.write(data) 
    
    def Save_as_File(self, event=None):
        self.filename = filedialog.asksaveasfile(filetypes = (("text Files",".txt"),("All Files","*.*")))
        data = self.get("1.0",'end-1c')
        filedata = self.filename.write(data)

    def Get_Help(self, event=None):
        box = messagebox.showinfo("GENERIC HELP WINDOW", "SORRY THIS IS USELESS")


root = Tk()
session = HyperType(root)
session.pack(fill='both', expand=1,)
root.mainloop()

# For Doctesting via command line:
# pytohn3 -m doctest HyperTyper.py
