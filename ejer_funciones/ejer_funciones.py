"""
FUNCIÓN PYTHON: 
.Es un bloque de código con un nombre específico que encapsula un conjunto deoperaciones. 
.Pueden tomar parámetros de entrada y devolver resultados y parámetros de salida, siendo invocadas desde diferentes partes de un programa para llevar a cabo una tarea específica.

Las funciones son objetos de PRIMERA CLASE: son tratados como cualquier otro dato como números o cadenas. 
    SE PUEDE:

    .Pasar una función como argumento a otra función. (ejercicio 6)
    .Retornar una función como resultado de otra.
    .Asignar una función a una variable.
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

#4.Función dos parámetros y devuelva multiplicación de ellos:
def producto(num1, num2):
    return num1 * num2

#EJEMPLO DE USO:
resu = producto(1, 2)
print(f"Producto: {resu}")

#5.Define una función que recibiendo dos números devuelva el módulo.

def module(num1, num2):
    return num1 % num2

resu = module(1, 2)
print(f"Módulo: {resu}")

#6.Define una función que recibiendo una función del ejercicio 4 o ejercicio 5 y dos valores numéricos devuelva su resultado.
def calc(function, num1, num2):
    return function(num1, num2) #a. Definimos la función y le pasamos los parámetros (otra funcion, dos numeros)

resu = calc(producto, 2, 5.5) #b.Invocamos la función y como parametros será producto, 2 y 5.5
print(f"Resu pasando como parámetro la función producto: {resu}")

#7.

def name_email(name, email):
    # Verifica si ambos el nombre y el email están completos
    if name != "" and email != "":
        print(f"Este es {name} y su {email}")
    # Verifica si solo el email está vacío
    elif email == "":
        print("Sin determinar")
    # Si ninguno de los dos está completo
    else:
        print("Nombre o email vacío")

# Pedir los inputs
name = input("Ingrese su nombre: ")
email = input("Ingrese su email: ")

# Llamar a la función
name_email(name, email)










