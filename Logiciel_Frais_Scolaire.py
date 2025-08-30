import datetime
import os
import pathlib
import random
import smtplib
import tempfile
from datetime import date
import openpyxl
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq

reste = 0

# ----------- Creation de la base des données ----------------
"""
con = sq.connect("PAIEMENT 2023-2024 DataBase.db")
c = con.cursor()
c.execute("CREATE TABLE Frais_scolaire(N° primary key, Nom text, PostNom text, Classe text, Motif text, Semestre numeric, Montant numeric, Reste numeric, Date text)")
c.execute("CREATE TABLE Frais_inscription(N° primary key, Nom text, PostNom text, Classe text, Motif text, Montant numeric, Date text)")
c.execute("CREATE TABLE Frais_OrgaMat(N° primary key, Nom text, PostNom text, Classe text, Motif text, Montant numeric, Date text)")
c.execute("CREATE TABLE Fourniture(N° primary key, Nom text, PostNom text, Classe text, Motif text, Montant numeric, Date text)")

con.close()
"""


def valider():
    global reste
    global time
    time = datetime.datetime.now().strftime("%H:%M:%S")
    if persoEnrty.get() == "":
        messagebox.showinfo('Attention', "Fixez le montant à payer !")
    else:
        if entryprc.get() == '' and entryrst.get() == '':
            messagebox.showwarning("Vide", "Inserez le montant perçu !!!")
            entryrst.delete(0, END)
            entryrst.insert(END, '')
        else:
            reste = int(persoEnrty.get()) - int(entryprc.get())
            entryrst.delete(0, END)
            entryrst.insert(0, str(reste))
            DOLLAR = round(reste / 2400, 2)
            entryrst1.delete(0, END)
            entryrst1.insert(0, str(DOLLAR))


def apercu():
    if entryname.get() == "":
        messagebox.showinfo("Info", "Inserez le nom !")

    elif entrypostname.get() == '' or entrynumber.get() == '' or entrySemestre.get() == '' or entryprc.get() == '':
        messagebox.showwarning('Attention', "Remplissage incomplète !")
    elif entryname.get().isdigit():
        messagebox.showerror('Erreur', "Format invalide !")
    elif entrypostname.get().isdigit():
        messagebox.showerror('Erreur', "Format invalide !")
    elif not entryname.get().istitle():
        messagebox.showerror('Erreur', "La première lettre du nom doit etre en majuscule !")
    elif not entrypostname.get().istitle():
        messagebox.showerror('Erreur', 'La première lettre du post-nom doit etre en majuscule !')
    else:
        if entryIntitule.get() == "Frais scolaire" and entrySemestre.get() == "-":
            messagebox.showwarning("Attention", "Precisez le semestre !")
        else:
            texteAp.insert(END,
                           f"  ________________________________________________________ \n*                                                          *")
            texteAp.insert(END, f"\n*                NOM DE L'ETABLISSEMENT                    *")
            texteAp.insert(END, f"\n* ________________________________________________________ *")
            texteAp.insert(END, f"\n*                                   Heure : {time}   ")
            texteAp.insert(END, f"\n*                                   Date  : {Aujourdhui}  ")
            texteAp.insert(END, f"\n*   N° Récu    : {AleaNumber}                            ")
            texteAp.insert(END, f"\n*   Noms       : {entryname.get()} - {entrypostname.get()}")
            texteAp.insert(END, f"\n*   Classe     : {entrynumber.get()}    ")
            texteAp.insert(END, f"\n* ________________________________________________________  ")
            texteAp.insert(END, f"\n*                                                           ")
            if entryIntitule.get() == "Inscription":
                texteAp.insert(END, f"\n*                      ---                              ")
            elif entryIntitule.get() == "Fourniture":
                texteAp.insert(END, f"\n*                      ---                              ")
            elif entryIntitule.get() == "OrgaMat":
                texteAp.insert(END, f"\n*                      ---                              ")
            else:
                texteAp.insert(END, f"\n*                    Semestre {entrySemestre.get()}     ")
            texteAp.insert(END, f"\n*                                                           ")
            texteAp.insert(END, f"\n*   Intitule   :   {entryIntitule.get()}                    ")
            texteAp.insert(END, f"\n*   Montant    :   {entryprc.get()} FC           ")
            if entryIntitule.get() == "Inscription":
                texteAp.insert(END, f"\n*                                          ")
            elif entryIntitule.get() == "Fourniture":
                texteAp.insert(END, f"\n*                                          ")
            elif entryIntitule.get() == "OrgaMat":
                texteAp.insert(END, f"\n*                                          ")
            elif entryIntitule.get() == "Frais scolaire" and entryprc.get() == persoEnrty.get():
                texteAp.insert(END, f"\n\n*             SOLDE FRAIS {entrySemestre.get()}e Semestre ")
            else:
                texteAp.insert(END, f"\n*   Reste      :   {entryrst.get() } FC ({entryrst1.get()} $) ")
            texteAp.insert(END, f"\n* ________________________________________________________  ")
            texteAp.insert(END, f"\n*                                                          *")
            texteAp.insert(END, f"\n*                                               Signature  *")
            texteAp.insert(END, f"\n* Copyright_StimLink@2023                                  *")
            texteAp.insert(END, f"\n* -------------------------------------------------------- *")


