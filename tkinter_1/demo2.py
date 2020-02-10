#! /usr/bin/env python3.8
"""Examining the Tkinter grid."""

# bring in ALL the tkinter goodies
from tkinter import Tk, Label

root = Tk()

for r in range(3):
    for c in range(4):
        label = Label(
            root, text=f"row={r}, col={c}", padx=10, pady=10, borderwidth=1, relief="solid"
        )
        label.grid(row=r, column=c)

# set up the main loop
root.mainloop()
