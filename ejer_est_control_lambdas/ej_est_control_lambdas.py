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


#EJERCICIOS CON LISTAS POR COMPRENSION:
