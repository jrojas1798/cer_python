#Laboratorio 3.2.1.11
word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letra in user_word:
    # Completa el cuerpo del bucle for.
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        word_without_vowels = word_without_vowels+letra
print(word_without_vowels)
# Imprimir la palabra asignada a word_without_vowels.




