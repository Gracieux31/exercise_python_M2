# !/usr/bin/env python3
# votre premier script python
#print('Hello world!')
#x, nom = 32, 'Toto'
#print('nom','a','x','ans')
#prop = (4500.0 + 2575)/14800
#print ("La proportion est", prop)
#print ("La proportion est %.2f" % prop)
#print ("La proportion est %.3f, arrondi à %i." % (prop, prop))

#fi = open ('Monfichier', 'r')
#t = fi.readlines ()
#print (t)
#fi.close ()

#fi = open('Monfichier', 'w')  # Correction des guillemets et de l'appel à 'open'
#fi.write("Ceci est la ligne un \nVoici la ligne deux\n")  # Utilisation correcte de '\n'
#fi.write("Ceci est la ligne trois \n")  # Ajout de l'échappement correct pour '\n'
#fi.close()
#a = 2
#if a > 0:
#    print("a est positif")
#elif a < 0:
#    print("a est négatif")
#else:
#    print("a est nul")
#for i in range(1000):
#    print(i)
#for i in range(5):
#    if i > 3:
#        break  # Interrompt la boucle
#    print(i)
#    if i == 2:
#        continue
#    print(i)

# Ce message sera imprimé même si la boucle est interrompue
#print('Finis! (après la boucle)')

#def monter():
#    global a  # On indique que 'a' est une variable globale
#    b = 3     # 'b' est une variable locale à la fonction
##    a = a + 1
#    print(a, b)

# Variables globales
#a = 15
#b = 20

# Appels de la fonction
#monter()
#monter()

# Affichage des valeurs globales de 'a' et 'b'
#print(a, b)



#def addition(a, b):
#    c = a + b
#    return c

#c = 15
#d = 20

#e = addition(c, d)

#print(c, '+', d, '=', e)

##import os
#if len(sys.argv) != 2:
#    sys.exit("ERREUR : il faut exactement un argument.")
#if os.path.exists('Monfichier.txt'):
#    os.system("ls -al")
#else:
#   sys.exit("ERREUR : Le fichier 'toto.txt' n'existe pas.")

#nombres = [5, 38, 10, 25]
#mots  = ["jambon", "fromage", "confiture", "chocolat"]
#trucs = [5000, "Brigitte", 3.1416, ["'Albert", "René", 1947]] 
#print (nombres) 
#print (mots) 
#print (trucs)


#mots = ['jambon', 'fromage', 'confiture', 'chocolat']

# Insertion de "miel" à l'index 2
#mots[2:2] = ["miel"]
#print(mots)

# Insertion de 'saucisson' et 'ketchup' à l'index 5
#mots[5:5] = ['saucisson', 'ketchup']
#print(mots)

# Remplacement des éléments de l'index 2 à 5 par ['ป']
#mots[2:5] = ['ป']
#print(mots)

# Remplacement des éléments de l'index 1 à 3 par ['salade']
#mots[1:3] = ['salade']
#print(mots)

# Remplacement des éléments à partir de l'index 1 par ['mayonnaise', 'poulet', 'tomate']
#mots[1:] = ['mayonnaise', 'poulet', 'tomate']
#print(mots)



#class Espaces(object):
#    aa = 33  # Variable de classe

#    def affiche(self):
        # Accès à la variable de classe et à l'attribut d'instance
#        print(aa, self.aa, Espaces.aa)
#aa = 12
#essai = Espaces()
#essai.aa = 67  # Attribut d'instance

# Appel de la méthode affiche
#essai.affiche()

# Pour afficher les valeurs à l'extérieur de la classe
#print(aa, essai.aa, Espaces.aa)  # Accès à l'attribut d'instance et à la variable de classe

# class Atome:
#     """Atomes simplifiés, choisis parmi les 10 premiers éléments du tableau périodique."""
#     # Table des atomes : (nom, numéro atomique, protons, neutrons)
#     table = {
#         1: ("Hydrogène", 1),   # H
#         2: ("Hélium", 2),      # He
#         3: ("Lithium", 3),     # Li
#         4: ("Béryllium", 4),   # Be
#         5: ("Bore", 5),        # B
#         6: ("Carbone", 6),     # C
#         7: ("Azote", 7),       # N
#         8: ("Oxygène", 8),     # O
#         9: ("Fluor", 9),       # F
#         10: ("Néon", 10)       # Ne
#     }

#     def __init__(self, nat):
#         """Le numéro atomique détermine le nombre de protons, d'électrons et de neutrons."""
#         self.np, self.ne = nat, nat  # Le nombre de protons et d'électrons est égal au numéro atomique
#         self.nn = Atome.table[nat][1]  # Neutrons (dans ce cas, égal à 0 pour simplifier)

#     def affiche(self):
#         print("\nNom de l'élément :", Atome.table[self.np][0])
#         print("%s protons, %s électrons, %s neutrons" % (self.np, self.ne, self.nn))


# class Ion(Atome):
#     """Les ions sont des atomes qui ont gagné ou perdu des électrons."""
    
