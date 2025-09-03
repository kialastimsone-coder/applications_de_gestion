import sqlite3 as sq
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

con = sq.connect("Boutique.db")
DATA = pd.read_sql_query("SELECT * FROM Données", con)
fig = plt.figure("Situation financière")

sns.displot(data=DATA, x="Epices", kind="kde")
plt.title("COURBE DE VENTE")
plt.show()

"""
import secrets
import string

print('Welcome to Password generator by GeekyHumans!')

#input the length of password
length = int(input('\nEnter the length of password: '))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
# combine the data
all = lower + upper + num + symbols

#use secrets

password = ''.join(secrets.choice(all) for i in range(length))

#print the password
print(password)
"""
"""
# Temps instantané

import tkinter as tk  # Python 3.x
import time


# function which changes time on Label
def update_time():
    # change text on Label
    lbl['text'] = time.strftime('Current time: %H:%M:%S')

    # run `update_time` again after 1000ms (1s)
    root.after(1000, update_time)  # function name without ()


# create window
root = tk.Tk()
root.geometry('150x100')
root.config(bg='seaGreen')

# create label for current time
lbl = tk.Label(root, text='Current time: 00:00:00')
lbl.pack()

# run `update_time` first time after 1000ms (1s)
root.after(1000, update_time)  # function name without ()

# update_time() # or run first time immediately

# "start the engine"
root.mainloop()
"""

"""
from tkinter import *
from tkinter.ttk import *

ws = Tk()
Progress_Bar = Progressbar(ws, orient=HORIZONTAL, length=250, mode='determinate')


def Slide():
    import time
    Progress_Bar['value'] = 20
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 50
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 80
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 100


Progress_Bar.pack()
Button(ws, text='Run', command=Slide).pack(pady=10)
mainloop()
"""

"""
import tkinter
import time

Window_Width = 800

Window_Height = 600

Ball_Start_XPosition = 50

Ball_Start_YPosition = 50

Ball_Radius = 30

Ball_min_movement = 5

Refresh_Sec = 0.01


def create_animation_window():
    Window = tkinter.Tk()
    Window.title("Python Guides")

    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="Black")
    canvas.pack(fill="both", expand=True)
    return canvas


def animate_ball(Window, canvas, xinc, yinc):
    ball = canvas.create_oval(Ball_Start_XPosition - Ball_Radius,
                              Ball_Start_YPosition - Ball_Radius,
                              Ball_Start_XPosition + Ball_Radius,
                              Ball_Start_YPosition + Ball_Radius,
                              fill="seaGreen", outline="Black", width=4)
    while True:
        canvas.move(ball, xinc, yinc)
        Window.update()
        time.sleep(Refresh_Sec)
        ball_pos = canvas.coords(ball)
        # unpack array to variables
        al, bl, ar, br = ball_pos
        if al < abs(xinc) or ar > Window_Width - abs(xinc):
            xinc = -xinc
        if bl < abs(yinc) or br > Window_Height - abs(yinc):
            yinc = -yinc


Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)

"""
"""

import time
from tkinter import *
from tkinter import messagebox

ws = Tk()

ws.geometry("300x300")

ws.title("Python Guides")

Hour = StringVar()
Minute = StringVar()
Second = StringVar()

Hour.set("00")
Minute.set("00")
Second.set("00")

Hour_entry = Entry(ws, width=3, font=("Arial", 18, ""),
                   textvariable=Hour)
Hour_entry.place(x=80, y=20)

Minute_entry = Entry(ws, width=3, font=("Arial", 18, ""),
                     textvariable=Minute)
Minute_entry.place(x=130, y=20)

Second_entry = Entry(ws, width=3, font=("Arial", 18, ""),
                     textvariable=Second)
Second_entry.place(x=180, y=20)


def OK():
    try:

        temp = int(Hour.get()) * 3600 + int(Minute.get()) * 60 + int(Second.get())
    except:
        print("Please Input The Correct Value")
    while temp > -1:

        Mins, Secs = divmod(temp, 60)

        Hours = 0
        if Mins > 60:
            Hours, Mins = divmod(Mins, 60)

        Hour.set("{0:2d}".format(Hours))
        Minute.set("{0:2d}".format(Mins))
        Second.set("{0:2d}".format(Secs))

        ws.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time up ")

        temp -= 1


button = Button(ws, text=' countdown', bd='5',
                command=OK)
button.place(x=100, y=110)

ws.mainloop()
"""

