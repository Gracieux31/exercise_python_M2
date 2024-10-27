#Modifiez le script ci-dessus afin qu'il établisse une table des occurrences de chaque mot dans le texte. 
#Conseil : dans un texte quelconque, les mots ne sont pas seulement séparés par des espaces,
#mais également par divers signes de ponctuation. Pour simplifier le problème, 
# vous pouvez commencer par remplacer tous les caractères nonalphabétiques par des espaces, 
# et convertir la chaîne résultante en une liste de mots à l'aide de la méthode split().

import collections

# Ouvrir le fichier
with open('Monfichier', 'r') as file:
    text = file.read()

# rend le en minuscules pour simplifier le comptage
text = text.lower()

# change les caractères non alphabétiques par des espaces
for char in text:
    if not char.isalpha() and not char.isspace():
        text = text.replace(char, ' ')

# change le texte en une liste de mots
words = text.split()

# stocke le comptage des mots
word_counts = collections.Counter(words)

# Afficher le nombre d'occurrences de chaque mot
for word, count in word_counts.items():
    print(f"{word}: {count}")