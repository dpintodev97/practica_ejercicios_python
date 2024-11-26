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