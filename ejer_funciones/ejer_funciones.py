"""
FUNCIÓN PYTHON: 
.Es un bloque de código con un nombre específico que encapsula un conjunto deoperaciones. 
.Pueden tomar parámetros de entrada y devolver resultados y parámetros de salida, siendo invocadas desde diferentes partes de un programa para llevar a cabo una tarea específica.
"""
#Ejemplo de función con uso real pidiendole al usuario el valor del parámetro r:
#1.Definimos la funcion con parámetro r:
"""def circle_area(r):
    area = 3.14 * r**2
    return area

#2.Llamamos a la funcion y pedimos al usuario el valor del parámetro r:
circulo = circle_area(float(input("Ingrese el radio del circulo: ")))

#3.Imprimimos el resultado:
print(f"El area del circulo es: {circulo}")
#print("El area del circulo es: ", circulo)

"""

#NOTA RECORDATORIO: el primer print con "f-string" es el recomendado en Python 3.6. y forma moderna de formatear cadenas; es lo mismo que el segundo print pero con permite incrustar variables directamente dentro de una cadena usando {}; es más compacto y legible para concatenar texto y valores; admite expresiones complejas dentro de los corchetes {}

#-------------------EJERCICIO CON FUNCIONES: ---------------------------

#1.Define una función llamada showAnimal que reciba dos argumentos name y n_legs e imprima por pantalla:

def showAnimal(name, n_legs):
    print(f"The animal {name} has {n_legs} legs.")  #<-- a.Definimos función con parámetros y lógica

#EJEMPLO DE USO:
showAnimal("dog", 4)  #<-- b.Invocamos la función las veces que quiera
showAnimal("cat", 4)

#2.Define una función que puede recibir cualquier número de argumentos e imprima cuántos argumentos ha recibido.

def n_args(*args): #a.función recibe núm indeterminado de argumentos no nombrados
    return len(args) #b.len : número de argumentos args

#EJEMPLO DE USO:
resu = n_args(1, 2, "John")
print(resu)

#3.Define una función que recibiendo dos números, devuelva la suma y la resta de ellos en una sola llamada.
def calculate(num1, num2):
    return num1 + num2, num1 - num2  #a.Retornará 2 valores, la suma y la resta y Python lo empaquetará en una tupla

#EJEMPLO DE USO:
resu_suma, resu_resta = calculate(1, 2) #b.Invocamos y descomponemos los valores devueltos en la tupla en 2 variables
print(f"Suma: {resu_suma}, Resta: {resu_resta}")







