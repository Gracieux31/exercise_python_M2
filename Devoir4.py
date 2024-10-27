#En partant de l'exercice précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome 
# (c'est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), 
# comme par exemple « radar » ou « s.o.s ».

def is_palindrome(input_string):
    reversed_string = input_string[::-1]
    if input_string == reversed_string:
        print("La chaîne est un palindrome")
    else:
        print("La chaîne n'est pas un palindrome")

#l'utilisateur d'entre une chaîne de caractères
user_input = input("Veuillez entrer une chaîne de caractères: ")

is_palindrome(user_input)