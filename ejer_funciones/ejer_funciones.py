"""
FUNCIÓN PYTHON: 
.Es un bloque de código con un nombre específico que encapsula un conjunto deoperaciones. 
.Pueden tomar parámetros de entrada y devolver resultados y parámetros de salida, siendo invocadas desde diferentes partes de un programa para llevar a cabo una tarea específica.
"""
#Ejemplo de función con uso real pidiendole al usuario el valor del parámetro r:
#1.Definimos la funcion con parámetro r:
def circle_area(r):
    area = 3.14 * r**2
    return area

#2.Llamamos a la funcion y pedimos al usuario el valor del parámetro r:
circulo = circle_area(float(input("Ingrese el radio del circulo: ")))

#3.Imprimimos el resultado:
print(f"El area del circulo es: {circulo}")
#print("El area del circulo es: ", circulo)

#NOTA RECORDATORIO: el primer print con "f-string" es el recomendado en Python 3.6. y forma moderna de formatear cadenas; es lo mismo que el segundo print pero con permite incrustar variables directamente dentro de una cadena usando {}; es más compacto y legible para concatenar texto y valores; admite expresiones complejas dentro de los corchetes {}

#-------------------EJERCICIO CON FUNCIONES: ---------------------------
