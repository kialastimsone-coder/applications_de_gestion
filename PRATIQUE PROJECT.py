# Créé par Lisa, le 14/10/2019
from tkinter import *
import tkinter as tk
from pylab import *
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


# Calcul de Ia
def Ia(Va, Suns, TaC):  # function Ia = Projet(Va,Suns,TaC)

    # Tension appliquée au panneau, ensoleillement et temperature
    # Ia = Projet(Va,G,T) = array voltage
    # Ia,Va = courant, tension appliquée
    # G = nombre de soleil (1 Soleil = 1000 W/mˆ2)
    # T = Tempétature en Deg C

    k = 1.38e-23  # Costante de  Boltzman
    q = 1.60e-19  # charge d'un electron

    # enter the following constants here, and the model will be
    # calculated based on these. for 1000W/mˆ2
    A = 1.2  # "diode quality" factor, =2 for crystaline, <2 for amorphous
    Vg = 1.12  # band gap voltage, 1.12eV for xtal Si, ˜1.75 for amorphous Si.
    Ns = 36  # number of series connected cells (diodes)

    T1 = 273 + 25
    Voc_T1 = 21.06 / Ns  # open cct voltage per cell at temperature T1
    Isc_T1 = 3.80  # short cct current per cell at temp T1

    T2 = 273 + 75
    Voc_T2 = 17.05 / Ns  # open cct voltage per cell at temperature T2
    Isc_T2 = 3.92  # short cct current per cell at temp T2

    TaK = 273 + TaC  # array working temp
    TrK = 273 + 25  # reference temp

    # when Va = 0, light generated current Iph_T1 = array short cct current
    # constant "a" can be determined from Isc vs T

    Iph_T1 = Isc_T1 * Suns
    a = (Isc_T2 - Isc_T1) / Isc_T1 * 1 / (T2 - T1)
    Iph = Iph_T1 * (1 + a * (TaK - T1))

    Vt_T1 = k * T1 / q  # = A * kT/q
    Ir_T1 = Isc_T1 / (exp(Voc_T1 / (A * Vt_T1)) - 1)
    Ir_T2 = Isc_T2 / (exp(Voc_T2 / (A * Vt_T1)) - 1)

    b = Vg * q / (A * k)
    Ir = Ir_T1 * (TaK / T1) ** (3 / A) * exp(-b * (1 / TaK - 1 / T1))

    X2v = Ir_T1 / (A * Vt_T1) * exp(Voc_T1 / (A * Vt_T1))
    dVdI_Voc = - 1.15 / Ns / 2  # dV/dI at Voc per cell –
    # from manufacturers graph
    Rs = - dVdI_Voc - 1 / X2v  # series resistance per cell

    # Ia = 0:0.01:Iph;
    Vt_Ta = A * 1.38e-23 * TaK / 1.60e-19  # =A*kT/q

    # Ia1 = Iph - Ir.*( exp((Vc+Ia.*Rs)./Vt_Ta) -1);
    # solve for Ia: f(Ia) = Iph - Ia - Ir.*( exp((Vc+Ia.*Rs)./Vt_Ta) -1) = 0;
    # Newton’s method: Ia2 = Ia1 - f(Ia1)/f’(Ia1)

    Vc = Va / Ns
    Ia = zeros(size(Vc))
    # Iav = Ia;
    for j in range(1, 5):
        Ia = Ia - (Iph - Ia - Ir * (exp((Vc + Ia * Rs) / Vt_Ta) - 1)) / (
                    -1 - (Ir * (exp((Vc + Ia * Rs) / Vt_Ta) - 1)) * Rs / Vt_Ta)
    # Iav = [Iav;Ia]; % to observe convergence for debugging.
    return Ia


# fonction pour recalculer le courant et la puissance et tracer le nouveau graph
def calcul():
    ensoleil = e1.get()  # on récupère l'ensoleillement
    temp = float(t1.get())  # on récupère la température
    rapp = float(r1.get())  # on récupère le rapport cyclique

    V = linspace(0, 30, 100)  # On prend une centaine de valeur de V entre 0 et 30
    # Le rapport cyclique entre 0 et 1

    Vref = V * rapp  # on multiplie la tension d'entrée par le rapport cyclique

    # ensoleillement entre 0 et 1
    Suns = ensoleil / 1000
    # température

    # I=f(v)
    Itemp1 = Ia(V, Suns, temp)
    I1 = Itemp1 / rapp

    # P=f(v)sans rapport cyclique
    P11 = V * Itemp1

    # P=f(v)avec rapport cyclique
    P1 = Vref * I1

    # tracer des courbes
    fig = Figure(figsize=(12, 8), dpi=60)
    a1 = fig.add_subplot(121)
    a1.plot(V, Itemp1)
    a1.plot(Vref, I1)
    a1.axes.set_ylim(0, 10)
    a1.axes.set_xlim(0, 30)
    a1.grid()

    a2 = fig.add_subplot(122)
    a2.plot(V, P11)
    a2.plot(Vref, P1)
    a2.axes.set_ylim(0, 100)
    a2.axes.set_xlim(0, 30)
    a2.grid()

    graph1 = FigureCanvasTkAgg(fig, root)
    canvas1 = graph1.get_tk_widget()
    canvas1.pack(side=LEFT)
    canvas1.place(x=40, y=50)
    canvas1.pack_propagate(False)

    labelx1 = Label(canvas1, text="Tension (en Volts)", bg='white')
    labelx1.pack(side=LEFT)
    labelx1.place(x=800, y=720)

    labelx2 = Label(canvas1, text="Tension (en Volts)", bg='white')
    labelx2.pack(side=LEFT)
    labelx2.place(x=300, y=720)

    labely1 = Label(canvas1, text="Courant \n(en Ampères)", bg='white')
    labely1.pack(side=LEFT)
    labely1.place(x=10, y=250)

    labely2 = Label(canvas1, text="Puissance\n(en Watt)", bg='white')
    labely2.pack(side=LEFT)
    labely2.place(x=550, y=250)


# ____programme principal/Interface_____#
# Création de la fenêtre principale
root = tk.Tk()
root.geometry('700x350')
root.title('Interface Homme-Machine')

# création d'un widget Frame dans la fenêtre principale pour l'ensoleillement et la température
Frame1 = Frame(root, width=380, height=240, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=10, pady=10)
Frame1.place(x=800, y=10)
Frame1.pack_propagate(False)  # permet de dimensionner le frame lorsqu'il contient des widgets

# On renomme le frame
Label(Frame1, text="Réglage de l'ensoleillement et de la température").pack(padx=10, pady=10)

# on met un scale horizontale et une entry dans le premier frame pour l'ensoleillement
e1 = IntVar()
e = tk.Entry(Frame1, textvariable=e1)
e.pack(side=LEFT, padx=5, pady=5)
e.place(x=240, y=35)
ensoleillement = Scale(Frame1, orient='horizontal', from_=0, to=1000, resolution=0, tickinterval=100, length=350,
                       variable=e1, label='Ensoleillement (W/m²)')
ensoleillement.pack(padx=10, pady=10)

# on met un deuxième scale horizontale et une entry dans le premier frame pour la température
t1 = DoubleVar()  # on definie t1 comme un float
t = tk.Entry(Frame1, textvariable=t1)
t.pack(side=LEFT, padx=5, pady=5)
t.place(x=240, y=135)
Temperature = Scale(Frame1, orient='horizontal', from_=0, to=100, resolution=0, tickinterval=10, length=350,
                    variable=t1, label='Température (°C)')
Temperature.pack(padx=10, pady=10)
Temperature.place(x=10, y=155)

# création d'un troisième widget Frame dans la fenêtre principale
Frame3 = Frame(root, width=380, height=140, borderwidth=2, relief=GROOVE)
Frame3.pack(side=LEFT, padx=10, pady=10)
Frame3.place(x=800, y=550)
Frame3.pack_propagate(False)  # permet de dimensionner le frame lorsqu'il contient des widgets

# On renomme le frame
Label(Frame3, text="Réglage du rapport cyclique du convertisseur Buck").pack(padx=10, pady=10)

# on met un scale horizontale et une entry dans le troisième frame pour le rapport cyclique
r1 = DoubleVar()
r = tk.Entry(Frame3, textvariable=r1)
r.pack(side=LEFT, padx=5, pady=5)
r.place(x=240, y=35)
Rapport = Scale(Frame3, orient='horizontal', from_=0, to=1, resolution=0.01, tickinterval=0.1, length=350, variable=r1,
                label='Rapport cyclique de Buck')
Rapport.pack(padx=10, pady=10)

# Bouton pour actualiser après avoir changé les valeurs
b1 = tk.Button(root, text='Actualiser', command=calcul)
b1.pack(side=LEFT, padx=10, pady=10)
b1.place(x=300, y=10)

b2 = tk.Button(root, text='Quitter', command=exit)
b2.pack()
b2.place(x=10, y=650)

tk.mainloop()
