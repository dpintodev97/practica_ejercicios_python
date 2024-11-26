#Ejercicios con diccionarios:

"""Diccionario: es una estructura de datos que almacena pares de clave-valor, donde cada clave debe ser única 
    e inmutable (como cadenas, números o tuplas), y cada valor puede ser de cualquier tipo.
    Es mutable: puedes agregar, modificar o eliminar elementos.
"""
#diccionario con las claves: coche, motocicleta, camión y los valores: 10, 20 y 30 respectivamente.

#2 FORMAS DE DEFINIR UN diccionario en Python:
mi_diccionario = {"coche": 10, "motocicleta": 20, "camión": 30}
mi_diccionario_2 = dict(coche=10, motocicleta=20, camión=30)

print(mi_diccionario)
print(mi_diccionario_2)

print("Valores del diccionario: ",mi_diccionario.values())
print("Claves del diccionario: ",mi_diccionario.keys())

# Podemos convertir a listas cuando necesitemos características que las vistas del diccionario
# no ofrecen (indexación, modificación, agregación de elementos etc.):

valores = list(mi_diccionario.values())
claves = list(mi_diccionario.keys())

print("Lista de valores:", valores)  # [10, 20, 30]
print("Lista de claves:", claves)    # ['coche', 'motocicleta', 'camión']

#Mostrar el valor de coche (10) con .get("coche"):
print("Muestro valor de coche: ", mi_diccionario.get("coche"))
#Muestro valor de coche(10) con ÍNDICE["coche"]
print("Muestro valor de coche con ÍNDICE: ", mi_diccionario["coche"])

#Añade avión al diccionario.
mi_diccionario["avión"] = 100
print("Agrego avión: ",mi_diccionario)