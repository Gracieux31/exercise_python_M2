# Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».

def contains_e(input_string):
    if 'e' in input_string:
        print("La chaîne contient le caractère 'e'")
    else:
        print("La chaîne ne contient pas le caractère 'e'")

user_input = input("Veuillez entrer une chaîne de caractères: ")

contains_e(user_input)

