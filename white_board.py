import tkinter as tk
from tkinter import PhotoImage, Canvas, Button
from tkinter.colorchooser import askcolor
from tkinter import ttk

root = tk.Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = "black"

def locate_xy(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def addLine(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), width=get_current_value(), fill=color, capstyle=tk.ROUND, smooth=True)
    current_x, current_y = event.x, event.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_palette()

color_box = PhotoImage(file="./assets/side_bar.png")
label_color_box = tk.Label(root, image=color_box, bg="#f2f3f5")
label_color_box.place(x=10, y=20)

eraser = PhotoImage(file="./assets/eraser.png")
button_eraser = Button(root, image=eraser, bg="#f2f3f5", command=new_canvas)
button_eraser.place(x=30, y=400)

colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    color_data = {
        "Black": "black",
        "Gray": "gray",
        "Brown": "brown",
        "Red": "red",
        "Orange": "orange",
        "Yellow": "yellow",
        "Green": "green",
        "Blue": "blue",
        "Purple": "purple"
    }

    for i, (color_name, fill_color) in enumerate(color_data.items()):
        id = colors.create_rectangle(10, 10 + i * 30, 30, 30 + i * 30, fill=fill_color)
        colors.tag_bind(id, "<Button-1>", lambda event, color=fill_color: show_color(color))

display_palette()

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", addLine)

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

current_value = tk.DoubleVar()
slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()
