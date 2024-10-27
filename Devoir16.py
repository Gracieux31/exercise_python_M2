#Améliorez encore le script de l'exercice précédent, en utilisant un dictionnaire pour diriger le flux d'exécution du programme 
#au niveau du menu principal.

# Fonction pour remplir le dictionnaire
def remplir_dictionnaire(base_donnees):
    while True:
        nom = input("Entrez le nom de votre ami (ou tapez 'stop' pour terminer) : ")
        if nom.lower() == 'stop':
            break
        try:
            age = int(input(f"Entrez l'âge de {nom} en années : "))
            taille = float(input(f"Entrez la taille de {nom} en mètres : "))
            base_donnees[nom] = (age, taille)
        except ValueError:
            print("Erreur : l'âge doit être un entier et la taille un nombre réel.")
            continue

# Fonction pour consulter le dictionnaire
def consulter_dictionnaire(base_donnees):
    while True:
        nom = input("Entrez le nom à rechercher (ou tapez 'stop' pour terminer) : ")
        if nom.lower() == 'stop':
            break
        if nom in base_donnees:
            age, taille = base_donnees[nom]
            print(f"Nom : {nom} - âge : {age} ans - taille : {taille:.2f} m")
        else:
            print(f"Le nom {nom} n'est pas dans la base de données.")

# Fonction pour enregistrer le dictionnaire dans un fichier
def enregistrer_dictionnaire(base_donnees, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        for nom, (age, taille) in base_donnees.items():
            ligne = f"{nom}@{age}#{taille}\n"
            fichier.write(ligne)

# Fonction pour reconstituer le dictionnaire à partir d'un fichier
def reconstituer_dictionnaire(nom_fichier):
    base_donnees = {}
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                nom, donnees = ligne.strip().split('@')
                age, taille = map(float, donnees.split('#'))
                base_donnees[nom] = (int(age), taille)
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    return base_donnees

# Script principal
def main():
    nom_fichier = "Log.txt"  # Nom du fichier pour sauvegarder les données
    base_donnees = {}

    # Dictionnaire des fonctions pour le menu
    menu_options = {
        'R': lambda: reconstituer_dictionnaire(nom_fichier),
        'A': lambda: remplir_dictionnaire(base_donnees),
        'C': lambda: consulter_dictionnaire(base_donnees),
        'S': lambda: enregistrer_dictionnaire(base_donnees, nom_fichier),
        'T': lambda: print("Terminaison du programme.") 

    while True:
        print("\nMenu :")
        print("(R)écupérer un dictionnaire préexistant sauvegardé dans un fichier")
        print("(A)jouter des données au dictionnaire courant")
        print("(C)onsulter le dictionnaire courant")
        print("(S)auvegarder le dictionnaire courant dans un fichier")
        print("(T)erminer")
        choix = input("Choisissez : ").upper()

        if choix in menu_options:
            if choix == 'R':
                base_donnees.update(menu_options[choix]())
                print("Dictionnaire reconstitué.")
            elif choix in ['A', 'C', 'S']:
                menu_options[choix]()
                if choix == 'S':
                    print(f"Données enregistrées dans {nom_fichier}.")
            elif choix == 'T':  # Terminer le programme
                print("Terminaison du programme.")
                break  # Sortir de la boucle
        else:
            print("Choix invalide, veuillez réessayer.")

# Appel du script principal
if __name__ == "__main__":
    main()