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
