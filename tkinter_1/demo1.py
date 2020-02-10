#! /usr/bin/env python3.8
"""A first look at Tkinter."""


# bring in ALL the tkinter goodies
from tkinter import Tk, Label

root = Tk()

# 1. create the label
label = Label(root, text="Hello world!")

# 2. add it to the root widget
# Here we use pack() to "shove" the label into its container. It's not very
# sophisticated or elegant, but it does the job for now.
label.pack()

# set up the main loop
root.mainloop()