def restauration():
    if entryname.get() == '' and entrynumber.get() == '' and entrySemestre.get() == '' and entryprc.get() == '' \
            and entryrst.get() == '' and entryNUM.get() == '' and EntryNOM.get() == "":
        messagebox.showinfo("Restauration", "Il n'y a rien à restaurer présentement !")
    else:
        message = messagebox.askyesno('Restauration', 'Voulez-vous restauré les données de la page ?')
        if message:
            entryname.delete(0, END)
            entrypostname.delete(0, END)
            entrynumber.delete(0, END)
            entryNUM.delete(0, END)
            entryrst.delete(0, END)
            entryrst1.delete(0, END)
            entryprc.delete(0, END)
            texteAp.delete(1.0, END)

            EntryNOM.delete(0, END)
            EntryPOST.delete(0, END)
            EntryCLASSE.delete(0, END)
            EntryINTITULE.delete(0, END)
            EntrySMSTRE.delete(0, END)
            EntryMNTN.delete(0, END)
            EntryRST.delete(0, END)
            EntryNUM.delete(0, END)


AleaNumber = random.randint(10000, 19999)


def enregistrement():
    global AleaNumber
    global table
    numero = AleaNumber
    noms = entryname.get()
    post = entrypostname.get()
    classe = entrynumber.get()
    motif = entryIntitule.get()
    semestre = entrySemestre.get()
    percu = entryprc.get()
    reste = entryrst.get()
    Date = Aujourdhui

    if entryname.get() == '' and entrynumber.get() == '' and entrySemestre.get() == '' and entryrst.get() == '':
        messagebox.showwarning('ENREGISTREMENT', "Il n'y a rien à enregistrer !")

    else:
        if entryIntitule.get() == "Frais scolaire":
            con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
            cuser = con.cursor()
            cuser.execute(
                "insert into Frais_scolaire ('N°', 'Nom', 'PostNom', 'Classe', 'Motif', 'Semestre', 'Montant', 'Reste', 'Date')"
                " values (?,?,?,?,?,?,?,?,?)", (numero, noms, post, classe, motif, semestre, percu, reste, Date))
            con.commit()
            con.close()
            messagebox.showinfo("ENREGISTREMENT", "Enregistrer avec succès !")
            con.close()

            newenreg = texteAp.get(1.0, END)
            file = open(f'FRAIS_SCOLAIRE_2023-2024/{AleaNumber}.txt', 'w')
            file.write(newenreg)
            file.close()
            AleaNumber = random.randint(10000, 19999)

            con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
            cuser = con.cursor()
            select = cuser.execute("select * from Frais_scolaire")
            for row in select:
                table.insert("", END, values=row)
            con.close()

        elif entryIntitule.get() == "Inscription":
            con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
            cuser = con.cursor()
            cuser.execute(
                "insert into Frais_inscription ('N°', 'Nom', 'PostNom', 'Classe', 'Motif', 'Montant', 'Date')"
                " values (?,?,?,?,?,?,?)", (numero, noms, post, classe, motif, percu, Date))
            con.commit()
            con.close()
            messagebox.showinfo("ENREGISTREMENT", "Enregistrer avec succès !")
            con.close()

            newenreg = texteAp.get(1.0, END)
            file = open(f'FRAIS_INSCRIPTION_2023-2024/{AleaNumber}.txt', 'w')
            file.write(newenreg)
            file.close()
            AleaNumber = random.randint(10000, 19999)

        elif entryIntitule.get() == "Fourniture":
            con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
            cuser = con.cursor()
            cuser.execute(
                "insert into Fourniture ('N°', 'Nom', 'PostNom', 'Classe', 'Motif', 'Montant', 'Date')"
                " values (?,?,?,?,?,?,?)", (numero, noms, post, classe, motif, percu, Date))
            con.commit()
            con.close()
            messagebox.showinfo("ENREGISTREMENT", "Enregistrer avec succès !")
            con.close()

            newenreg = texteAp.get(1.0, END)
            file = open(f'FOURNITURE_2023-2024/{AleaNumber}.txt', 'w')
            file.write(newenreg)
            file.close()
            AleaNumber = random.randint(10000, 19999)

        elif entryIntitule.get() == "OrgaMat":
            con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
            cuser = con.cursor()
            cuser.execute(
                "insert into Frais_OrgaMat ('N°', 'Nom', 'PostNom', 'Classe', 'Motif', 'Montant', 'Date')"
                " values (?,?,?,?,?,?,?)", (numero, noms, post, classe, motif, percu, Date))
            con.commit()
            con.close()
            messagebox.showinfo("ENREGISTREMENT", "Enregistrer avec succès !")
            con.close()

            newenreg = texteAp.get(1.0, END)
            file = open(f'FRAIS_ORGAMAT_2023-2024/{AleaNumber}.txt', 'w')
            file.write(newenreg)
            file.close()
            AleaNumber = random.randint(10000, 19999)

        entryname.delete(0, END)
        entrypostname.delete(0, END)
        entrynumber.delete(0, END)
        entryNUM.delete(0, END)
        entryrst.delete(0, END)
        entryrst1.delete(0, END)
        entryprc.delete(0, END)
        texteAp.delete(1.0, END)


