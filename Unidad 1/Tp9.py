#Recursividad
###Ejercicio 1###
def factorial(n):
    if n == 0 or n == 1:    #caso base
        return 1
    else:
        return n * factorial(n - 1) #para el llamado recursivo
#se pide un numero y se muestran todos los factoriales desde 1 hasta ese numero
num = int(input("Ingrese un numero: "))

for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

###Ejercicio 2###
def fibonacci(n):
    if n == 0:          # primer caso base
        return 0
    elif n == 1:        # segundo caso base
        return 1
    else:
        return fibonacci (n - 1) + fibonacci (n - 2) #para recursion
#se pide un numero y se muestra su valor 
num = int(input("Ingrese un numero: "))
print(f"Fibonacci({num}) = {fibonacci(num)}")


###Ejercicio 3###
def potencia(base, exponente):
    if exponente == 0:      #caso base
        return 1
    else:
        return base * potencia(base, exponente - 1) #para recursion
#se ingresa base y exponente
b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))

resultado = potencia(b, e)
print(f"{b}^{e} = {resultado}")


###Ejercicio 4###
def decimal_a_binario(n):
    if n == 0:
        return "0"  #primer caso base
    elif n == 1:
        return "1"     #segundo caso base
    else:
        #para llamar recursivamente con n//2 y agregar el resto al final
        return decimal_a_binario (n // 2) + str (n % 2)
#se ingresa un numero y se convierte a binario
num = int(input("Ingrese un numero entero positivo: "))
print(f"El numero {num} en binario es: {decimal_a_binario(num)}")


###Ejercicio 5### 
def es_palindromo(palabra):
    if len(palabra) <= 1:      #caso base
        return True
    if palabra[0] != palabra[-1]: # si las puntas no coinciden, no sera palindromo
        return False
    return es_palindromo(palabra[1:-1])#recursion quitando los extremos
#entrada del usuario
palabra = input("Ingrese una palabra: ")
print(es_palindromo(palabra))

###Ejercicio 6###
def suma_digitos(n):
    if n < 10:      #caso base
        return n
    else:
        #ultimo digito: n % 10
        #el resto del numero: n // 10
        return (n % 10) + suma_digitos(n // 10)
num = int(input("Ingrese un numero: "))
print(suma_digitos(num))

###Ejercicio 7###
def contar_bloques(n):
    if n == 1:      #caso base
        return 1
    else:
        return n + contar_bloques(n - 1) #recursion sumando el nivel actual
num = int(input("Ingrese la cantidad de bloques del nivel mas bajo: "))
print(contar_bloques(num))

###Ejercicio 8###
def contar_digito(numero, digito):
    if numero == 0:     #caso base
        return 0
    else:
        ultimo = numero % 10    #para obtener el ultimo digito
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito) #recursion
#entrada del usuario
n = int(input("Ingrese un numero: "))
d = int(input("Ingrese el digito a contar: "))
print(contar_digito(n, d))