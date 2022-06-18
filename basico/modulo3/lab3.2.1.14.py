#Laboratorio 3.2.1.14
blocks = int(input("Ingresa el número de bloques: "))
#
# Escribe tu código aquí.
#	
altura = 0
while blocks > altura:
    altura = altura+1
    blocks = blocks - altura
print("La altura de la pirámide:", altura)