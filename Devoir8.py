#Écrivez un programme qui analyse un par un tous les éléments d'une liste de nombres (par exemple celle de l'exercice précédent) 
# pour générer deux nouvelles listes. L'une contiendra seulement les nombres pairs de la liste initiale, 
# et l'autre les nombres impairs. Par exemple, si la liste initiale est celle de l'exercice précédent, 
# le programme devra construire une liste pairs qui contiendra [32, 12, 8, 2], et une liste impairs qui contiendra [5, 3, 75, 15]. 
#Astuce : pensez à utiliser l'opérateur modulo (%) déjà cité précédemment.

def separate_even_odd(input_list):
    even_list = [num for num in input_list if num % 2 == 0]
    odd_list = [num for num in input_list if num % 2 != 0]
    print("Liste des nombres pairs :", even_list)
    print("Liste des nombres impairs :", odd_list)

separate_even_odd([32, 5, 12, 8, 3, 75, 2, 15])