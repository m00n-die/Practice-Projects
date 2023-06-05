"""A simple hello world application for Tkinter"""
import tkinter as tk


root = tk.Tk()
root.title("Hello world") #not in original code
label = tk.Label(root, text="Hello world!")
label.pack()
root.mainloop()