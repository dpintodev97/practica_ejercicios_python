#EJERCICIO DE TUPLAS:
"""Tupla: es una colección de elementos NO ORDENADOS y SIN DUPLICADOS. 
    Las tuplas son inmutables (no se pueden modificar).
    A diferencia de los conjuntos (set), las tuplas sí mantienen el orden en que se agregan los elementos.
    Permiten duplicados: A diferencia de los conjuntos (set), las tuplas sí permiten duplicados."""

#Accede al primer y último elemento de la tupla e imprime sus valores:
mi_tupla = (1, 2, 3, 4, 5)
print("Primer elemento: ", mi_tupla[0])
print("Último elemento: ", mi_tupla[-1])

# Usando el constructor tuple() para crear la tupla
mi_tupla_2 = tuple(["perro", "gato", "naranja"])
print("Mi segunda tupla creada con constructor: ",mi_tupla_2)

#Concatena las dos tuplas en una nueva con el nombre ‘tupla_concatenada’:
tupla_concatenada = mi_tupla + mi_tupla_2
print("Tupla concatenada: ", tupla_concatenada)

#Cuenta el número de elementos de la tupla del punto 3
print("Conteo de tupla concatenada: ", len(tupla_concatenada))

#Encuentra el índice del elemento perro dentro de ‘tupla_concatenada’:
print("índice del elemento 'perro': ", tupla_concatenada.index("perro")) 

#Desempaqueta ‘tupla_concatenada’ en las variables (por este orden) tp1, tp2, tp3 y el resto en tp4
tp1, tp2, tp3, *tp4 = tupla_concatenada
print("Inicio de la tupla, empezando en elemento primero: ",tp1)
print(tp2) 
print(tp3)
print("Resto de la tupla: ", tp4)

mi_tupla_3 = ('coche', 'motocicleta', 'camión')
tp1, tp2, tp3 = mi_tupla_3
print("Imprime el inicio de la tupla", tp1)
print(tp2)
print(tp3)

#Imprime los valores de las variables (tp1 = coche, tp2 = motocicleta, tp3 = camon…)
# Definimos las variables
tp1 = "coche"
tp2 = "motocicleta"
tp3 = "camión"

# Imprimimos los valores de las variables
print("Imprime los valores de las variables (tp1 = coche, tp2 = motocicleta, tp3 = camión): ", tp1, tp2, tp3)

print("Añade nuevo elemento: ", tupla_concatenada + ("barco",))
#NOTA: Las tuplas en Python son inmutables, lo que significa que no puedes modificar sus elementos una vez que han sido creadas, por eso no hay add como en las listas

print("Mostrar elementos de la tupla concatenada: ", tupla_concatenada)
