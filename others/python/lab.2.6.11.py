hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.

total_mins = hour*60 + mins + dura
print(total_mins)

hours = total_mins // 60
mins = total_mins % 60
hours %= 24
time = str(hours) + ":" + str(mins)

print("El evento termina a las: ", time)