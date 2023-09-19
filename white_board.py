# First, let's import tkinter and some module for color manipulation and choosing
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

# Now, let's define the root and the windown configuration like title, size, etc
root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

# Run the app
root.mainloop()