def actualiser(event):
    global AleaNumber
    today = date.today()
    Aujourdhui = today.strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    EntryNOM.delete(0, END)
    EntryPOST.delete(0, END)
    EntryCLASSE.delete(0, END)
    EntryINTITULE.delete(0, END)
    EntrySMSTRE.delete(0, END)
    EntryMNTN.delete(0, END)
    EntryRST.delete(0, END)
    EntryNUM.delete(0, END)
    texteAp.delete(1.0, END)
    selected = table.focus()
    donnee = table.item(selected)
    row = donnee["values"]

    EntryNUM.insert(0, row[0])
    EntryNOM.insert(0, row[1])
    EntryPOST.insert(0, row[2])
    EntryCLASSE.insert(0, row[3])
    EntrySMSTRE.insert(0, row[4])
    EntryINTITULE.insert(0, row[5])
    EntryMNTN.insert(0, row[6])
    EntryRST.insert(0, row[7])


def modification():

    if persoEnrty.get() == "":
        messagebox.showerror("Impossible", "Fixé le frais scolaire !")
    elif EntryNUM.get() == "":
        messagebox.showerror("Impossible", "Selectionner les données à modifiées !")
    else:
        num = EntryNUM.get()
        nom = EntryNOM.get()
        post = EntryPOST.get()
        classe = EntryCLASSE.get()
        intitule = EntryINTITULE.get()
        semestre = EntrySMSTRE.get()
        montant = EntryMNTN.get()
        reste = int(persoEnrty.get()) - int(EntryMNTN.get())
        EntryRST.delete(0, END)
        Reste = EntryRST.insert(0, str(reste) + " FC")

        con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
        cuser = con.cursor()

        news = [num, nom, post, classe, intitule, semestre, montant, Reste]
        cuser.execute("UPDATE Frais_scolaire set Nom=?, PostNom=?, Classe=?, Motif=?, Semestre=?, Montant=?, Reste=? "
                      "WHERE N°=?", news)
        con.commit()
        messagebox.showinfo("Modification", "Donnée modifier avec succès...")

        con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
        cuser = con.cursor()
        select = cuser.execute("select * from Frais_scolaire")
        for row in select:
            table.insert("", END, values=row)

        con.close()


def recherche():
    if entryNUM.get() == "":
        messagebox.showerror("Not insert", "Inserez le numéro du reçu")
    else:
        for i in os.listdir('FRAIS_SCOLAIRE_2023-2024/'):
            if i.split('.')[0] == entryNUM.get():
                f = open(f'FRAIS_SCOLAIRE_2023-2024/{i}', 'r')
                texteAp.delete(1.0, END)
                for data in f:
                    texteAp.insert(END, data)
                f.close()
                break
        else:
            messagebox.showerror('Erreur', 'N° Réçu incorrect')
            entryNUM.delete(0, END)


