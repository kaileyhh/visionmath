from re import X
import tkinter as tk
import numpy as np

tape_height = 4.8125
f = 284.772
phi = -2
x_img = 0
y_img = 0

def draw_dot(event):
    canvas.delete("all")
    input_canvas.delete("all")
    x1 = event.x
    x2 = event.x
    y1 = event.y
    y2 = event.y

    x_img = x1 - center_x
    y_img = canvas_height - y1

    canvas.create_oval(x1, y1, x2, y2, fill = "white", width = 4, outline="white")

    if (x1 < center_x and (center_x - x1 > 10)):
        canvas.create_line(x1+10, y1, center_x, y1, fill = "red", width = 3)

    elif (x1 - center_x > 10): 
        canvas.create_line(x1-10, y1, center_x, y1, fill = "red", width = 3)

    canvas.create_line(x1, y1+10, x1, canvas_height, fill = "blue", width = 3)

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
        print("hi")
        temp_y = np.tan(np.arctan(y_img / f) + phi * np.pi / 180) * f
        temp_y = canvas_height - temp_y

        canvas.create_text(x1, temp_y - 10, anchor = "center", font = ("Purisa", 10), text = ("virtual y_img"), fill = "white")

        canvas.create_oval(x1, temp_y, x1, temp_y, fill = "yellow", width = 4)
    
    elif (phi < 0):
        print("hi")
        temp_y = np.tan(np.arctan(y_img / f) + phi * np.pi / 180) * f
        temp_y = canvas_height - temp_y

        canvas.create_text(x1, temp_y + 10, anchor = "center", font = ("Purisa", 10), text = ("virtual y_img"), fill = "white")

        canvas.create_oval(x1, temp_y, x1, temp_y, fill = "yellow", width = 4)
    
    calculate_distance(x1, y1)


def calculate_distance(x1, y1):
    x_img = x1
    y_img = y1
    temp_atan = np.arctan(y_img / f)
    temp_atan = np.tan(temp_atan + phi*np.pi/180.0)
    distance = np.sqrt(np.power(tape_height/temp_atan, 2) + np.power(((tape_height*x_img)/(temp_atan*f)),2))
    input_canvas.create_text(10, 55, anchor = "w", font = ("Purisa", 10), text = ("distance = " + str(distance)))


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
canvas.pack()
input_canvas.pack()
top.mainloop()