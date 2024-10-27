# Écrivez un script qui crée un mini-système de base de données fonctionnant à l'aide d'un dictionnaire, 
# dans lequel vous mémoriserez les noms d'une série de copains, leur âge et leur taille.

# Fonction pour remplir le database

def remplir_dictionnaire():
    base_donnees = {}  # Initialisation du database
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

# Fonction pour consulter le database
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

# exécution 
def main():
    print("Remplissage de la base de données des amis.")
    base_donnees = remplir_dictionnaire()
    
    print("\nConsultation de la base de données.")
    consulter_dictionnaire(base_donnees)

# Appel de l'exécution
if __name__ == "__main__":
    main()
