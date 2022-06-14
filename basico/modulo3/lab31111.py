# Laboratorio 3.1.1.11
income = float(input("Introduce el ingreso anual:"))
#
# Escribe tu código aquí.
#
if income <= 85_529:
    tax = income*0.18 - 556.2
else:
    tax = 14839.2+ (income-85528)*0.32

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
