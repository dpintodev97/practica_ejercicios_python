#EJERCICIOS CON IF:
a = 10
b = 100
#1.
if a == 10:
    print("Es igual a 10")
else:
    print("Es diferente de 10")

#2.
if a == 10 and b==10:
    print("Es igual a 10")
elif a == 10:
    print("Solo a es igual a 10")
elif b == 10:
    print("B es igual a 10")
else:
    print("Niguno es igual a 10")

#3.
if a % 2 != 0 and b % 2 != 0:
    print("A y B son impares")
else:
    print("A y B no son impares")

#EJERCICIOS CON WHILE:
i = 10
#2.Defina una estructura de control que solo imprima i una vez:

while i == 10:
    print(i)
    break
#3.Defina una estructura de control que imprima i solo si el valor de i es par:
while i % 2 == 0:
    print(i)
    break  

#4.
i = 0
while i < 10:
    i += 1
    if i == 6:    
        print("Ejecución terminada en: ",i)
        break

#EJERCICIOS CON FOR:
a = ['Hello', "World"]
b = ['Python',3.9]
c = 'HelloWordPython'

#1.
for i in c:
    print("Recorro e imprimo todos los caracteres de c: ",i)
#2.
#Muestra todos los valores de a.
for i in a:
    print("Muestro todos los valores de a: ",i)

#3.Muestra : cada valor de a y b mostrando cada elemento de a con el de la misma posición de b sin utilizar los índices de posición !. <------ Uso de range para recorrer listas y len para saber la longitud de la lista
for i in range(len(a)):
    print(a[i], b[i])
#NOTA: 
""" len devuelve la longitud de la lista, cuántos elementos hay en a
range(n) : genera una secuencia de números desde 0 hasta n-1.
En este caso, range(len(a)) genera : secuencia de núm que va desde 0 hasta el tamaño de la lista a (sin incluir len(a)).
FOR:
Itera sobre los números generados por range(len(a)), que en este caso serían los índices 0, 1, 2, y lo hace hasta que llega al final de la lista a.
En cada iteración, i toma el valor de cada número en el rango generado.

print(a[i], b[i]):
En cada iteración, imprime el elemento en la posición i de las listas a y b.
Usando el índice i, el código accede a los elementos de a y b y los imprime en la misma línea, separados por un espacio.
"""

#4.Muestra en cada iteración el valor y su índice para los elementos de b.
for i in range(len(b)):
    print("Valor: ",b[i], ", con índice: ",i)






#EJERCICIOS CON LISTAS POR COMPRENSION:
