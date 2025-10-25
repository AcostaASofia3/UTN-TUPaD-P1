#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
pi = 3.14
def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio
radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

#Ejercicio 5
def segundos_a_horas(segundos):
   horas = segundos / 3600
   return horas
segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"(segundos) segundos equivalen a {horas:.2f} horas")

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese el numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return(suma,resta,multiplicacion,division) 

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")

#Ejercicio 8
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2) 
    return imc

peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
imc = calcular_imc(peso, altura)
print (f"El indice de masa corporal (IMC) es:{imc:.2f} ")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
celsius = float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en fahrenheit es:{fahrenheit:.2f}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
promedio = calcular_promedio(a,b,c)
print(f"El promedio de los tres numeros es: {promedio:.2f}")