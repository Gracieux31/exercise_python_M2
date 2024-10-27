#Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. 
# Par exemple, si on l'appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :

def find_max(input_list):
    max_value = max(input_list)
    print("Le plus grand élément de cette liste a la valeur", max_value)

find_max([32, 5, 12, 8, 3, 75, 2, 15])