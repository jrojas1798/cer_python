#Laboratorio 3.2.1.15
c0 = int(input("Ingresa un numero positivo para la variable c0 "))
pasos = 0
while c0 != 1:
    if c0%2 ==0:
        c0 = c0/2
        pasos += 1
    elif c0%2 == 1: 
        c0= (3*c0) + 1
        pasos += 1
    print (int(c0))

print ("Pasos = ",pasos)