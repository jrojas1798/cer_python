#Laboratorio 3.1.1.12
year = int(input("Introduce un año:"))

#
# Escribe tu código aquí.
#	
if not year % 4 == 0:
    print("Año común")
elif not (year%100 == 0):
    print("Año Bisiesto")
elif not (year%400 == 0):
    print("Año común")
else:
    print("Año bisiesto")