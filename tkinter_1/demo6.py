#! /usr/bin/env python3.8
"""One-function calculator."""

import tkinter as tk

root = tk.Tk()
root.title("One-function calculator")
root.geometry("250x350")

display = tk.Entry(root, borderwidth=5)
display.grid(row=0, column=0, padx=10, pady=10, columnspan=4, sticky="we")
root.grid_columnconfigure((0, 1, 2, 3), uniform="equal", weight=1)
root.grid_rowconfigure((1, 2, 3, 4), uniform="equal", weight=1)

button_7 = tk.Button(root, text="7").grid(row=1, column=0, sticky="nsew")
button_8 = tk.Button(root, text="8").grid(row=1, column=1, sticky="nsew")
button_9 = tk.Button(root, text="9").grid(row=1, column=2, sticky="nsew")
button_4 = tk.Button(root, text="4").grid(row=2, column=0, sticky="nsew")
button_5 = tk.Button(root, text="5").grid(row=2, column=1, sticky="nsew")
button_6 = tk.Button(root, text="6").grid(row=2, column=2, sticky="nsew")
button_1 = tk.Button(root, text="1").grid(row=3, column=0, sticky="nsew")
button_2 = tk.Button(root, text="2").grid(row=3, column=1, sticky="nsew")
button_3 = tk.Button(root, text="3").grid(row=3, column=2, sticky="nsew")
button_0 = tk.Button(root, text="0").grid(row=4, column=0, columnspan=2, sticky="nsew")
button_dot = tk.Button(root, text=".").grid(row=4, column=2, sticky="nsew")
button_add = tk.Button(root, text="+").grid(row=1, column=3, rowspan=2, sticky="nsew")


root.mainloop()
