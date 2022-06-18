#Laboratorio 3.4.1.6
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero = int(input("Ingresa el numero que remplazaras en la lista: "))
hat_list[2] = numero 
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[4]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la lista es de: ",len(hat_list))
print(hat_list)
