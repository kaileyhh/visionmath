import cv2
import numpy as np

canvas_width = 320
canvas_height = 240

canvas = np.zeros((canvas_height,canvas_width,3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX


while(True):
    tape_x = int(input("x coord "))
    tape_y = int(input("y coord "))

    center_x = int(canvas_width/2)
    center_y = int(canvas_height/2)

    lime_color = (182, 255, 166)

    blue_color = (255, 0, 0)
    red_color = (0, 0, 255)


    cv2.circle(canvas, (tape_x, tape_y), 4, lime_color, -1)


    cv2.line(canvas, pt1=(tape_x + 10, tape_y), pt2=(center_x, tape_y), color=red_color, thickness=1)
    cv2.line(canvas, pt1=(tape_x, tape_y + 10), pt2=(tape_x, canvas_height), color=blue_color, thickness=1)

    x_text = "x_img = " + str(tape_x - center_x)
    y_text = "y_img = " + str(canvas_height - tape_y)

    x_text_org = (int((tape_x - (tape_x - center_x)/2) - 30), tape_y-5)
    y_text_org = (tape_x + 5, (int(tape_y + (canvas_height - tape_y)/2.0)))

    cv2.putText(canvas, x_text, x_text_org, font, 0.4, red_color, 1)
    cv2.putText(canvas, y_text, y_text_org, font, 0.4, blue_color, 1)

    cv2.imshow("image", canvas)
