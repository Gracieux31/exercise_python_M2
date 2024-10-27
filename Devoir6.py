#Écrivez un programme qui affiche « proprement » tous les éléments d'une liste.
#  Si on l'appliquait par exemple à la liste t2 de l'exercice ci-dessus, on devrait obtenir :

t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t2_string = ' '.join(t2)

print(t2_string)