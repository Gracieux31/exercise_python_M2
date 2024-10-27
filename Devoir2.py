#Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères.
#Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »

def insert_asterisks(input_string):
    return '*'.join(list(input_string))

#l'utilisateur entre une chaîne de caractères
user_input = input("Veuillez entrer une chaîne de caractères: ")

new_string = insert_asterisks(user_input)
print(new_string)