def imprimer():
    if texteAp.get(1.0, END) == '\n':
        messagebox.showwarning('Impression', "Il n'y a aucun réçu à imprimer !")
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(texteAp.get(1.0, END))
        os.startfile(file, 'print')


if not os.path.exists('FRAIS_SCOLAIRE_2023-2024'):
    os.mkdir('FRAIS_SCOLAIRE_2023-2024')

if not os.path.exists('FRAIS_INSCRIPTION_2023-2024'):
    os.mkdir('FRAIS_INSCRIPTION_2023-2024')

if not os.path.exists('FRAIS_ORGAMAT_2023-2024'):
    os.mkdir('FRAIS_ORGAMAT_2023-2024')

if not os.path.exists('FOURNITURE_2023-2024'):
    os.mkdir('FOURNITURE_2023-2024')


# --------------- UTILISATION DU LOGICIEL -------------------------


def MANUEL_UTILISATION():
    global root1
    root1 = Toplevel()
    root1.grab_set()
    root1.title("Manuel d'utilisation")
    root1.iconbitmap("Design StimLink 2-1.ico")
    root1.config(bg="black")
    root1.resizable(0, 0)

    Guideframe = LabelFrame(root1, text="BIENVENUE AU GUIDE D'UTILISATION", font=('calibri', 17, 'bold'), bd=5,
                            bg='black', fg='white')
    Guideframe.grid(row=0, column=0)

    Commencer = Button(Guideframe, text="Pour commencer", font=('calibri', 13, 'bold'), bg='black',
                       fg='Orange', command=commencer)
    Commencer.grid(row=0, column=0, sticky='w', padx=10, pady=8)

    Fonctions = Button(Guideframe, text="Les fonctions", font=('calibri', 13, 'bold'), bg='black',
                       fg='Orange', command=fonctions)
    Fonctions.grid(row=0, column=1, sticky='w', padx=10, pady=8)

    DB = Button(Guideframe, text="Base de données", font=('calibri', 13, 'bold'), bg='black',
                fg='Orange', command=bd)
    DB.grid(row=0, column=2, sticky='w', padx=10, pady=8)

    Auteur = Button(Guideframe, text="A propos de l'auteur", font=('calibri', 13, 'bold'), bg='black',
                    fg='Orange', command=auteur)
    Auteur.grid(row=0, column=3, sticky='w', padx=10, pady=8)

    Close = Button(Guideframe, text='Close', font=('calibri', 13, 'bold'), bg='red', fg='white', width=12,
                   command=close)
    Close.grid(row=1, column=3, pady=20)

    root1.mainloop()


# -------------------- Les fonctions (UTILISATION DU LOGICIEL) ----------------------


def commencer():
    root2 = Toplevel()
    root2.grab_set()
    root2.title("Pour commencer")
    root2.iconbitmap("Design StimLink 2-1.ico")
    root2.config(bg="black")
    root2.resizable(0, 0)

    title = Label(root2, text='LES PRINCIPES POUR COMMENCER A UTILISER', font=('Arial', 15, 'bold'), fg='Orange',
                  bg='black')
    title.pack()

    texte = Label(root2,
                  text="Le logiciel de gestion des paies permet de gerer d'une manière très moderne les données. \n" \
                       "Pour débuter, il faut maitriser les principes prédéfinis, et respecter toutes les étapes, \n" \
                       "nécessaire, au cas contraire, le logiciel ne marchera pas correctement (en d'autres terme, \n"
                       "il y aura des bugs). \n\n" \
                       "Principe 1 : ''' LA CONFIGURATION ''' Il faudrai en premier choisir l'intitulé du paiement (Ex. : Fourniture, frais...) \n, "
                       "et fixé le montant à payer (dans le champ montant en FC), et préciser le semestre s'il s'agit du frais scolaire, \n"
                       "et mettre juste un (-) s'il s'agit d'un autre intitulé par ex. OrgaMat, Inscription et Fourniture \n\n" \
                       "Principe 2 : ''' IDENTIFICATION ET PAIEMENT ''' Inserez le montant perçu, et remplisez tous les champs nécessaire, telque \n"
                       "(Nom, Post nom et Classe), et ne pas inseré quoi que ce soit dans 2 champs suivant : \n" \
                       "               - Reste à payer en FC (CDF) \n" \
                       "               - Reste à payer en $ (USD) \n" \
                       "Ces 2 champs nous donne les résultats une fois l'algorithme est en marche, il ne faut pas inserez des valeurs. \n\n" \
                       "Principe 3 : ''' REGLE D'ECRITURE ''' Le nom et Post nom doivent respecter une règle très particulière pour l'écriture : \n" \
                       "               - La première lettre du nom ou post nom doit être toujours en majuscule \n" \
                       "               - Le reste en minuscule. (Ex. : Stimsone Sivi) par contre (stimsone sivi) ne marchera pas ! \n\n" \
                       "Principe 4 : ''' RESULTAT ''' Pour mettre l'algorithme en marche, il faudrait, après remplissage des entrées, cliquez sur le \n" \
                       "bouton 'valider', si tous les principes sont respecter, il nous retournera le resultat sans problème, en cas de disfonctionnement, \n"
                       "prière de contacter le concepteur. (Voir contact auteur).\n\n"
                       "NB : Toujours enregistrer chaque opération, avant de restaurer ou de quitter.\n",
                  font=('Arial', 11, 'bold'), justify=LEFT)
    texte.pack(side=TOP)


