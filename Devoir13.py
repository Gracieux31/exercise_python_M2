#Écrivez une fonction qui échange les clés et les valeurs d'un dictionnaire 
# (ce qui permettra par exemple de transformer un dictionnaire anglais/français en un dictionnaire français/anglais).
#On suppose que le dictionnaire ne contient pas plusieurs valeurs identiques.
#
def swap_dictionary(input_dict):
    return {value: key for key, value in input_dict.items()}

# exécution de la fonction
english_french = {'hello': 'bonjour', 'goodbye': 'au revoir', 'please': 's\'il vous plaît'}
french_english = swap_dictionary(english_french)
print(french_english)