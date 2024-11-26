#EJERCICIO DE CONJUNTOS (set):
"""Conjunto (set) : es una colección de elementos no ordenados y sin duplicados. 
Los conjuntos NO mantienen el orden de los elementos (a partir de Python 3.7, el orden de inserción es preservado, 
pero no se puede contar con esto en versiones anteriores)."""

#Define un conjunto con los valores coche, motocicleta, bicicleta:
mi_set = {"coche", "motocicleta", "bicicleta"}
print(mi_set)

#CASO: quiera convertirlo a un String :mi_cadena = str(mi_set); sin embargo, siguen apareciendo llaves, por eso:
#CASO 2: convertir a String con un separador personalizado:
# Convertir a cadena de texto con un separador personalizado -----------> coche, bicicleta, motocicleta
mi_cadena = ", ".join(mi_set)
print(mi_cadena)

#Añade avión al conjunto.
mi_set.add("avión")
print(mi_set)

#Elimina coche del conjunto (también se puede usar discard)
mi_set.remove("coche")
print("Elimina coche: ", mi_set)

#Crea otro conjunto con los valores avión, coche, tractor (utiliza una forma diferente que en el punto 1).
mi_set_2 = set() #creamos el SET vacío, llamando a su CONSTRUCTOR () y añadimos elementos:
mi_set_2.add("avión")
mi_set_2.add("coche")
mi_set_2.add("tractor")
print("Otro set de manera distinta: ", mi_set_2)

#NOTA: no se puede usar extend() como en las listas, ya que los set  son estructuras desordenadas 
#    y que no permiten duplicados

#Crea otro conjunto con los valores que se repitan en los conjuntos anteriores.
mi_set_3 = mi_set.intersection(mi_set_2)
print("Set con valores que se repitan en sets anteriores: ",mi_set_3)

#Muestra un conjunto con todos los valores que pertenecen al conjunto creado en el punto 1 y punto 4:
mi_set_4 = mi_set.union(mi_set_2)  #union(): combina los valores de ambos sets
print("Set con valores unidos: ",mi_set_4)