def fonctions():
    root3 = Toplevel()
    root3.grab_set()
    root3.title("Les fonctions")
    root3.iconbitmap("Design StimLink 2-1.ico")
    root3.config(bg="black")
    root3.resizable(0, 0)

    title = Label(root3, text='COMPRENDRE LES DIFFERENTES FONCTIONS', font=('Arial', 15, 'bold'), fg='Orange',
                  bg='black')
    title.pack()

    texte = Label(root3, text="Derrière chaque opération (bouton) se cache une fonction. \n " \
                              "1. Valider : la fonction valider nous permet d'effectuer des calculs, et retourner les résultats \n "
                              "s'il n'y a pas des bugs \n\n " \
                              "2. Aperçu : La fonction aperçu affiche nos resultats dans une table, il ne marche pas si : \n\n " \
                              "          - le nom, le post nom, la classe, etc... ne sont pas remplis \n " \
                              "          - le montant ne pas inserer \n\n " \
                              "3. Enregistrer : La fonction enregistrer à pour rôle de stocker nos données sous différentes façons : \n " \
                              "          - dans une base de donnée : la base de donnée récolte les informations et les classifies dans \n "
                              "            des tables selon les spécificités \n " \
                              "          - dans un repertoire de reçu : il enregistre tous les données sous forme de reçu dans un repertoire,\n "
                              "            pour qu'elles soient facillement analyser\n\n" \
                              "4. Imprimer : On peut imprimer sur papier nos reçu, en appuyant sur le bouton imprimer, après avoir tous rempli...\n\n " \
                              "5. Restaurer : La fonction restaurer rétablie par défaut l'interface, sauf la zone de configuration\n\n" \
                              "6. Fermer : Il permet d'arrêter le programme\n\n" \
                              "7. Guide d'utilisation : Il nous aide à utiliser et à bien manipuler le logiciel, \n"
                              " c'est un guider qui décrit précisement ce qu'il faut faire et comment le faire.\n\n" \
                              "8. Lancer : Cette fonction permet de lancer une recherche dans le repertoire (uniquement du frais scolaire) \n "
                              " et il nous affiche le résultat si le numéro du réçu est bel et bien enregistrer. \n",
                  font=('Arial', 11, 'bold'), justify=LEFT)
    texte.pack(side=TOP)


def bd():
    root4 = Toplevel()
    root4.grab_set()
    root4.title("La base de données")
    root4.iconbitmap("Design StimLink 2-1.ico")
    root4.config(bg="black")
    root4.resizable(0, 0)

    title = Label(root4, text='LA DATABASE', font=('Arial', 15, 'bold'), fg='Orange', bg='black')
    title.pack()

    texte = Label(root4,
                  text="DB veut dire Data Base (ou Base des Données en français). \n "
                       "Elle permet de sécurisé nos données d'une manière très éfficace et pratique \n "
                       "La DB offre une certaine interractivité entre l'homme et la machine, \net "
                       "facilite l'analyse en favorisant le trie pour tirer des conclusions \n "
                       "Ce logiciel contient une seule DB repartie en 4 tables, qui est les 4 possibles paies de l'années : \n"
                       "- Table 1 : Frais_scolaire : Il reçoit toute les données liées au frais scolaire \n"
                       "- Table 2 : Frais_inscription : Il reçoit toute les données liées à l'inscription \n"
                       "- Table 3 : Frais_OrgaMat : Il reçoit toute les données liées à l'organisation matérielle \n"
                       "- Table 4 : Fourniture : Il reçoit toute les données liées à la fourniture scolaire \n",
                  font=('Arial', 11, 'bold'), justify=LEFT)
    texte.pack(side=TOP)