"""
from matplotlib import pyplot as plt
plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50000, 40000, 70000, 80000, 200000], label="MAC", color='r', width=.4)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80000, 20000, 20000, 50000, 60000], label="Dominos", color='b', width=.4)
plt.legend(loc='upper right')
plt.xlabel('Months')
plt.ylabel('Sales Amount')
plt.title('Information')
plt.show()
"""

"""
from tkinter import *
import random


def gen_color():
    ws.configure(background=random.choice(["black", "red", "green", "blue", "yellow", "seaGreen"]))


ws = Tk()
ws.title("Python Guides")
ws.geometry('500x500')

Button(ws, text='Click Me', command=gen_color).pack()
ws.mainloop()
"""
"""
from tkinter import *

ws = Tk()
ws.title("Python Guides")


def convert():
    if a1['state'] == NORMAL:
        a1["state"] = DISABLED
        a2["text"] = "enable"
    elif a1['state'] == DISABLED:
        a1["state"] = NORMAL
        a2["text"] = "disable"


# --Buttons
a1 = Button(ws, text="button")
a1.config(height=8, width=9)
a1.grid(row=0, column=0)
a2 = Button(text="disable", command=convert)
a2.grid(row=0, column=1)
ws.mainloop()
"""

"""
from tkinter import Tk, Canvas

root = Tk()
cnv = Canvas(root, width=180, height=100)
cnv.pack()

cnv.create_rectangle(20, 20, 80, 80, fill='red', outline='')

def dessiner(c):
    cnv.create_rectangle(100, 20, 100+c, 20+c, fill='blue', outline='')

cnv.after(1000, dessiner, 42)

root.mainloop()
"""
"""
from tkinter import Tk, Canvas, Button
from random import randrange

def anim(cpt):
    global id_anim
    cnv.delete("all")
    cnv.create_text(SIDE//2, SIDE//2, text =int(cpt), font="Arial 200 bold")
    id_anim = cnv.after(500, anim, cpt+1)

def go():
    cnv.after_cancel(id_anim)
    anim(1)

SIDE = 400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.pack()
btn = Button(root, text="Reset", command=go)
btn.pack()

id_anim = None
anim(1)

root.mainloop()
"""
"""
import numpy as np
import cv2
from keras.models import Model, Sequential
from keras.layers import Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from PIL import Image

from keras.applications.imagenet_utils import preprocess_input
from keras.preprocessing import image
import matplotlib.pyplot as plt
from keras.models import model_from_json
from os import listdir


def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (160, 160))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    img /= 127.5
    img -= 1

    return img


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class InceptionResNetV1:
    pass


model = InceptionResNetV1()
print("model built")
model.load_weights('facenet_weights.h5')
print("weights loaded")


def findEuclideanDistance(source_representation, test_representation, euclidiean_distance=None):
    euclidean_distance = source_representation - test_representation
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidiean_distance))
    euclidean_distance = np.sqrt(euclidean_distance)

    return euclidean_distance

threshhold = 21

employee_pictures = "database/"

employees = dict()

for file in listdir(employee_pictures):
    employee, extension = file.split(".")
    img = preprocess_image('database/%s.jpg' % (employee))
    representation = model.predict(img)[0, :]

    employees[employee] = representation

print("employee representations retrieved successfully")

cap = cv2.VideoCapture(0)  # webcam

while (True):
    ret, img = cap.read()

    for (x, y, w, h) in faces:
        if w > 130:  # discard small detected faces
            cv2.rectangle(img, (x, y), (x + w, y + h), (67, 67, 67), 1)  # draw rectangle to main image

            detected_face = img[int(y):int(y + h), int(x):int(x + w)]
            detected_face = cv2.resize(detected_face, (160, 160))

            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis=0)

            img_pixels /= 127.5
            img_pixels -= 1

            captured_representation = model.predict(img_pixels)[0, :]

    distances = []

    for i in employees:
        employee_name = i
        source_representation = employees[i]

        distance = findEuclideanDistance(captured_representation, source_representation)

        distances.append(distance)

    label_name = 'unknown'
    index = 0
    for i in employees:
        employee_name = i
        if index == np.argmin(distances):
            if distances[index] <= threshold:

                similarity = 100 - (20 - distance)
                if similarity > 99.99: similarity = 99.99

                label_name = "%s (%s%s)" % (employee_name, str(round(similarity, 2)), '%')

                break

        index = index + 1
        cv2.putText(img, label_name, (int(x + w + 15), int(y - 64)), cv2.FONT_HERSHEY_SIMPLEX, 1, (67, 67, 67), 2)

        cv2.line(img, (x + w, y - 64), (x + w - 25, y - 64), (67, 67, 67), 1)
        cv2.line(img, (int(x + w / 2), y), (x + w - 25, y - 64), (67, 67, 67), 1)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break

cap.release()
cv2.destroyAllWindows()
"""
"""
import tkinter as tk
import random as rd


class AppliBaballe(tk.Tk):
    def __init__(self):
        # Constructeur de l'application.
        tk.Tk.__init__(self)
        # Coord baballe.
        self.x, self.y = 200, 200
        # Rayon baballe.
        self.size = 50
        # Pas de deplacement.
        self.dx, self.dy = 20, 20
        # Création et packing du canvas.
        self.canv = tk.Canvas(self, bg='light gray', height=400, width=400)
        self.canv.pack()
        # Création de la baballe.
        self.baballe = self.canv.create_oval(self.x, self.y,
                                             self.x+self.size,
                                             self.y+self.size,
                                             width=2, fill="blue")
        # Binding des actions.
        self.canv.bind("<Button-1>", self.incr)
        self.canv.bind("<Button-2>", self.boom)
        self.canv.bind("<Button-3>", self.decr)
        self.bind("<Escape>", self.stop)
        # Lancer la baballe.
        self.move()

    def move(self):
        # Déplace la baballe (appelée itérativement avec la méthode after).
        # Incrémente coord baballe.
        self.x += self.dx
        self.y += self.dy
        # Vérifier que la baballe ne sort pas du canvas (choc élastique).
        if self.x < 10:
            self.dx = abs(self.dx)
        if self.x > 400-self.size-10:
            self.dx = -abs(self.dx)
        if self.y < 10:
            self.dy = abs(self.dy)
        if self.y > 400-self.size-10:
            self.dy = -abs(self.dy)
        # Mise à jour des coord.
        self.canv.coords(self.baballe, self.x, self.y, self.x+self.size,
                         self.y+self.size)
        # Rappel de move toutes les 50ms.
        self.after(50, self.move)

    def boom(self, mclick):
        # Relance la baballe dans une direction aléatoire au point du clic.
        self.x = mclick.x
        self.y = mclick.y
        self.canv.create_text(self.x, self.y, text="Boom !", fill="red")
        self.dx = rd.choice([-30, -20, -10, 10, 20, 30])
        self.dy = rd.choice([-30, -20, -10, 10, 20, 30])

    def incr(self, lclick):
        # Augmente la taille de la baballe.
        self.size += 10
        if self.size > 200:
            self.size = 200

    def decr(self, rclick):
        # Diminue la taille de la baballe.
        self.size -= 10
        if self.size < 10:
            self.size = 10

    def stop(self, esc):
        # Quitte l'application.
        self.quit()

if __name__ == "__main__":
    myapp = AppliBaballe()
    myapp.title("Baballe !")
    myapp.mainloop()
"""

"""
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

plt.axes(xlim=(0, 2), ylim=(-2, 2))
fig = plt.Figure(dpi=100)
ax = fig.add_subplot(xlim=(0, 2), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button = tkinter.Button(master=root, text="Quit", command=root.quit)
button.pack(side=tkinter.BOTTOM)

toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

tkinter.mainloop()
"""