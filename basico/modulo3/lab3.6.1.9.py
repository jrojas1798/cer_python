#Laboratorio 3.6.1.9
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
#
lista2 = my_list[2:9]
for i in my_list:
    if i in lista2:
        del my_list[i]


print("La lista con elementos únicos:")
print(my_list)