def auteur():
    root5 = Toplevel()
    root5.grab_set()
    root5.title("L'Auteur")
    root5.iconbitmap("Design StimLink 2-1.ico")
    root5.config(bg="black")
    root5.resizable(0, 0)

    title = Label(root5, text="A PROPOS DE L'AUTEUR", font=('Arial', 15, 'bold'), fg='Orange', bg='black')
    title.pack()

    texte = Label(root5,
                  text="Stimsone SIVI KIALA, ingénieur en Génie électrique/Energies renouvelables.\n "
                       "Ayant pour mission de réduire l'éffort mental et physique que l'homme peut \n "
                       "dépenser pour exercer une tâche plus ou moins complèxe, il pensera à s'auto-former \n "
                       "en programmation et le langage Python était sa priorité pour réléver ce défi.\n"
                       "Email : kialastimsone@gmail.com\n"
                       "Contact : +243 85 374 20 23, 81 58 95 286\n"
                       "Site web  : https://sites.google.com/view/stimlink\n",
                  font=('Arial', 11, 'bold'), justify=LEFT)
    texte.pack(side=TOP)


def close():
    global root1
    root1.destroy()


# ------------------------------- Fin (UTILISATION DU LOGICIEL) -----------------------------


def quitter():
    question = messagebox.askyesno('Fermeture', 'Voulez-vous fermer le programme ?')
    if question:
        quit()


def tables():
    if entryIntitule.get() == "":
        messagebox.showerror("Vide", "Precisez l'intitulé du paiement !")
    else:
        if entryIntitule.get() == "Inscription":
            print("")
        elif entryIntitule.get() == "Frais scolaire":
            print()
        elif entryIntitule.get() == "Fourniture":
            print("Fourniture scolaire")
        elif entryIntitule.get() == "OrgaMat":
            print("Frais orgamat")


AleaNumber = random.randint(10000, 19999)

# FENETRE PRINCIPALE
root = Tk()
root.config(background='gray15')
root.geometry('1386x723')
root.minsize(1386, 723)
root.maxsize(1386, 723)
root.title('PAIEMENT 2023-2024')
root.iconbitmap('Design StimLink 2-1.ico')

table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), height=5, show='headings')
table.place(x=695, y=275, width=640, height=343)

table.heading(1, text="N°")
table.heading(2, text="Nom")
table.heading(3, text="Post-nom")
table.heading(4, text="Classe")
table.heading(5, text="Intitulé")
table.heading(6, text="Semestre")
table.heading(7, text="Montant")
table.heading(8, text="Reste")
table.heading(9, text="Date")
table.bind("<ButtonRelease-1>", actualiser)

table.column(1, width=5)
table.column(2, width=28)
table.column(3, width=28)
table.column(4, width=15)
table.column(5, width=10)
table.column(6, width=10)
table.column(7, width=15)
table.column(8, width=15)
table.column(9, width=15)

con = sq.connect('PAIEMENT 2023-2024 DataBase.db')
cuser = con.cursor()
select = cuser.execute("select * from Frais_scolaire")
data = select.fetchall()
for row in data:
    table.insert("", END, values=row)

con.close()

Date = StringVar()
today = date.today()
Aujourdhui = today.strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")

DATE = Label(root, textvariable=Date, width=15, font="arial 10", bg="gray15", fg="gray15")
DATE.place(x=0, y=100)
Date.set(Aujourdhui)

labelprincipale = Label(root, text="PAIEMENT 2023-2024", font=('Arial', 30, 'bold'), bg='gray15', fg='white',
                        bd=12, relief=RIDGE)
labelprincipale.pack(fill=X)

FRAME = Frame(root)
FRAME.pack()

config = LabelFrame(FRAME, text='Configuration', font=('Arial', 18, 'bold'),
                    fg='Orange', bg='gray17', relief=GROOVE, bd=5)
