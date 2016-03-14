#!/usr/bin/env python3

import Tkinter
from Tkinter import *
import ScrolledText

window = Tkinter.Tk(className="TKEDIT")
textbox = ScrolledText.ScrolledText(window, width=110, height=90)

window.mainloop()