#! /usr/bin/env python3.8
"""Button demo."""

# bring in ALL the tkinter goodies
from tkinter import *


def add_label():
    """Click handler."""
    label = Label(root, text="You clicked a button!!", padx=5, pady=5)
    label.pack()


root = Tk()

button = Button(root, text="Click Me!", command=add_label)
button.pack()

# set up the main loop
root.mainloop()
