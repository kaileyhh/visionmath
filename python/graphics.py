import tkinter as tk
import numpy as np
from collections import namedtuple

default_height = tape_height = 4.8125
default_f = f = 284.772
default_phi = phi = -2
x_img = 0
y_img = 0

x1 = None
y1 = None

def draw_dot(event):
    global x1
    global y1
    canvas.delete("all")
    input_canvas.delete("all")

    canvas.create_line(center_x - 5, center_y, center_x + 5, center_y, fill = "green", width = 3)
    canvas.create_line(center_x, center_y - 5, center_x, center_y + 5, fill = "green", width = 3)


    x1 = event.x
    x2 = event.x
    y1 = event.y
    y2 = event.y

    x_img = x1 - center_x
    y_img = canvas_height - y1

    canvas.create_oval(x1 - 3, y1 - 3, x2 + 3, y2 + 3, fill = "lime green", width = 0, outline="white")

    if (x1 < center_x and (center_x - x1 > 10)):
        canvas.create_line(x1+5, y1, center_x, y1, fill = "red", width = 3)

    elif (x1 - center_x > 10): 
        canvas.create_line(x1-5, y1, center_x, y1, fill = "red", width = 3)

    canvas.create_line(x1, y1+5, x1, canvas_height, fill = "blue", width = 3)

    if (x1 < 240):
        canvas.create_text(x1+7, (int(y1 + (canvas_height - y1)/2)), anchor="w", font=("Purisa", 10),
            text=("y_img = " + str(y_img)), fill="blue")
    else:
        canvas.create_text(x1-7, (int(y1 + (canvas_height - y1)/2)), anchor="e", font=("Purisa", 10),
            text=("y_img = " + str(y_img)), fill="blue")
    
    

    canvas.create_text(int((x1 - (x1 - center_x)/2)), y1 - 7, anchor="center", font=("Purisa", 10),
            text=("x_img = " + str(x_img)), fill="red")

    

    input_canvas.create_text(10, 10, anchor="w", font=("Purisa", 10),
            text=("height = " + str(tape_height)), fill="white")
    input_canvas.create_text(10, 25, anchor="w", font=("Purisa", 10),
            text=("focal length = " + str(f)), fill="white")
    input_canvas.create_text(10, 40, anchor="w", font=("Purisa", 10),
            text=("limelight tilt up = " + str(phi)), fill="white")
    
    if (phi > 0):
        temp_y = np.tan(np.arctan(y_img / f) + phi * np.pi / 180) * f

        input_canvas.create_text(10, 85, anchor = "w", font = ("Purisa", 10), text = ("virtual y = " + str(temp_y)), fill = "white")


        temp_y = canvas_height - temp_y

        canvas.create_text(x1, temp_y - 10, anchor = "center", font = ("Purisa", 10), text = ("virtual y_img"), fill = "white")

        canvas.create_oval(x1 - 3, temp_y - 3, x1 + 3, temp_y + 3, fill = "yellow", width = 0)

    
    elif (phi < 0):
        temp_y = np.tan(np.arctan(y_img / f) + phi * np.pi / 180) * f

        input_canvas.create_text(10, 85, anchor = "w", font = ("Purisa", 10), text = ("virtual y = " + str(temp_y)), fill = "white")

        temp_y = canvas_height - temp_y

        canvas.create_text(x1, temp_y + 10, anchor = "center", font = ("Purisa", 10), text = ("virtual y_img"), fill = "white")

        canvas.create_oval(x1 - 3, temp_y - 3, x1 + 3, temp_y + 3, fill = "yellow", width = 0)
        
    else:
        input_canvas.create_text(10, 85, anchor = "w", font = ("Purisa", 10), text = ("no virtual y"), fill = "white")
    
    calculate_distance(x1, y1)


def calculate_distance(x1, y1):
    x_img = x1 - center_x
    y_img = canvas_height - y1



    temp_atan = np.arctan(y_img / f)
    temp_atan = np.tan(temp_atan + phi*np.pi/180.0)
    distance = np.sqrt(np.power(tape_height/temp_atan, 2) + np.power(((tape_height*x_img)/(temp_atan*f)),2))
    input_canvas.create_text(10, 55, anchor = "w", font = ("Purisa", 10), text = ("distance = " + str(distance)), fill = "white")

    if (phi > 0):
        temp_y = np.tan(np.arctan(y_img / f) + phi * np.pi / 180) * f
        y_img = temp_y

    angle = np.arcsin(x_img * tape_height / (y_img * distance)) * 180 / np.pi

    input_canvas.create_text(10, 70, anchor = "w", font = ("Purisa", 10), text = ("angle = " + str(angle)), fill = "white")


# def get_height():
#     tape_height = heightge.get("1.0", "end")
    
lime_color = (182, 255, 166)

blue_color = (255, 0, 0)
red_color = (0, 0, 255)
black_color = (255, 255, 255)
white_color = (0, 0, 0)

canvas_width = 320
canvas_height = 240

center_x = int(canvas_width / 2)
center_y = int(canvas_height / 2)

top = tk.Tk()

canvas = tk.Canvas(top, bg="black", cursor="arrow", width = canvas_width, height=canvas_height)

input_canvas = tk.Canvas(top, bg="black", cursor="arrow", width = canvas_width, height = 100)

canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', draw_dot)
click_num=0




# heightge=tk.Text(input_canvas, height=2, width=10)
# heightge.pack()
# buttonCommit=tk.Button(input_canvas, height=1, width=10, text="Commit", 
#                     command=lambda: calculate_distance())

# buttonCommit.pack()

frame = tk.Frame(top)
select = tk.StringVar()
select.set("height")
menu = tk.OptionMenu(frame, select, "height", "focal length", "tilt", "reset all")
input = tk.Entry(frame)

def update():
    global tape_height
    global f
    global phi
    option = select.get()
    if option != "reset all":
        try:
            value = float(input.get())
        except Exception:
            return

    if option == "height":
        tape_height = value
    elif option == "focal length":
        f = value
    elif option == "tilt":
        phi = value
    else:
        tape_height = default_height
        f = default_f
        phi = default_phi

    FakeEvent = namedtuple("Event", ["x", "y"])

    draw_dot(FakeEvent(x1, y1))

button = tk.Button(frame, text="Update", command=update)


canvas.pack()
input_canvas.pack()
menu.grid(row=0, column=0)
input.grid(row=0, column=1)
button.grid(row=0, column=2)
frame.pack()
top.mainloop()
