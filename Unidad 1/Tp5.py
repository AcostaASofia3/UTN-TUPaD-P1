#Ejercicio 5. Listas

#Ejercicio 1

notas = [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
#Mostrar la lista completa
print ("Las notas de los estudiantes es:", notas)
#calcular el promedio
promedio = sum(notas) / len(notas)
print ("El promedio de los estudiantes es:", promedio)

nota_max = max(notas) #nota mas alta
print ("La nota mas alta es:", nota_max)
nota_min = min(notas) #nota mas baja
print ("La nota mas baja es:", nota_min)

#Ejercicio 2

productos = []  #PIDE AL USUARIO QUE CARGUE 5 PRODUCTOS
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)
#Mostrar la lista ordenada alfabeticamente
print("\nLista de productos ordenados alfabeticamente:")
print(sorted(productos)) #Se utiliza sorted() para no modificar la lista original
#pregunta que producto desea eliminar
eliminar = input ("\nIngrese el producto que desea eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
#elimina la primera
    print("\nEl producto '{eliminar}' fue eliminado")
else:
    print("\nEse producto '{eliminar}' no esta en la lista")
#Muestra la lista actualizada
print ("\nLista actualizada de productos:")
print(productos)

#Ejercicio 3

import random
numeros= [random.randint(1,100) for _ in range (15)]
print(f"Lista original de 15 numeros al azar: {numeros}")
#Crear una lista para los pares y otra para los impares
pares = []
impares = []
#iterar sobre la lista original para clasificar los numeros 
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
#mostrar cuantos numeros tiene cada lista
#se utiliza la funcion len() para obtener el conteo de elementos
print(f"La lista de numeros pares contiene {len(pares)} elementos")
print(f"La lista de numeros impares contiene {len(impares)} elementos")

#Mostrar listas creadas
#Uso de estructuras repetitivas para mostrar listas
print("\nNumeros pares:")
for par in pares:
    print(par, end=" ")

print("\nNumeros impares:")
for impar in impares:
    print(impar, end=" ")
print("\n")

#Ejercicio 4

datos = [1,3,5,3,7,1,9,5,3]
#Crear una lista nueva sin elementos repetidos
listasinrepetidos = list(set(datos))
#Mostrar el resultado
print(f"La lista original es: {datos}")
print(f"La lista nueva sin numeros repetidos es:{listasinrepetidos}")

#Ejercicio 5

#Crear una lista de estudiantes
estudiantes = ["ana", "francisco", "juan", "carlos", "pedro", "maria", "laura", "rosa"]
print("Lista actual de estudiantes:")
#el bucle para mostrar cada nombre de la lista 
for nombre in estudiantes:
    print(nombre)

#Preguntar al usuario si quiere agregar o eliminar a un nuevo estudiante 
opcion = input("¿Desea 'agreagar' o 'eliminar' un estudiante? ")
opcion = opcion.lower()#convierte en minusculas asi se facilita la comparacion

#se realiza la accion solicitada
if opcion == "agregar":
#pedimos el nombre del nuevo estudiante
    nuevo_nombre = input("Escribe el nombre del estudiante que deseas agregar: ")
    estudiantes.append(nuevo_nombre)#se utiliza para poder poner el nuevo nombre al final 
    print("¡Estudiante agregado!")
    
elif opcion == "eliminar": #si la opcion es eliminar
    #se pide el nombre del estudiante a eliminar 
    nombre_eliminado = input("Escribe el nombre del estudiante que quieres eliminar: ")
    if nombre_eliminado in estudiantes: #se comprueba si el nombre esta en la lista usando in
        estudiantes.remove(nombre_eliminado)#si se encuentra lo elimina con .remove()
        print("Estudiante eliminado")
    else:
    #si la opcion no es valida
        print("No es la respuesta correcta. La lista no ha cambiado")
#Mostrar la lista final actualizada 
print ("\nLa lista final de estudiantes es:")
for nombre in estudiantes:
    print(nombre)


#Ejercicio 6
numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original:")
print(numeros)
#Rotar los elementos una posicion hacia la derecha
#primero se obtiene el ultimo numero de la lista
#El -1 siempre se refiere al ultimo elemento
ultimo_num = numeros[-1]

l_rotada = [] #Crea una nueva lista para guardar el resultado
l_rotada.append(ultimo_num) # ponemos el ultimo numero como el primer elemento de la nueva lista

#se recorre la lista original para copiar el resto de los elementos
#tambien recorre el primer elemento (indice 0) hasta el antepenultimo
for i in range(len(numeros) -1): 
#agregamos cada elemento a la nueva lista
    l_rotada.append(numeros[i])

#Mostrar la lista rotada
print("\nLista despues de rotar a la derecha:")
print(l_rotada)


#Ejercicio 7
#definir la matriz con 7 dias y 2 temperaturas por dia (minima y maxima)
#cada lista interna representa un dia
temp_semana = [
    [24,34],
    [28,37],
    [16,33],
    [11,23],
    [14,25],
    [16,27],
    [21,30],
] 
#Crea listas para guardar las temperaturas minimas y maximas por separado  
minimas = []
maximas = []
#recorre la matriz para llenar las listas minimas y maximas
for dia in temp_semana:
    minimas.append(dia[0])
    maximas.append(dia[1])
#calcula el promedio de las minimas y maximas
#la funcion sum() suma todos los elementos de una lista
#la funcion len() cuenta cuantos elementos hay en una lista
promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print(f"El promedio de las temperaturas minimas es: {promedio_min:2f}°C")
print(f"El promedio de las temperaturas maximas es: {promedio_max:2f}°C")
#encontrar el dia con la mayor amplitud termica 
mayor_amplitud = 0
dia_mayor_amplitud = ""
#lista de nombres de los dias para mostrarlos en el resultado
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
#recorre la matriz nuevamente para calcular la amplitud de cada dia
for i in range(len(temp_semana)):
    #la amplitud termica es la diferencia entre la maxima y la minima
    amplitud_actual = temp_semana[i][1] - temp_semana[i][0]
    #se compara la amplitud actual con la mayor amplitud encontrada hasta ahora
    if amplitud_actual > mayor_amplitud:
        mayor_amplitud = amplitud_actual
        dia_mayor_amplitud = dias_semana[i]
print(f"El dia con mayor amplitud termica ({mayor_amplitud}°C) fue el {dia_mayor_amplitud}")
 
#Ejercicio 8
#matriz de notas: 5 estudiantes (filas) y 3 materias(columnas)
notas = [
    [6, 7, 9],
    [7, 10, 8],
    [7, 9, 6],
    [8, 10, 6],
    [8, 9, 7]
]
print("Promedio de cada estudiante:")
#recorre la matriz por filas(estudiantes)
for i in range(len(notas)):
    #calcula el promedio de la fila actual 
    promedio_est = sum(notas[i]) / len(notas[i])
    print(f"Estudiante {i+1}: {promedio_est:.2f}")
print("\nPromedio de cada materia:")
#recorre la matriz por columnas(materias)
#primero, recorre cada columna(materia)
for j in range(len(notas[0])):
    suma_mat = 0
    #recorre cada fila (estudiante) para sumar las notas de esa materia 
    for i in range(len(notas)):
        suma_mat += notas[i][j] 
    #calcula el promedio de la materia
    promedio_mat = suma_mat / len(notas)
    print (f"Materia {j+1}: {promedio_mat:.2f}")


#Ejercicio 9
#Inicializo con guiones para las casillas vacias
tablero = [
["-", "-", "-"],
["-", "-", "-"],
["-", "-", "-"]
]
#definimos una funcion para mostrar el tablero de forma ordenada
def mostrar_tablero(tab):
    for fila in tab:
        #usa join() para unir los elementos de cada fila con espacios
        print(" ".join(fila))
#bucle para dos jugadas (1 para X y 1 para 0)
for turno in range(2):
    #Determina de quien es el turno
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"
    print(f"\nTurno de {jugador}")
    #pedimos la fila y columna al usuario    
    fila = int(input("Ingresa el numero de fila (0, 1, 2): "))
    columna = int(input("Ingresa el numero de columnas (0, 1, 2): "))
    #se verifica si la posicion es valida y esta vacia 
    if 0 <= fila <= 2 and 0 <= columna <= 2 and tablero[fila][columna] == "-":
        #si es valida, coloca la ficha del jugador 
        tablero[fila][columna] = jugador
    else:
        print("Movimiento invalido. Intentalo de nuevo")
        #resta 1 al turno para que el mismo jugador tenga otro oportunidad 
        turno -= 1
        continue
    #Muestra el tablero despues de cada jugada
    print("\nEstado actual del tablero:")
    mostrar_tablero(tablero)



#Ejercicio 10

#Matriz de ventas: 4 productos(filas) y 7 dias(columnas)
ventas = [
    [10, 12, 18, 15, 20, 25, 8],
    [6, 11, 7, 12, 10, 8, 5],
    [18, 22, 28, 15, 33, 9, 20],
    [9, 11, 12, 17, 21, 14, 24]
]
#Lista con nombres de los productos y dias para que el resultado sea mas claro
nombre_prod = ["producto 1", "producto 2", "producto 3", "producto 4"]
dias_semana = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"]

#Mostrar el total vendido por cada producto
print ("total de ventas por cada producto:")
#recorre la matriz por filas (cada producto)
for i in range(len(ventas)):
    #usa num() para sumar todas las ventas de la fila del producto actual
    total_prod = sum(ventas[i])
    print(f"{nombre_prod[i]}: {total_prod} unidades vendidas")

#Mostrar el dia con mayores ventas totales
print("\n---")
print("Analisis de ventas por dia:")
#crea una lista para guardar el total de ventas de cada dia
ventas_por_dia = []
#Recorre la matriz por columnas (cada dia)
for j in range(len(ventas[0])):# len(ventas[0]) da el numero de dias (columnas)
    suma_dia = 0
    #suma las ventas de cada producto en ese dia
    for i in range(len(ventas)):
        suma_dia += ventas [i][j]
    ventas_por_dia.append(suma_dia)
#Encuentra el dia con mayores ventas usando la funcion (max)
max_ventas_dia = max(ventas_por_dia)
#obtiene el indice de ese valor maximo
indice_dia_mas_vendido = ventas_por_dia.index(max_ventas_dia)
#usa el indice para encontrar el nombre del dia
dia_mas_vendido = dias_semana[indice_dia_mas_vendido]

print(f"ventas totales por dia: {ventas_por_dia}")
print(f"El dia con mayores ventas totales fue el {dia_mas_vendido} con {max_ventas_dia} unidades vendidas")

#indica cual fue el producto mas vendido de la semana
print("n\----")
print("Analisis de ventas totales:")
#para encontrar el producto mas vendido, necesita los totales por producto
total_prod = []
for fila in ventas:
    total_prod.append(sum(fila))

#encuentra la mayor cantidad de ventas entre los productos 
max_ventas_prod = max(total_prod)
#obtiene el indice del producto con mas ventas
indice_dia_mas_vendido = total_prod.index(max_ventas_prod)
#usa el indice para encontrar el nombre del producto 
producto_mas_vendido = nombre_prod[indice_dia_mas_vendido]

print(f"ventas totales por producto: {total_prod}")
print(f"el producto mas vendido en la semana fue el {producto_mas_vendido}")