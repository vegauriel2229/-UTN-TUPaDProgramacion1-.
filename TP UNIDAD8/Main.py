
productos = []

# --- 1. Leer archivo y cargar productos en una lista de diccionarios ---
try:
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        print("\n *LISTA DE PRODUCTOS* ")
        print("-" * 60)

        for linea in archivo:
            partes = linea.strip().split(";")

            if len(partes) == 3:
                nombre = partes[0].capitalize()
                precio = float(partes[1])
                cantidad = int(partes[2])

                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto)
                print(f"Producto: {nombre:12} | Precio: ${precio:,.2f} | Cantidad: {cantidad}")
            else:
                print(" Línea con formato incorrecto:", linea)

        print("-" * 60)
except FileNotFoundError:
    print(" No se encontró el archivo 'productos.txt'. Se creará automáticamente al guardar nuevos productos.")

# --- 2. Agregar un nuevo producto ---
def agregar_producto():
    print("\n Agregar un nuevo producto")
    nombre = input("Ingrese el nombre del producto: ").strip().lower()
    precio = input("Ingrese el precio del producto: ").strip()
    cantidad = input("Ingrese la cantidad del producto: ").strip()

    try:
        precio = float(precio)
        cantidad = int(cantidad)
    except ValueError:
        print("Error: el precio debe ser numérico y la cantidad un número entero.")
        return

    nuevo_producto = {"nombre": nombre.capitalize(), "precio": precio, "cantidad": cantidad}
    productos.append(nuevo_producto)
    print(f"Producto '{nombre.capitalize()}' agregado correctamente.")

# --- 3. Buscar producto por nombre ---
def buscar_producto():
    nombre_buscar = input("\n Ingrese el nombre del producto que desea buscar: ").strip().capitalize()
    encontrado = False

    for producto in productos:
        if producto["nombre"] == nombre_buscar:
            print(f"\n Producto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print(f" El producto '{nombre_buscar}' no se encuentra en la lista.")

# --- 4. Guardar productos actualizados ---
def guardar_productos():
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']};{producto['precio']};{producto['cantidad']}\n")
    print(" Archivo 'productos.txt' actualizado correctamente.")

# --- 5. Mostrar todos los productos ---
def mostrar_todos():
    print("\nProductos en el sistema:")
    print("-" * 60)
    for p in productos:
        print(f"Producto: {p['nombre']:12} | Precio: ${p['precio']:,.2f} | Cantidad: {p['cantidad']}")
    print("-" * 60)

# --- Menú principal ---
while True:
    print("""
==============================
       MENÚ PRINCIPAL
==============================
1. Ver todos los productos
2. Buscar producto
3. Agregar producto
4. Guardar productos
0. Salir
==============================
""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_todos()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        guardar_productos()
    elif opcion == "0":
        print("Saliendo del programa... ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")




