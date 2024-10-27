#Vous avez à votre disposition un fichier texte quelconque (pas trop gros).
# Écrivez un script qui compte les occurrences de chacune des lettres de l'alphabet dans ce texte
# (on simplifiera le problème en ne tenant pas compte des lettres accentuées).

import collections

# ouvre le fichier texte
with open('Monfichier', 'r') as file:
    text = file.read()

# Convertir le texte en minuscules
text = text.lower()

# stocke le comptage des lettres
letter_counts = collections.defaultdict(int)

for char in text:
    # Vérifie le caractère est une lettre de l'alphabet
    if char.isalpha():
        letter_counts[char] += 1

for letter, count in letter_counts.items():
    print(f"{letter}: {count}")