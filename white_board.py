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

# Icons and images

## Color bar
color_box = PhotoImage(file="./assets/side_bar.png")
Label(root, image=color_box,bg="#f2f3f5").place(x=10,y=20)

# Create the erase
eraser = PhotoImage(file="./assets/eraser.png")
Button(root, image=eraser, bg="#f2f3f5").place(x=30, y=400)

# Here we define the colors use sidebar
colors = Canvas(root, bg="#ffffff", width=37,height=300,bd=0)
colors.place(x=30, y=60)

# Here it goes the drawing canvas
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100,y=10)

# Now let's bind the canvas with the colors and buttons
canvas.bind("<Button-1>")
canvas.bind("<B1-Motion>")

# Run the app
root.mainloop()