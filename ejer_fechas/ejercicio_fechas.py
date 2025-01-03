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

# 1.Convierte cada cadena de la lista fechas a un objeto datetime.date 
fechas_date = [datetime.strptime(fecha, "%Y-%m-%d").date() for fecha in fechas]
#fechas_date <- OBJETO DATETIME QUE USARÉ EN OTROS EJERCICIOS

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

#3.Combina cada elemento de los objetos date y los objetos time de los dos ejercicios anteriores para crear una
#lista de objetos datetime:

# Combinar con zip para crear una lista de objetos datetime, que ITERE simultáneamente cada elemento de cada lista:
lista_objetos_datetime = [datetime.combine(fecha, hora) for fecha, hora in zip(fechas_date, horas_time)]
print("La lista de objetos datetime es: ", lista_objetos_datetime)
#NOTA: datetime.combine ----> combina dos objetos date y time en un solo objeto datetime

#4.Calcula los días de diferencia que hay entre los objetos date resultantes del ejercicio 1 y la fecha actual.

actual_date = datetime.now().date() #del actual objeto datetime solo quiero la fecha, por eso el .date()
day_diff = actual_date - fechas_date[0] #resta la fecha actual menos la primera fecha de la lista
print("Días de diferencia entre fechas: ", day_diff.days)   

#Elige una fecha de los objetos date resultantes del ejercicio 1 y cambiar su año a 2025.
#nueva variable que toma por ej, el elemento tercero de la lista, y reemplaza su año por 2025:
new_date = fechas_date[2].replace(year=2025) 
print("Nueva fecha cambiando año por 2025: ", new_date)

#Convierte cada objeto datetime resultante del ejercicio 3 en una cadena con el formato DD/MM/YYYY HH:MM
datetime_string = [dt1.strftime("%d/%m/%Y %H:%M")for dt1 in lista_objetos_datetime]
print("En formato cadena de texto: ", datetime_string)