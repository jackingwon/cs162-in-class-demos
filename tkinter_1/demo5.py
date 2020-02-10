#! /usr/bin/env python3.8
"""Button demo."""

# import tkinter and alias it
import tkinter as tk


def copy_text():
    txt = text_input.get(0.0, tk.END)
    text_output.config(state="normal")
    text_output.delete(0.0)
    text_output.insert(0.0, txt)
    text_output.config(state="disabled")


root = tk.Tk()
root.title("Textbox Demo")

input_label = tk.Label(root, text="Input:")
text_input = tk.Text(root, height=10, width=50)
input_label.pack(side=tk.TOP)
text_input.pack(side=tk.TOP)

copy_button = tk.Button(root, text="Copy", command=copy_text)
copy_button.pack()

output_label = tk.Label(root, text="Output:")
text_output = tk.Text(root, height=10, width=50, state="disabled")
output_label.pack(side=tk.TOP)
text_output.pack(side=tk.TOP)

# set up the main loop
root.mainloop()
