#EJERCICIOS DE LISTAS:
"""
lista en Python: es un tipo de estructura de datos que permite almacenar una colección de elementos de cualquier 
    tipo (no como los arrays). Son ordenadas, mutables (puedes cambiar sus elementos después de haberlas creado) 
    y permiten elementos duplicados.
"""

mi_lista = [10, 20, "Hello", 20.5]

#Añade “Word” al final de la lista.
mi_lista.append("Word")
print(mi_lista)

#Añade “Python” al principio de la lista.
mi_lista.insert(0,"Python")
print(mi_lista)

#Elimina el segundo valor de la lista (si quieres eliminar explícitamente usa remove; con pop coge el índice)
mi_lista.pop(1)
print(mi_lista)

#Crea una segunda lista con los valores 20, 40, ‘Bye’ (utiliza una forma diferente que en el inicio)
mi_lista_2 = [20, 40]
mi_lista_2.extend(["Bye"])
print(mi_lista_2)

#Une las dos listas y muestra la lista final.
mi_lista_3 = mi_lista + mi_lista_2
print(mi_lista_3) 

"""
PYTHON vs JAVA
    En Python:

    .Las listas son estructuras de datos dinámicas y flexibles que pueden contener elementos de tipos diversos.
    .Los arrays de Python son más eficientes para manejar datos homogéneos (todos del mismo tipo), 
        pero no son tan comunes para la mayoría de los casos como las listas.

    En Java:

    .List es una interfaz que se implementa en clases como ArrayList y LinkedList.
    .Las listas en Java son genéricas y más orientadas a tipos específicos, lo que proporciona más control 
        sobre el tipo de elementos que puedes almacenar."""