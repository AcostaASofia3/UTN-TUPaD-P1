#Ejercicio 1  
with open("productos.txt", "w", encoding="utf-8") as archivo: 
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,350.0,15\n")
        archivo.write("Goma,80.0,40\n")

    #Mostramos un mensaje para avisar que el archivo se creo correctamente    
print("El archivo 'productos.txt' fue creado con 3 productos de ejemplos.")

#Ejercicio 2
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:   
        linea = linea.strip()#para sacar el salto de linea
        nombre, precio, cantidad = linea.split(",")# para dividir en partes
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Ejercicio 3
#Mostar los productos actuales
with open("productos.txt", "r", encoding="utf-8") as archivo:
        print("Productos actuales:\n")
        for linea in archivo:
              linea = linea.strip()
              nombre, precio, cantidad = linea.split(",")
              print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
#pedir nuevo producto al usuario
print("\nIngrese un nuevo producto para agregar al archivo:")
nuevo_nombre = input("Nombre: ")
nuevo_precio = input("Precio: ")
nueva_cantidad = input("Cantidad: ")
#agregar al archivo sin borrar lo anterior
with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}")
print("\nProducto agregado correctamente.")      
       
#Ejercicio 4
productos = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        dic = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(dic)
#Mostramos la lista completa de diccionarios
print("Lista de productos(estrucuta interna):")
for p in productos:
    print(p)        

#Ejercicio 5 
buscar = input("\nIngrese el nombre del producto a buscar: ").strip().capitalize()
encontrado = False
for p in productos:
     if p["nombre"].lower() == buscar.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado en la lista.")


#Ejercicio 6
for p in productos:
    p["precio"] = p["precio"] * 1.10
#se guarda todo en el archivo, reemplazando el contenido anterior
with open ("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        linea = f"{p['nombre']}, {p['precio']}, {p['cantidad']}\n"
        archivo.write(linea)
print("\nArchivo actualizado correctamente con los nuevos precios")