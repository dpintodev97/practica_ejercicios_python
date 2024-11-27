#Para hacer conversiones entre cadenas y objetos de fecha u hora, necesitamos importar el modulo datetime
from datetime import datetime

#EJERCICIO CON FECHAS :

"""Para realizar estos ejercicios parte de dos listas: una con fechas representadas como cadenas en formato
YYYY-MM-DD y otra con horas con cadenas en formato HH:MM:SS

fechas = ['2024-09-09', '2023-08-15', '2022-07-01']

horas = ['14:30:00', '09:15:00', '23:59:59']
"""

fechas = ['2024-09-09', '2023-08-15', '2022-07-01']
horas = ['14:30:00', '09:15:00', '23:59:59']

# Convierte cada cadena de la lista fechas a un objeto datetime.date
fechas_date = [datetime.strptime(fecha, "%Y-%m-%d").date() for fecha in fechas]

# Convierte cada cadena de la lista horas a un objeto datetime.time
horas_time = [datetime.strptime(hora, "%H:%M:%S").time() for hora in horas]

#Muestra la fecha de hoy y la hora de hoy.
print("La fecha de hoy es: ", fechas_date)
print("La hora de hoy es: ", horas_time)

#NOTA: datetime.strptime ----> para analizar las cadenas y convertirlas.
#función strptime (string parse time) toma 2 argumentos: 
#   La cadena de texto.
#   El formato en el que está la cadena (%Y-%m-%d para fechas y %H:%M:%S para horas).
#Y por último, acceso: .date() o .time() para extraer únicamente la parte de la fecha o la hora.

#Combina cada elemento de los objetos date y los objetos time de los dos ejercicios anteriores para crear una
#lista de objetos datetime:
lista_objeto_datetime = datetime.combine(fechas_date[0], horas_time[0])
print("La lista de objetos datetime es: ", lista_objeto_datetime )
#NOTA: datetime.combine ----> combina dos objetos date y time en un solo objeto datetime; como es lista de elementos, se puede acceder a ellos con indices, partiendo en el 0






