#Écrivez un script qui crée un mini-système de base de données fonctionnant à l'aide d'un dictionnaire, 
#dans lequel vous mémoriserez les noms d'une série de copains, leur âge et leur taille.

# Pour écrire dans le dictionnaire
def remplir_dictionnaire():
    base_donnees = {}  # remise a zéro
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
    return base_donnees

# pour lire le dictionnaire.
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

# Enregistre le dictionnaire dans un fichier texte
def enregistrer_dictionnaire(base_donnees, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        for nom, (age, taille) in base_donnees.items():
            fichier.write(f"{nom}@{age}#{taille:.2f}\n")
    print(f"Le dictionnaire a été enregistré dans le fichier '{nom_fichier}'.")

# reconstitue le dictionnaire à partir d'un fichier texte
def reconstituer_dictionnaire(nom_fichier):
    base_donnees = {}
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                    nom, infos = ligne.split('@')
                    age, taille = infos.split('#')
                    base_donnees[nom] = (int(age), float(taille))
        print(f"Le dictionnaire a été reconstitué à partir du fichier '{nom_fichier}'.")
    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' n'existe pas.")
    return base_donnees

# Script d'exécution
def main():
    print("Remplissage de la base de données des amis.")
    base_donnees = remplir_dictionnaire()

    # Enregistrer le dictionnaire dans un fichier texte
    nom_fichier = "Log.txt"
    enregistrer_dictionnaire(base_donnees, nom_fichier)

    # Reconstituer le dictionnaire à partir du fichier
    base_donnees_reconstituees = reconstituer_dictionnaire(nom_fichier)

    print("\nConsultation de la base de données reconstituée.")
    consulter_dictionnaire(base_donnees_reconstituees)

# Appel du script principal
if __name__ == "__main__":
    main()