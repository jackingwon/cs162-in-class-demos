#! /usr/bin/env python3.8
"""Button demo."""

# bring in ALL the tkinter goodies
from tkinter import *


def greet():
    """Click handler."""
    # method 1
    output_label["text"] = user_name.get()

    # method 2
    # output_label.config(text=user_name.get())


root = Tk()

input_label = Label(root, text="Enter your name: ", padx=10, pady=10)
input_label.grid(row=0, column=0)

user_name = Entry(root)
user_name.grid(row=0, column=1)

output_label = Label(root, text="", padx=10, pady=10)
output_label.grid(row=1, column=0)

button = Button(root, text="Click Me!", padx=15, pady=15, command=greet)
button.grid(row=2)

# set up the main loop
root.mainloop()
