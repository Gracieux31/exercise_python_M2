#Écrivez un programme qui analyse un par un tous les éléments d'une liste de mots 
#(par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'] ) pour générer deux nouvelles listes.
#L'une contiendra les mots comportant moins de 6 caractères, l'autre les mots comportant 6 caractères ou davantage.

def separate_words(input_list):
    short_words = [word for word in input_list if len(word) < 6]
    long_words = [word for word in input_list if len(word) >= 6]
    print("Liste des mots courts :", short_words)
    print("Liste des mots longs :", long_words)

separate_words(['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'])