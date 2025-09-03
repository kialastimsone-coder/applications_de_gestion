import tkinter as tk
from tkinter import *

root = tk.Tk()
root.config(bg="gray17")
root.geometry("400x350")
root.title("Expérience")


def Resultat():
    chemise = 18000
    basquet = 22000
    veste = 100000
    Lacoste = 12000
    result = int(entry.get())*chemise + int(entry1.get())*basquet + int(entry2.get())*veste + int(entry3.get())*Lacoste
    entryresultat.delete(0, END)
    entryresultat.insert(END, str(result)+" FC")


label = Label(root, text="Expérience 1", bg="gray17", fg="white", font=("Arial", 20, 'bold'))
label.place(x=130, y=30)

label1 = Label(root, text="Chemise", bg="gray16", fg="white", font=("Arial", 11))
label1.place(x=30, y=100)

entry = Entry(root, width=5, bg="gray10", fg="yellow", font=('Arial', 12))
entry.place(x=35, y=135)
entry.insert(END, 0)

label2 = Label(root, text="Basquet", bg="gray16", fg="white", font=("Arial", 11))
label2.place(x=120, y=100)

entry1 = Entry(root, width=5, bg="gray10", fg="yellow", font=('Arial', 12))
entry1.place(x=125, y=135)
entry1.insert(END, 0)

label3 = Label(root, text="Veste", bg="gray16", fg="white", font=("Arial", 12))
label3.place(x=205, y=100)

entry2 = Entry(root, width=5, bg="gray10", fg="yellow", font=('Arial', 12))
entry2.place(x=210, y=135)
entry2.insert(END, 0)

label4 = Label(root, text="Lacoste", bg="gray16", fg="white", font=("Arial", 12))
label4.place(x=300, y=100)

entry3 = Entry(root, width=5, bg="gray10", fg="yellow", font=('Arial', 12))
entry3.place(x=305, y=135)
entry3.insert(END, 0)

bouton = Button(root, text="Somme", width=10, bg="gray30", fg="gray16", font=('Arial', 12), command=Resultat)
bouton.place(x=270, y=210)

resultat = Label(root, text="Prix total", bg="gray15", fg="red", font=("Arial", 12, 'bold'))
resultat.place(x=62, y=195)

entryresultat = Entry(root, width=12, bg="gray10", fg="gold", font=('Arial', 12, 'bold'))
entryresultat.place(x=45, y=230)

periode = Label(root, text="Observation", bg="gray15", fg="blue", font=("Arial", 12, 'bold'))
periode.place(x=115, y=270)

entryperiode = Entry(root, width=22, bg="gray10", fg="white", font=('Arial', 11, 'bold'))
entryperiode.place(x=2, y=305)

entryperiode1 = Entry(root, width=25, bg="gray10", fg="white", font=('Arial', 9, 'bold'))
entryperiode1.place(x=190, y=305)

root.mainloop()
