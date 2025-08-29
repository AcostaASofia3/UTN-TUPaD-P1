#EL TRABAJO 1 COMPLETO
#Ejercicio-1
print("¡Hola Mundo!")

#Ejercicio-2
nombre = input("Ingrese su nombre: ")
saludo = f"Hola {nombre}"
print(saludo)

#Ejercicio-3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese la edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido} tengo {edad} años, y vivo en {lugar}")

#Ejercicio-4
import math
radio_c = float(input("ingrese el radio de un circulo: "))
area_c = math.pi * (radio_c) **2
perimetro_c = 2* math.pi * radio_c
print (f"el area del circulo es: {area_c} y el perimetro es: {perimetro_c} ")  ) 

#Ejercicio-5
segundos = float(input("ingrese la cantidad de segundos: "))
horas = round(segundos / 3600, 2) 
print(f"el equivalente a {segundos} y segundos son {horas} horas")

#Ejercicio-6
numero = int(input("ingrese un numero: "))

print(f"tabla de multiplicar del {numero}: ")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


#Ejercicio-7
num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

suma_num1_num2 =  num1 + num2
division_num1_num2 = round(num1 / num2, 2)
multiplicacion_num1_num2 = num1 * num2
resta_num1_num2 = num1 - num2

print (f"""
    resultado suma: {suma_num1_num2}
    resultado resta: {resta_num1_num2}
    resultado multiplicacion: {multiplicacion_num1_num2}
    resultado division : {division_num1_num2}
        """)

#Ejercicio-8
peso=float(input("Ingrese su peso en kilogramos: "))
altura=float(input("Ingrese su altura"))
imc = round (peso / altura **2, 2)
print(f"el IMC es: {imc}") 


#Ejercicio-9
celsius = float(input("Ingrese la Temperatura en °C: "))
fahrenheit = round((9/5)*celsius+32,2)
print(f"{celsius} °C equivale a {fahrenheit} °F")

#Ejercicio-10
num1 = float(input("Ingresar el primer numero: "))
num2 = float(input("Ingresar el segundo numero: "))
num3 = float(input("Igresar el tercer numero: "))
suma_1_2_3 =num1 + num2 + num3
promedio_1_2_3 = round(suma_1_2_3/3, 2)
print(f"el resultado de los tres numeros es: {promedio_1_2_3}")