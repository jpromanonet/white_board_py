import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import ttk

app = tk.Tk()
app.title("Drawing Canvas")
app.geometry("1050x570+150+50")
app.configure(bg="#f2f3f5")
app.resizable(False, False)

current_x = 0
current_y = 0
drawing_color = "black"

def update_current_position(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def draw_line(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), width=get_line_width(), fill=drawing_color, capstyle=tk.ROUND, smooth=True)
    current_x, current_y = event.x, event.y

def select_color(new_color):
    global drawing_color
    drawing_color = new_color

def clear_canvas():
    canvas.delete('all')
    display_color_palette()

color_box = tk.PhotoImage(file="./assets/side_bar.png")
color_box_label = tk.Label(app, image=color_box, bg="#f2f3f5")
color_box_label.place(x=10, y=20)

eraser = tk.PhotoImage(file="./assets/eraser.png")
eraser_button = tk.Button(app, image=eraser, bg="#f2f3f5", command=clear_canvas)
eraser_button.place(x=30, y=400)

colors = tk.Canvas(app, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_color_palette():
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
        color_id = colors.create_rectangle(10, 10 + i * 30, 30, 30 + i * 30, fill=fill_color)
        colors.tag_bind(color_id, "<Button-1>", lambda event, color=fill_color: select_color(color))

display_color_palette()

canvas = tk.Canvas(app, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind("<Button-1>", update_current_position)
canvas.bind("<B1-Motion>", draw_line)

def get_line_width():
    return '{:.2f}'.format(line_width_value.get())

def update_line_width_label(event):
    line_width_label.configure(text=get_line_width())

line_width_value = tk.DoubleVar()
line_width_slider = ttk.Scale(app, from_=0, to=100, orient='horizontal', command=update_line_width_label, variable=line_width_value)
line_width_slider.place(x=30, y=530)

line_width_label = ttk.Label(app, text=get_line_width())
line_width_label.place(x=27, y=550)

app.mainloop()
