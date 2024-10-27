#Vous avez à votre disposition un fichier texte quelconque (pas trop gros). 
# Écrivez un script qui analyse ce texte, et mémorise dans un dictionnaire l'emplacement exact de chacun des mots 
# (compté en nombre de caractères à partir du début).
# Lorsqu'un même mot apparaît plusieurs fois, tous ses emplacements doivent être mémorisés : 
# chaque valeur de votre dictionnaire doit donc être une liste d'emplacements.

import collections

# Ouvrir le fichier en mode lecture
with open('Monfichier', 'r') as file:
    text = file.read()

text = text.lower()

# change tous les caractères non alphabétiques par des espaces
for char in text:
    if not char.isalpha() and not char.isspace():
        text = text.replace(char, ' ')

# Stocke les emplacements des mots
word_locations = collections.defaultdict(list)


for word in text.split():
    # tous les emplacements du mot
    start = 0
    while start < len(text):
        start = text.find(word, start)
        if start == -1: break
        word_locations[word].append(start)
        start += len(word)

# Afficher les emplacements de chaque mot
for word, locations in word_locations.items():
    print(f"{word}: {locations}")