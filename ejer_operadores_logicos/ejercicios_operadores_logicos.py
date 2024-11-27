'''NOTA: '==' compara el contenido de los objetos. Si dos listas tienen los mismos elementos en el mismo orden, ==  devuelve True, independientemente de si son el mismo objeto en memoria o no.

Mientars que 'is' compara si dos variables apuntan al mismo objeto en memoria. Si las dos variables se refieren al mismo objeto en la memoria, is devuelve True, de lo contrario devuelve False
'''

#EJERCICIOS CON OPERADORES ARITMETICOS
a, b, c = 50, 5.0, 100  # Asignación múltiple (si se escribe de seguido (a=50, b=5.0....)lo interpreta como una Tupla)
d = a + b
e = a - b
f = d * e
g = f / a
h = f % a
print("Variable soriginales sobre las que hacer operaciones: ", a, b, c, "; y las operaciones: ", d, e, f, g, h)

#EJERCICIOS OPERADOR DE COMPARACIÓN
#Define las variables a y b con los valores 50 y 10
a = 50
b = 10  
#Comprueba si a y b son iguales.
a == b
print(a == b)
#Comprueba si a y b son distintos.
a != b
print(a != b)
#Comprueba si a es mayor que b.
a > b
print(a > b)
#Comprueba si a es menor o igual que b.
a <= b
print(a <= b)

#EJERCICIOS OPERADOR DE ASIGANCION:
#Define una variable y asígnale el valor 999.
mi_variable = 999
#Suma 1 a la variable anterior.
mi_variable += 1
print(mi_variable)
#Resta 10 a la variable anterior.
mi_variable -= 10
print(mi_variable)
#Multiplica por 10 la variable anterior.
mi_variable *= 10
print(mi_variable)
#Divide entre 5 la variable anterior.
mi_variable /= 5
print(mi_variable)
#Asigna a la variable inicial el resultado del módulo de 60
mi_variable %= 60
print(mi_variable)

#EJERCICIOS CON OPERADORES LOGICOS
#Crea las variables a, b, c y d con los valores 10, 100, 200 y 300 respectivamente.
a = 10
b = 100
c = 200
d = 300 
print(a, b, c, d)

#Comprueba si a es mayor que b y c es menor que d.
a > b and c < d
print(a > b and c < d) #False

#Comprueba si la suma de a y b es mayor o igual que c o la suma de b y c es mayor o igual que d.
a + b >= c or b + c >= d
print(a + b >= c or b + c >= d) #True 

#EJERCICIOS CON OPERADORES DE PERTENENCIA:
list1 = [1, 2, 3, 4, 5]
list2 = ['Hello', 'World', 'Python']
list3 = ['Operator','Membership', 100, 200]

#Comprueba si 5 está en list1.
5 in list1
print(5 in list1) #True

#Comprueba si 'Python' está en list2.
"Hello" and 'Python' in list2
print("Hello" and 'Python' in list2) #True

#Comprueba si list2 es igual que list3.
list2 is list3
print(list2 is list3) #False

'''NOTA: '==' compara el contenido de los objetos. Si dos listas tienen los mismos elementos en el mismo orden, ==   devuelve True, independientemente de si son el mismo objeto en memoria o no.

Mientars que 'is' compara si dos variables apuntan al mismo objeto en memoria. Si las dos variables se refieren al mismo objeto en la memoria, is devuelve True, de lo contrario devuelve False
'''

#EJERCICIOS CON OPERADORES BIT A BIT:
'''Estos tipos de operadores utiliza números binarios internamente. Es decir, operan sobre los bits individuales de los números, no sobre su valor completo. 

Operadores bit a bit son muy útiles cuando necesitas manipular los bits de un número directamente. 
Los operadores &, |, y ^ realizan comparaciones bit a bit, ~ invierte los bits, mientras que << y >> desplazan los bits hacia la izquierda o la derecha, respectivamente.
'''

a = 1 #a = 1 en binario es 0001
b = 2 #b = 2 en binario es 0010

#Operador AND
a & b
print(a & b) #El resultado es 0000, que en decimal es 0 <--

#Operador XOR: hace XOR donde el resultado es 1 si los bits son diferentes, y 0 si son iguales:
a ^ b
print(a ^ b) #El resultado es 0011, que en decimal es 3.

#Operador OR: hace OR donde el resultado es 1 si al menos uno de los bits es 1, y 0 solo si ambos son 0
a | b
print(a | b) #El resultado es 0011, que en decimal es 3.

#Operador NOT: hace una operación NOT bit a bit, que invierte todos los bits del número.Cambia 1 a 0 y 0 a 1:
~a
print(~a) #resu: es 1110, que en formato de complemento a 2 (representación binaria de números negativos) es -2.
#NOTA: Alt Gr + 4 ---> ~ 

#Operador LEFT SHIFT: hace desplazamiento a la izquierda de los bits, lo que equivale a multiplicar el número por 2 elevado al número de posiciones desplazadas.
a << 2
print(a << 2) #resultado : 0100, que en decimal es 4 (equivalente a 1 * 2^2)
'''0001  (a)
    << 2
    ----
    0100  (resultado)
'''

#Operador RIGHT SHIFT: desplazamiento a la derecha de los bits, lo que equivale a dividir el número por 2 elevado al número de posiciones desplazadas (y redondear hacia abajo si es necesario):
a >> 2
print(a >> 2) #El resultado es 0000, que en decimal es 0 (equivalente a 1 // 2^2).
'''
    0001  (a)
    >> 2
    ----
    0000  (resultado)
'''

#EJERCICIOS CON OPERADOR DE IDENTIDAD:
a = 3
b = 3.0

a = 3
b = 3.0

# Comprueba si a es un int.
print("Tipo de dato de a es int?", type(a) is int)  # True

# Comprueba si b es un booleano.
print("Tipo de dato de b es bool?", type(b) is bool)  # False

# Comprueba si b es un float.
print("Tipo de dato de b es float?", isinstance(b, float))  # True




