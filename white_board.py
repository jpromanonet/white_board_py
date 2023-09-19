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

# A function to draw in the screen
current_x = 0
current_y = 0
color = "black"

def locate_xy(work):

    global current_x, current_y

    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y

    canvas.create_line((current_x,current_y, work.x, work.y),width=get_current_value(), fill=color, capstyle=ROUND,smooth=TRUE)
    current_x,current_y = work.x, work.y

# Color picker
def show_color(new_color):
    global color
    color = new_color

# Eraser function (clean screen)
def new_canvas():

    canvas.delete('all')
    display_pallete()

# Icons and images

## Color bar
color_box = PhotoImage(file="./assets/side_bar.png")
Label(root, image=color_box,bg="#f2f3f5").place(x=10,y=20)

# Create the erase
eraser = PhotoImage(file="./assets/eraser.png")
Button(root, image=eraser, bg="#f2f3f5", command = new_canvas).place(x=30, y=400)

# Here we define the colors use sidebar
colors = Canvas(root, bg="#ffffff", width=37,height=300,bd=0)
colors.place(x=30, y=60)

# Let's create a function to display the color pallete
def display_pallete():
    # Black
    id = colors.create_rectangle((10,10,30,30), fill="black")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("black"))

    # Gray
    id = colors.create_rectangle((10,40,30,60), fill="gray")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("gray"))

    # Brown
    id = colors.create_rectangle((10,70,30,90), fill="brown")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("brown"))

    # Red
    id = colors.create_rectangle((10,100,30,120), fill="red")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("red"))

    # Orange
    id = colors.create_rectangle((10,130,30,150), fill="orange")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("orange"))

    # Yellow
    id = colors.create_rectangle((10,160,30,180), fill="yellow")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("yellow"))

    # Green
    id = colors.create_rectangle((10,190,30,210), fill="green")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("green"))

    # Blue
    id = colors.create_rectangle((10,220,30,240), fill="blue")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("blue"))

    # Purple
    id = colors.create_rectangle((10,250,30,270), fill="purple")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("purple"))

display_pallete()

# Here it goes the drawing canvas
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100,y=10)

# Now let's bind the canvas with the colors and buttons
canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", addLine)

# Line slider
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

current_value = tk.DoubleVar()
slider = ttk.Scale(root, from_=0, to=100,orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

## Value label
value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27,y=550)

# Run the app
root.mainloop()