# --------------- HORLOGE --------------

import tkinter as tk
import time
import math

WIDTH = 400
HEIGHT = 400

root = tk.Tk()
root.title("StimLink horloge")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


def horloge():
    canvas.delete("all")
    now = time.localtime()
    heure = now.tm_hour % 12
    minute = now.tm_min
    seconde = now.tm_sec
    canvas.create_oval(2, 2, WIDTH, HEIGHT, outline='black', width=2)

    for i in range(12):
        angle = i * math.pi/6 - math.pi/2
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(angle)

        if i == 0:
            canvas.create_text(x, y-10, text=str(i+12), font=('Arial', 12))
        else:
            canvas.create_text(x, y, text=str(i), font=('Arial', 12))

    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
        x2 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)

        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill='black', width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill='black', width=1)

    hour_angle = (heure + minute/60) * math.pi/6 - math.pi/2
    hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, hour_x, hour_y, fill='black', width=6)

    minute_angle = (heure + seconde / 60) * math.pi / 30 - math.pi / 2
    minute_x = WIDTH / 2 + 0.7 * WIDTH / 2 * math.cos(minute_angle)
    minute_y = HEIGHT / 2 + 0.7 * HEIGHT / 2 * math.sin(minute_angle)
    canvas.create_line(WIDTH / 2, HEIGHT / 2, minute_x, minute_y, fill='black', width=4)

    seconde_angle = seconde * math.pi / 30 - math.pi / 2
    seconde_x = WIDTH / 2 + 0.6 * WIDTH / 2 * math.cos(seconde_angle)
    seconde_y = HEIGHT / 2 + 0.6 * HEIGHT / 2 * math.sin(seconde_angle)
    canvas.create_line(WIDTH / 2, HEIGHT / 2, seconde_x, seconde_y, fill='yellow', width=2)


canvas.after(1000, horloge)
horloge()
root.mainloop()
