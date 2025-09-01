
#Ejercicio 1 "Mayor de Edad"
#Paso 1: pedimos la edad al usuario
edad = int(input("Ingrese la edad: "))
#Paso 2: Se compara si es mayor a 18 
if edad > 18:
    print ("Eres mayor de edad")
else:
    print ("No eres mayor de edad")
#Paso 3: Mostramos el resultado según la condición

#Ejercicio 2 "Solicitud de nota al usuario"
#Paso 1: solicitamos la nota
nota = float(input("Ingrese la nota: "))
#Paso 2: si la nota es >=6, esta aprobado o en caso contrario estara desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("desaprobado")

#Ejercicio 3 "Solicitar numeros pares"
#Paso 1:Pedimos un numero
num = int(input("Ingrese el numero: "))
#Paso 2: se utiliza el operador modulo (%) para ver si es par
if num % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")
#Paso 3: mostramos el mensaje correspondiente

#ejercicio 4 "categorias por edad"
#Paso 1: solicitamos la edad    
edad = int(input("Ingrese su edad: "))
#Paso 2: se utiliza condiciones encadenadas (if/elif/else)
if edad < 12:
    print ("niño/a")
elif 12 <= edad < 18:
    print ("adolescente")
elif 18 <= edad < 30:
    print ("adulto/a joven")
else:
    print ("adulto/a")
#Paso 3: se realizo la clasificación en niño, adolescente, adulto joven o adulto.

#Ejercicio 5 "validar longitud de contraseñas"
#Paso 1: solicita la contraseña
contraseña = input("introduzca la contraseña: ")
#Paso 2: se verifica la longitud utilizando len()
#Paso 3: si esta en el rango, es valido, si no se mostrara un mensaje de error
if 8 <= len(contraseña) <= 14:
    print("Ingreso la contraseña correcta")
else:
    print ("por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6 "Lista numeros aleatorios"
#Paso 1: generamos 50 numeros aleatorios entre 1 y 100
from statistics import median, mean, multimode
import random
num_aleatorio = [random.randint(1, 100) for _ in range (50)]

#Paso 2: se calcula la media, mediana y moda
m = mean(num_aleatorio)
med = median(num_aleatorio)
modos = multimode(num_aleatorio)
mod = modos[0]

print("Lista:", num_aleatorio)
print(f"media: {m:.2f} | mediana: {med:.2f} | moda:{mod}")
#Paso 3: Se analiza la relacion entre ellos para identificar sesgo
if m > med > mod:
    print ("sesgo positivo (a la derecha)")
elif m < med < mod:
    print ("sesgo negativo (a la izquierda)")
elif abs(m - med) < 1e-9 and med == mod:
    print("sin sesgo")
else:
    print ("no se puede determinar un sesgo claro con estos valores")
#Paso 4: mostramos los resultados

#Ejercicio 7 "Programa que solicite frase o palabra al usuario"
#Paso 1: pedimos un texto
texto = input("Ingrese la palabra o frase: ")
#Paso 2: revisamos la ultima letra
if not texto:
    print ("")
ultima = texto[-1].lower()
vocales = set("aeiouáéíóú")
#Paso 3: si es vocal, se añade "!" al final. Si no, lo dejamos como esta.
if ultima in vocales:
    print (texto + "!")
else:
    print(texto)

#ejercicio 8 "Programa que solicite el nombre según opción"
#Paso 1: Pedimos el nombre
nombre = input("ingrese su nombre: ")
#Paso 2: preguntamos una opcion: 1, 2, 3.
#Paso 2: Segun la opcion: mayusculas, minusculas, titulo
opcion = input("elige la opcion 1 (MAYUSCULAS), 2 (MINUSCULAS), o 3 (Titulo): ")
#Paso 3: mostramos el resultado
if opcion == "1":
    print (nombre.upper())
elif opcion == "2":
    print (nombre.lower())
elif opcion == "3":
    print (nombre.title())
else:
    print ("opcion incorrecta")

#ejercicio 9 "Programa que solicite al usuario la magnitud de un terremoto"
 
#Paso 1: pedimos la magnitud del terremoto
magnitud = float(input("ingrese la magnitud del teremoto: "))
#Paso 2: Usamos rangos para clasificar el nivel
#Paso 3: Mostramos la categoria correspondiente
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print ("leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print ("moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print ("fuerte (puede causar daños en estructuras debiles)")
elif 6 <= magnitud < 7:
    print("muy fuerte(puede causar daños significativos)")
else:
    print("extremo(puede causar graves daños a gran escala)")    


#ejercicio 10 "Programa que solicite al usuario el hemisferio"
#Paso 1: solicitamos el hemisferio (Norte o Sur)
hemisferio = input("Hemisferio (N/S): ").strip().upper()
#Paso 2: Pedimos mes y dia
mes = (int(input("Mes (1-12): ")))
dia = (int(input("Dia (1-31): ")))
fecha = (mes, dia)
#Paso 3: Se define los rangos de fechas para cada estacion segun el hemisferio
#Paso 4: se determinan las estaciones correspondientes
if hemisferio == 'N':
    if (fecha >= (12,21)) or (fecha <= (3,20)):
        estacion = "invierno"
    elif (fecha >= (3,21)) and (fecha <= (6,20)):
        estacion = "primavera" 
    elif (fecha >= (6,21)) and (fecha <= (9,20)):
        estacion = "verano"
    else:
        estacion = "otoño"

if hemisferio == 'S':
    if (fecha >= (12,21)) or (fecha <= (3,20)):
        estacion = "verano"
    elif (fecha >= (3,21)) and (fecha <= (6,20)):
        estacion = "otoño" 
    elif (fecha >= (6,21)) and (fecha <= (9,20)):
        estacion = "invierno"
    else:
        estacion = "primavera"
else:
    print("Ingreso el hemisferio invalido. Utilice 'N' o 'S'. ")
print = ("Estacion: ", estacion)