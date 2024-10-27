# - Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments
#  des deux listes en les alternant, de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t3 = []

#me permet de lister cela en Date+mois
for i in range(len(t1)):
    t3.append(str(t1[i]) + ' ' + t2[i])

for element in t3:
    print(element)