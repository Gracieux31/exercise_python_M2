#Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l'inversant.
#Ainsi par exemple, « zorglub » deviendra « bulgroz ».

def reverse_string(input_string):
    return input_string[::-1]

new_string = reverse_string("zorglub")
print(new_string)