#     def __init__(self, nat, charge):
#         """Le numéro atomique et la charge électrique déterminent l'ion."""
#         super().__init__(nat)  # Appelle le constructeur de la classe parente
#         self.ne = self.ne - charge  # Nombre d'électrons modifié par la charge
#         self.charge = charge

#     def affiche(self):
#         super().affiche()  # Appelle la méthode affiche de la classe parente
#         print("Particule électrisée. Charge =", self.charge)


# # Exemple d'utilisation :
# hydrogene = Atome(1)
# hydrogene.affiche()

# ion_hydrogene = Ion(1, 1)  # H+ (ion hydrogène avec une charge positive)
# ion_hydrogene.affiche()


#Mdule TK ( Graphique)

# from tkinter import *
# fen1 = Tk()
# tex1 = Label(fen1, text='Bonjour tout le monde!', fg='red')
# tex1.pack()  # tex1 au lieu de texl
# bou1 = Button(fen1, text='Quitter', command=fen1.destroy)
# bou1.pack()  # bou1 au lieu de boul
# fen1.mainloop()  # fen1 au lieu de fenl

# from tkinter import *

# def pointeur(event):
#     chaine.configure(text="Clic détecté en X=" + str(event.x) + ", Y=" + str(event.y))

# fen = Tk()
# cadre = Frame(fen, width=200, height=150, bg="light yellow")

# # Correction de la faute de frappe: "<Bytton-1>" devient "<Button-1>"
# cadre.bind("<Button-1>", pointeur)
# cadre.pack()

# chaine = Label(fen)
# chaine.pack()

# fen.mainloop()

# from tkinter import *

# # Initialisation des coordonnées globales
# x1, y1 = 10, 10

# # procédure générale de déplacement :
# def avance(gd, hb):
#     global x1, y1  # Correction de la variable y1 (faute de frappe)
#     x1, y1 = x1 + gd, y1 + hb
#     can1.coords(oval1, x1, y1, x1 + 30, y1 + 30)  # Correction: oval1 au lieu de ovall

# # gestionnaires d'événements :
# def depl_gauche():
#     avance(-10, 0)

# def depl_droite():  # Correction de la faute de frappe dans le nom de la fonction
#     avance(10, 0)

# def depl_haut():
#     avance(0, -10)

# def depl_bas():
#     avance(0, 10)

# # Création de la fenêtre principale
# fen = Tk()
# can1 = Canvas(fen, width=400, height=300, bg='white')
# can1.pack()

# # Création d'un oval qui sera déplacé
# oval1 = can1.create_oval(x1, y1, x1 + 30, y1 + 30, fill='red')

# # Ajout des boutons de contrôle
# Button(fen, text='Gauche', command=depl_gauche).pack(side=LEFT)
# Button(fen, text='Droite', command=depl_droite).pack(side=RIGHT)
# Button(fen, text='Haut', command=depl_haut).pack(side=TOP)
# Button(fen, text='Bas', command=depl_bas).pack(side=BOTTOM)

# fen.mainloop()


# from tkinter import *

# # Les variables suivantes seront utilisées de manière globale :
# x1, y1 = 10, 10  # coordonnées initiales

# # Procédure générale de déplacement :
# def avance(gd, hb):
#     global x1, y1
#     x1, y1 = x1 + gd, y1 + hb
#     can1.coords(oval1, x1, y1, x1 + 30, y1 + 30)

# # Gestionnaires d'événements :
# def depl_gauche():
#     avance(-10, 0)

# def depl_droite():
#     avance(10, 0)

# def depl_haut():
#     avance(0, -10)

# def depl_bas():
#     avance(0, 10)

# # ——— Programme principal ———
# # Création du widget principal :
# fen1 = Tk()
# fen1.title("Exercice d'animation avec Tkinter")  # Correction du titre (manquait une parenthèse)

# # Création des widgets fils :
# can1 = Canvas(fen1, bg='dark grey', height=300, width=300)  # Ajout de la virgule manquante entre 'height' et 'width'
# oval1 = can1.create_oval(x1, y1, x1 + 30, y1 + 30, width=2, fill='red')  # Correction de `ovall` en `oval1`
# can1.pack(side=LEFT)

# # Création des boutons :
# Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
# Button(fen1, text='Gauche', command=depl_gauche).pack()
# Button(fen1, text='Droite', command=depl_droite).pack()  # Correction des fautes de frappe
# Button(fen1, text='Haut', command=depl_haut).pack()
# Button(fen1, text='Bas', command=depl_bas).pack()

# # Lancement de la boucle principale :
# fen1.mainloop()


from scapy.all import *
plage = '192.168.1.1-15'
paquet = Ether() / IP(dst=plage) / ICMP()
rep, non_rep = srp(paquet, timeout=0.5 )
for element in rep:
if element[1][|CMP] .type == 0:
print(element[0][IP].dst +' a renvoyé un echo-reply ')
for element in non rep:
if element[1][|СМР] .type == 8:
print(element[O][IP].dst +' : aucun echo-reply ')