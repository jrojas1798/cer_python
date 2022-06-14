# Laboratorio 2.6.1.11
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
# calcula los minutos y los convierte a una cadena
minutos=str((mins+dura) %60)
# calcula los minutos totales y luego lo convierte a horas y despues a una cadena
horas= str(((hour*60 + mins + dura)//60) % 24)
'Salida'
print("Hora: " +horas +":" +minutos)