config.grid(row=0, column=0)

intitulelabel = Label(config, text='Intitulé', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
intitulelabel.grid(row=0, column=0, padx=12, pady=5, sticky="w")
ListIntitule = ['Inscription', 'Fourniture', 'Frais scolaire', 'OrgaMat']

btnchoix = Button(root, text="Select", font=('arial', 12, 'bold'), bg='white', fg='black', bd=3,
                      width=5, command="")
btnchoix.place(x=10, y=650)

entryIntitule = ttk.Combobox(config, values=ListIntitule, font=('Arial', 12, 'bold'), width=15)
entryIntitule.grid(row=0, column=1, padx=8, sticky="w")

perso = Label(config, text='Montant en FC', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
perso.grid(row=2, column=0, padx=12, pady=5, sticky="w")

persoEnrty = Entry(config, font=('Arial', 12, 'bold'), width=13)
persoEnrty.grid(row=2, column=1, padx=8, sticky="w")
persoentry = StringVar()

Semestrelabel = Label(config, text='Semestre', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
Semestrelabel.grid(row=1, column=0, padx=12, pady=5, sticky="w")
ListSemestre = ['-', '1', '2', '3']

entrySemestre = ttk.Combobox(config, values=ListSemestre, font=('Arial', 12, 'bold'), width=4)
entrySemestre.grid(row=1, column=1, padx=8, sticky="w")

detail_frame = LabelFrame(FRAME, text='Identification', font=('Arial', 18, 'bold'),
                          fg='Orange', bg='gray17', relief=GROOVE, bd=5)

detail_frame.grid(row=0, column=1)

namelabel = Label(detail_frame, text='Nom', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
namelabel.grid(row=0, column=0, padx=12, pady=5, sticky="w")
entryname = Entry(detail_frame, font=('Arial', 14, 'bold'), width=20)
entryname.grid(row=0, column=1, padx=8, sticky="w")

postnamelabel = Label(detail_frame, text='Post-nom', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
postnamelabel.grid(row=1, column=0, padx=12, pady=5, sticky="w")
entrypostname = Entry(detail_frame, font=('Arial', 14, 'bold'), width=20)
entrypostname.grid(row=1, column=1, padx=8, sticky="w")

numberlabel = Label(detail_frame, text='Classe', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
numberlabel.grid(row=2, column=0, padx=12, pady=5, sticky="w")
ListClasse = ['8ème A', '8ème B', '8ème C', '1ère ETRI A', '1ère ETRI B', '1ère ETRI C',
              '2ème ETRI A', '2ème ETRI B', '2ème ETRI C', '3ème ETRI A', '3ème ETRI B',
              '3ème ETRI C', '4ème ETRI A', '4ème ETRI B', '4ème ETRI C', '1ère LATIN PH A',
              '1ère LATIN PH B', '2ème LATIN PH A', '2ème LATIN PH B', '3ème LATIN PH A',
              '3ème LATIN PH B', '4ème LATIN PH A', '4ème LATIN PH B', '1ère C CTR A',
              '1ère C CTR B', '2ème C CTR B', '2ème C CTR B', '3ème C CTR A', '3ème C CTR B',
              '4ème C CTR A', '4ème C CTR B', '1ère SCT A', '1ère SCT B', '1ère SCT C',
              '2ème SCT A', '2ème SCT B', '2ème SCT C', '3ème SCT A', '3ème SCT B',
              '3ème SCT C', '4ème SCT A', '4ème SCT B', '4ème SCT C', '1ère PEDA A',
              '1ère PEDA B', '1ère PEDA C', '2ème PEDA A', '2ème PEDA B', '2ème PEDA C',
              '3ème PEDA A', '3ème PEDA B', '3ème PEDA C', '4ème PEDA A', '4ème PEDA B', '4ème PEDA C',
              '1ère COM/GST A', '1ère COM/GST B', '2ème COM/GST A', '2ème COM/GST B',
              '3ème COM/GST A', '3ème COM/GST B', '4ème COM/GST A', '4ème COM/GST B', '1ère CONS A',
              '1ère CONS B', '2ème CONS A', '2ème CONS B', '3ème CONS A', '3ème CONS B',
              '4ème CONS A', '4ème CONS B',
              ]
entrynumber = ttk.Combobox(detail_frame, values=ListClasse, font=('Arial', 13, 'bold'), width=22)
entrynumber.grid(row=2, column=1, padx=8, sticky="w")

rec_frame = LabelFrame(FRAME, text='Recherche', font=('Arial', 18, 'bold'),
                       fg='Orange', bg='gray17', relief=GROOVE, bd=5)
rec_frame.grid(row=0, column=3)

NUMlabel = Label(rec_frame, text='N°Reçu', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
NUMlabel.grid(row=0, column=0, padx=12, pady=5, sticky='e')
entryNUM = Entry(rec_frame, font=('Arial', 13, 'bold'), width=10)
entryNUM.grid(row=0, column=1, padx=8)

Newlabel1 = Label(rec_frame, text='', font=('Arial', 12, 'bold'), bg='gray17',
                  fg='gold')
Newlabel1.grid(row=2, column=0, padx=12, pady=5, sticky='w')

Recherche = Button(rec_frame, text='Lancer', font=('Arial', 12, 'bold'), width=6, command=recherche)
Recherche.grid(row=1, column=1, padx=12, pady=5)

mtn_frame = LabelFrame(FRAME, text='Montant', font=('Arial', 18, 'bold'),
                       fg='Orange', bg='gray17', relief=GROOVE, bd=5)
mtn_frame.grid(row=0, column=2)

Prclabel = Label(mtn_frame, text='Perçu', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
Prclabel.grid(row=0, column=0, padx=12, pady=5, sticky='w')
entryprc = Entry(mtn_frame, font=('Arial', 13, 'bold'), width=15)
entryprc.grid(row=0, column=1, padx=8, sticky="w")
Rstlabel = Label(mtn_frame, text='Reste to CDF', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
Rstlabel.grid(row=1, column=0, padx=12, pady=5, sticky='w')
entryrst = Entry(mtn_frame, font=('Arial', 13, 'bold'), width=15)
entryrst.grid(row=1, column=1, padx=8, sticky="w")

Rstlabel1 = Label(mtn_frame, text='Reste to USD', font=('Arial', 14, 'bold'), bg='gray15', fg='white')
Rstlabel1.grid(row=2, column=0, padx=12, pady=5, sticky='w')
entryrst1 = Entry(mtn_frame, font=('Arial', 13, 'bold'), width=15)
entryrst1.grid(row=2, column=1, padx=8, sticky="w")

# Apercu
Apercutab = Frame(root, bd=7, relief=GROOVE)
Apercutab.place(x=50, y=233)

Apercutitle = Label(Apercutab, text='REÇU DE PAIEMENT', font=('Arial', 15, 'bold'), bd=3, relief=GROOVE)
Apercutitle.pack(fill=X)

scrollbar = Scrollbar(Apercutab, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

texteAp = Text(Apercutab, height=21, width=60, yscrollcommand=scrollbar.set)
texteAp.pack()
scrollbar.config(command=texteAp.yview())

# Boutons
validBouton = Button(root, text='Valider', font=('arial', 12, 'bold'), bg='orange', fg='white', bd=4,
                     width=7, command=valider)
validBouton.place(x=795, y=650)

ApercuBouton = Button(root, text='Aperçu', font=('arial', 12, 'bold'), bg='blue', fg='white', bd=4,
                      width=7, command=apercu)
ApercuBouton.place(x=882, y=650)

enregBouton = Button(root, text='Enregistrer', font=('arial', 12, 'bold'), bg='green', fg='white',
                     bd=4, width=10, command=enregistrement)
enregBouton.place(x=968, y=650)

quitBouton = Button(root, text='Restaurer', font=('arial', 12, 'bold'), bg='seagreen', fg='white',
                    bd=4, width=8, command=restauration)
quitBouton.place(x=1103, y=650)

quitBouton = Button(root, text='Fermer', font=('arial', 12, 'bold'), bg='red', fg='white',
                    bd=4, width=7, command=quitter)
quitBouton.place(x=1199, y=650)

ImprimeBouton = Button(root, text='IMPRIMER', font=('arial', 12, 'bold'), bg='white', fg='gray20',
                       bd=4, width=8, command=imprimer)
ImprimeBouton.place(x=288, y=650)

guidebtn = Button(root, text="GUIDE D'UTILISATION", font=('arial', 12, 'bold'), bg='seagreen', fg='white',
                  bd=4, width=18, command=MANUEL_UTILISATION)
guidebtn.place(x=90, y=650)

root.mainloop()
