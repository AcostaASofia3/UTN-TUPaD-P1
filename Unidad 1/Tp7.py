#Ejercicio 1 
#diccionario original con los precios de las frutas
precios_frutas = {"Banana": 1200, "Anana": 2500, "Melon": 3000, "Uva": 1450}
#print(precios_frutas)

#Añadimos las nuevas frutas al diccionario
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)#mostramos el diccionario completo


#Ejercicio 2 
#creamos el diccionario inicial
precios_frutas = {"Banana": 1200, "Anana": 2500, "Melon": 3000, "Uva": 1450}


#se agregan las nuevas frutas
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print("Diccionario con todas las frutas agregadas: ")
print(precios_frutas)
#actualizamos los precios de las frutas
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

print("\nDiccionario con los precios actualizados: ")
print(precios_frutas) #Mostrar el diccionario final

#Ejercicio 3
#Diccionario con frutas y precios
precios_frutas = {
    "Banana": 1330, 
    "Anana": 2500, 
    "Melon": 2800, 
    "Uva": 1450,
    "Naranja": 1200,
    "Manzanan": 1700,
    "Pera": 2300
}
#Se crea una lista que contendra solo las frutas
precios_frutas = list(precios_frutas.keys())

#Mostramos la lista
print("Lista de frutas sin precios: ")
print(precios_frutas) 

#Ejercicio 4
#Diccionario con contactos iniciales
contactos_telef = {
    "Juan": "123456", 
    "Ana": "987654"
}
for i in range(5):#bucle para agregar contactos nuevos
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el numero telefonico: ")
    contactos_telef[nombre] = telefono#para guardar en el diccionario
#Mostramos todos los contactos guardados
print("\nAgenda completa: ")
print(contactos_telef)

#pedimos un nombre para consultar su numero
nombre_buscar = input("\nIngrese el nombre del contacto que buscar: ")
#Para verificar si existe en el diccionario
if nombre_buscar in contactos_telef:
    print(f"El numero de {nombre_buscar} es: {contactos_telef[nombre_buscar]}")
else:
    print("Ese contacto no existe en la agenda")


#Ejercicio 5

frase = input("Ingrese la frase: ")#pedimos la frase

palabras = frase.split()#convertimos la frase en una lista de palabras

palabras_unicas = set(palabras)#para crear un conjunto con las palabras unicas
recuento = {}#creamos un diccionario vacio para contar las repeticiones

for palabra in palabras:#para contar cuantas veces aparece cada palabra
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"\nPalabras unicas: {palabras_unicas}")#mostramos el resultado
print(f"Recuento: {recuento}")

#Ejercicio 6
alumnos = {}#Para crear el diccionario vacio donde se guardaran los alumnos y sus 3 notas

for i in range(3):#bucle para ingresar 3 alumnos
    nombre = input("Ingrese el nombre del alumno: ")#se solicits el nombre del alumno
    #solicitamos las notas y lo convertimos en entero
    nota1 = int(input("Ingrese la primera nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercer nota: "))
  
#guardamos en el diccionario la clave "nombre" con el valor una tupla de 3 notas
    alumnos[nombre] = (nota1, nota2, nota3)


for nombre, notas in alumnos.items():#calcular y mostrar el promedio de cada alumno
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#Ejercicio 7
parcial_1 = {"Ana", "Luis", "Juan", "Sofia"}
parcial_2 = {"Sofia", "Luis", "Miguel", "Marta"}

print("Aprobaron ambos parciales:", parcial_1 & parcial_2)#estudiantes que aprobaron ambos parciales(interseccion)
print("Aprobaron solo uno de los dos:", parcial_1 ^ parcial_2)#estudiantes que aprobaron solo uno de los dos(diferencia)
print("Lista total de estudiantes que aprobaron al menos un parcial:", parcial_1 | parcial_2)#estudiantes que aprobaron al menos un parcial(union)

#Ejercicio 8
#Creamos un diccionario inicial con algunos productos y su stock
productos = {
    "Jabon": 20,
    "yerba": 10,
    "Pan": 5,
    "Leche": 15
}    
#pedimos al usuario el nombre del producto que quiere consultar
producto = input("ingrese el nombre del producto que desea consultar: ")

if producto in productos: #para verificar si el producto existe en el diccionario
    print(f"El producto {producto} tiene {productos[producto]} unidades en stock")# si existe, mostramos cuantas unidades hay

    agregar = input("¿Desea agregar un nuevo producto? (si/no):" )#Preguntamos si quiere agregar mas unidades
    if agregar.lower() == "si":
        unidades = int(input("Ingrese cuantas unidades desea agregar: "))
        productos[producto] += unidades #Para sumar el stock
        print(f"Producto {producto} agregado con {unidades} unidades")
    else:
        print("No se agrego ningun producto nuevo")    
else: 
    #si el producto no exite, preguntamos si desea agregar como nuevo
    print(f"El producto {producto} no se encuentra en el stock")
    nuevo = input("Desea agregarlo como nuevo producto? (si/no): ")
    if nuevo.lower() == "si":
        unidades = int(input("Ingrese la cantidad de unidades para este nuevo producto: "))
        productos[producto] = unidades#para agregar el nuevo producto al diccionario 
        print(f"Producto {producto} agregado con {unidades} unidades")
    else:
        print("No se agrego ningun producto nuevo")
#mostramos el stock actualizado de todos los productos
print("\nStock actualizado de productos:")
print(productos)

#Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunion",
    ("Martes", "15:00"): "Clase de ingles",
    ("Miercoles", "11:00"): "Capacitación del personal",
    ("Jueves", "08:00"): "Conferencias",
    ("Viernes", "16:30"): "Eventos de formacion"
}

dia = input("Ingrese el dia: ")#Se pide al usuario que ingrese un dia
hora = input("Ingrese la hora: ")#Se pide al usuario que ingrese una hora
if (dia, hora) in agenda:#se comprueba si la tupla existe como clave en el diccionario
    print(f"En {dia} a las {hora} hay: {agenda[(dia, hora)]}")#si existe, debe mostrar el evento correspondiente
else:
    print("No hay actividades resgistradas en ese horario")#si no existe, debe informar que no hay actividades

#Ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"} #Diccionario original
invertido = {} #para crear el nuevo diccionario

#Invertir claves y valores
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario inverido:", invertido)