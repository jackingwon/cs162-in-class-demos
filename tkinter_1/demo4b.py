#! /usr/bin/env python3.8
"""Button demo."""

# bring in ALL the tkinter goodies
from tkinter import *


def method_3(txt):
    output_label_text.set(txt)


root = Tk()

output_label_text = StringVar()

input_label = Label(root, text="Enter your name: ", padx=10, pady=10)
input_label.grid(row=0, column=0)

user_name = Entry(root)
user_name.grid(row=0, column=1)

output_label = Label(root, padx=10, pady=10, textvariable=output_label_text)
output_label.grid(row=1, column=0)

# name = user_name.get()
button = Button(root, text="Click Me!", padx=15, pady=15, command=lambda: method_3(user_name.get()))
button.grid(row=2)

# set up the main loop
root.mainloop()
