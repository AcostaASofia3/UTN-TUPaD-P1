#Trabajo Completo Estructuras Repetitivas

#Ejercicio 1
 
print ("Imprimir numeros enteros")
#utilizo bucle for, ya que genera los numeros desde 0 hasta 100
for num in range (0,101):
#en cada vuelta, muestro el valor de num
    print(num, end=" ")
print ("\n")

#Ejercicio 2
#pido al usuario que ingrese un numero entero
numeros = (input("Ingrese un numero entero: ")).split()

for num in numeros:
    aux = abs(int(num))
    cont = 0
#si el numero es 0, tiene un digito
    if aux == 0:
        cont = 1
    else:
#mientras el numero sea mayor que 0
        while aux > 0:
            aux //= 10
            cont += 1
#suma 1 al contador por cada digito eliminado

#muestra el resultado
print (f"el numero {num} tiene {cont} digitos")

#Ejercicio 3
 
#solicito dos numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#decidir cual es el menor y cual es el mayor
if num1 < num2:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor = num1
#acumulador: arranco en 0
total = 0
#debo recorrer los numeros que estan en el medio y los voy sumando 
for i in range (menor + 1, mayor):
      total = total + i
#muestro el resultado final
print ("La suma de los numeros entre", menor, "y", mayor, "es:", total)

#Ejercicio 4
 
#acumulador arranca en 0
total = 0
#Mientras el numero no sea 0, seguira sumando
while True:
    num = int(input("Ingrese otro numero (0 para terminar): "))
    if num == 0:
        break
    total += num
#cuando el usuario ingresa 0, se corta el while y muestra la suma 
print(f"La suma total es: {total}")

#Ejercicio 5

import random
#genero un numero secreto
secreto = random.randint(0, 9)
intentos = 0
numero = -1
#pido un numero al usuario hasta que acierte
while numero != secreto:
    numero = int(input("Adivina un numero aleatorio entre 0 y 9: "))
    intentos = intentos + 1
    if numero < secreto:
        print("El numero es mas alto.")
    elif numero > secreto: 
        print ("El numero es mas bajo.")
#Cuando acierta, muestra cuantos intentos utlizo  
print("¡Correcto! Lo adivinaste en", intentos, "intento(s).")

#Ejercicio 6

#utilizo for hasta que baje de 100 a 0, y para luego preguntar si es par.
for i in range (100, -1, -1):
    if i % 2 == 0:
        print (i)

#Ejercicio 7

#pido al usuario un numero entero positivo
n = (int(input("Ingrese un numero entero positivo: ")))
#valida si el numero es negativo
if n < 0:
    print ("Debe ser un numero positivo")
else:
#se usa una formula matematica para calcular la suma
    total = n * (n + 1) // 2
    print ("La suma desde 0 hasta", n, "es:", total) 
#muestra el resultado al usuario

#Ejercicio 8
 
#hice 4 contadores
pares = 0
impares = 0
positivos = 0
negativos = 0
#con for de 100 vueltas voy pidiendo numeros
for i in range(100):
    num = int(input(f"Ingrese el numero {i+1}/100: "))
#segun lo que de el numero, va aumentando el contador que corresponde
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1
#muestro los resultados
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)



#Ejercicio 9 

#acumular suma
suma = 0
#utilizo for de 100 vueltas y voy pidiendo numeros y sumando.
for i in range (100):
    num = int(input(f"Ingrese el numero {i+1}/100: "))
    suma = suma + num
#divido la suma por 100, que eso es la media
media = suma / 100
print("La suma total es:", suma)
print("La media es:", media)

#Ejercicio 10

#pido al usuario un numero entero
n = int(input("Ingrese un numero entero: "))
signo = 1

if n < 0:
    signo = -1
    n = -n

invertido = 0
#se van sacando digitos y armando el numero invertirdo
while n > 0:
#sacar el ultimo digito con % 10 y luego armar el nuevo numero multiplicado por 10
#y luego sumar ese digito, al final dividir con // 10 para ir sacando digitos. 
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10
invertido = invertido * signo
print ("Numero invertido:", invertido)