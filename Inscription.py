import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


def enregistrer():
    messagebox.showinfo("Enregistement", "Inscription approuvée")


def supprimer():
    quit()


app = ttk.Window(themename="darkly")
app.geometry("600x700")
app.title("INSCRIPTION")

label = ttk.Label(app, text="Formulaire d'inscription")
label.pack(pady=30)
label.config(font=("Arial", 25, 'bold'))

nom = ttk.Frame(app)
nom.pack(pady=15, padx=10, fill="x")
ttk.Label(nom, text="Nom        ").pack(side="left", padx=5)
ENTRY1 = ttk.Entry(nom).pack(side="left", fill="x", padx=5)

post = ttk.Frame(app)
post.pack(pady=15, padx=10, fill="x")
ttk.Label(post, text="Post-nom").pack(side="left", padx=5)
ttk.Entry(post).pack(side="left", fill="x", padx=5)

prenom = ttk.Frame(app)
prenom.pack(pady=15, padx=10, fill="x")
ttk.Label(prenom, text="Prénom   ").pack(side="left", padx=5)
ttk.Entry(prenom).pack(side="left", fill="x", padx=5)

numero = ttk.Frame(app)
numero.pack(pady=15, padx=10, fill="x")
ttk.Label(numero, text="Numéro tutilaire").pack(side="left", padx=5)
ttk.Entry(numero).pack(side="left", fill="x", padx=5)

adresse = ttk.Frame(app)
adresse.pack(pady=15, padx=10, fill="x")
ttk.Label(adresse, text="Adresse").pack(side="left", padx=5)
ttk.Entry(adresse).pack(side="left", fill="x", padx=10)

CbxEtcivil = ["Marié(e)", "Célibataire", "Divorcé(e)", "Veuf(ve)"]
EtCivil = ttk.Frame(app)
EtCivil.pack(pady=15, padx=10, fill="x")
ttk.Label(EtCivil, text="Etat civil").pack(side="left", padx=5)
ttk.Combobox(EtCivil, values=CbxEtcivil).pack(side="left", fill="x", padx=5)

sexe = ttk.Frame(app)
sexe.pack(pady=15, padx=10, fill="x")
ttk.Label(sexe, text="Sexe :").pack(side="left", padx=5)
ttk.Label(sexe, text="Homme").pack(side="left", padx=5)
ttk.Radiobutton(sexe, value=0).pack(side="left")

ttk.Label(sexe, text="Femme").pack(side="left", padx=5)
ttk.Radiobutton(sexe).pack(side="left")

ckbutton = ttk.Frame(app)
ckbutton.pack(pady=15, padx=10, fill="x")
ttk.Checkbutton(ckbutton, bootstyle="round-toggle", text="Garder l'info ?").pack(side="left", padx=10)

button = ttk.Frame(app)
button.pack(pady=15, padx=10, fill="x")
ttk.Button(button, text="Enregistrer", bootstyle=SUCCESS, command=enregistrer).pack(side="left", padx=10)
ttk.Button(button, text="Quitter", bootstyle=SECONDARY, command=supprimer).pack(side="left", padx=10)



app.mainloop()
