#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
#llamamos a la funcion
imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!" #devuelve el texto con el nombre asignado
#solicitamos el nombre al usuario
nombre = input("Ingrese su nombre: ")
#para llamar a la funcion 
saludo = saludar_usuario(nombre)
#mostramos el resultado
print(saludo)

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#pedimos al usuario los datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

#llamamos a la funcion con los datos ingresados
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
#definimos una constante 'pi'
pi = 3.14
#Funcion que calcula el area del circulo
def calcular_area_circulo(radio):
    return pi * radio ** 2 #Devuelve el resultado del area

#funcion que calcula el perimetro del circulo 
def calcular_perimetro_circulo(radio):
    return 2 * pi * radio #devuelve el resultado del perimetro

#pedimos el valor del radio
radio = float(input("Ingrese el radio del circulo: "))

#se utiliza para llamar ambas funciones para obtener los resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

#Para mostrar los resultados con 2 decimales
print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

#Ejercicio 5

def segundos_a_horas(segundos):
   horas = segundos / 3600
   return horas#para devolver el resultado en horas

#pedimos al usuario ingresar los segundos
segundos = float(input("Ingrese la cantidad de segundos: "))

#llamamos a la funcion
horas = segundos_a_horas(segundos)

#Mostramos el resultado
print(f"(segundos) segundos equivalen a {horas:.2f} horas")

#Ejercicio 6
#se define la funcion
def tabla_multiplicar(numero):
    #se utiliza el bucle for para recorrer los numeros del 1 al 10
    for i in range(1,11):
        #para mostrar cada linea de la tabla
        print(f"{numero} x {i} = {numero * i}")
#se pide al usuario un numero
numero = int(input("Ingrese el numero para ver su tabla de multiplicar: "))
#llamamos a la funcion
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    #para evitar error si b es 0 (no se puede dividir por cero)
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    #devuelve todos los resultados como una tupla
    return(suma,resta,multiplicacion,division) 

#pedimos los numeros
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

#Llama a la funcion 
resultados = operaciones_basicas(a, b)

#Mostramos los resultados de forma clara 
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")

#Ejercicio 8
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2) 
    return imc
#solicitar datos al usuario
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
#Calcular el IMC llamando a la funcion
imc = calcular_imc(peso, altura)
#Mostrar el resultado con dos decimales
print (f"El indice de masa corporal (IMC) es:{imc:.2f} ")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
#Pedir la temperatura en celsius 
celsius = float(input("Ingrese la temperatura en grados celsius: "))
#Llamar a la funcion
fahrenheit = celsius_a_fahrenheit(celsius)
#Mostrar el resultado
print(f"La temperatura en fahrenheit es:{fahrenheit:.2f}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
#Pedimos al usuario los tres numeros
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
#llamamos a la funcion 
promedio = calcular_promedio(a,b,c)
#mostramos el resultado con 2 decimales
print(f"El promedio de los tres numeros es: {promedio:.2f}")