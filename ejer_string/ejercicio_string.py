"""
Define una variable con un string con el valor “ Master Python”.
Muestra la longitud de la variable anterior.
Muestra el primer carácter del string.
Muestra el penúltimo carácter del string.
Elimina los espacios iniciales del string.
Muestra los caracteres en posiciones impares.
Convierte todo el string en minúscula.
Separa el string por espacios en blanco.
Reemplaza “python” por “JAVA”.
"""

mi_string = "Master Python"

print("Longitud del string: ", len(mi_string))
print("Primer carácter: ", mi_string[0])
print("Penúltimo carácter: ", mi_string[-2])
print("String sin espacios iniciales: ", mi_string.lstrip())
print("Carácteres en posiciones impares: ", mi_string[1::2])
print("String en minuscula: ", mi_string.lower())
print("String reemplazado: ", mi_string.replace("python", "JAVA"))

#.lstrip() elimina los espacios en blanco del principio de la cadena, pero deja los espacios al final.
#.rstrip() elimina los espacios en blanco del final de la cadena, pero deja los espacios al principio.
#.strip() elimina los espacios en blanco de ambos extremos de la cadena.

#mi_string[1::2] --> es un slice (rebanado) de la cadena usando notación de índices. 

#   En Python, podemos acceder a partes de una cadena utilizando índices y la sintaxis de slice: 
#   mi_string[inicio:fin:paso]. El paso es el tercer valor y nos indica con qué intervalo tomamos 
#   los elementos de la cadena.

#La notación mi_string[1::2] significa:
#   1: Comienza desde el índice 1 (es decir, el segundo carácter de la cadena, porque los índices empiezan desde 0).
#   ::: Esto significa que tomamos la cadena hasta el final.
#2: El paso es 2, por lo que se tomarán los caracteres en posiciones impares (índices 1, 3, 5, 7...).