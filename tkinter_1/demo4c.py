#! /usr/bin/env python3.8
"""Button demo."""

# bring in ALL the tkinter goodies
from tkinter import *


def increment():
    """Increment the count."""
    current_val = count.get()
    count.set(current_val + 1)


def decrement():
    """Decrement the count."""
    current_val = count.get()
    count.set(current_val - 1)


root = Tk()

count = IntVar(root)
count.set(0)

display = Label(root, textvariable=count)
display.pack()

start = Button(root, padx=10, pady=10, text="Increment", command=increment)
start.pack(side=LEFT)
start = Button(root, padx=10, pady=10, text="Decrement", command=decrement)
start.pack(side=RIGHT)

# set up the main loop
root.mainloop()
