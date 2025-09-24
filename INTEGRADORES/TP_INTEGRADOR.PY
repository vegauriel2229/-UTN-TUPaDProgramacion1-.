#TP INTEGRADOR 1

# -------------------- DATOS INICIALES --------------------
Golosinas = [
    ["1","kitkat","20"],
    ["2","chicles","50"],
    ["3","caramelo_menta","50"],
    ["4","huevo_kinder","10"],
    ["5","cheetos","10"],
    ["6","twixs","10"],
    ["7","MYM`S","10"],
    ["8","papas_lays","2"],
    ["9","Milkybar","10"],
    ["10","Alfajor_Tofi","15"],
    ["11","Lata_Coca","12"],
    ["12","Chitos","10"]
]

empleados = {
    "1100":"José Alonso",
    "1200":"Federico Pacheco",
    "1300":"Nelson Pereira",
    "1400":"Osvaldo Tejada",
    "1500":"Gastón Garcia"
}

claves_tecnico = ("admin","CCCDDD","2020")

golosinasPedidas = []


# -------------------- FUNCIONES --------------------
def mostrargolosinas(Golosinas):
    print("\nN°   | Producto         | Stock")
    print("--------------------------------")
    for golosina in Golosinas:
        print(f"{golosina[0]:<4} | {golosina[1]:<15} | {golosina[2]}")


def mostrar_golosinas_pedidas():
    print("\n=== HISTORIAL DE GOLOSINAS PEDIDAS ===")
    if not golosinasPedidas:
        print("Aún no se pidieron golosinas.")
    else:
        for fila in golosinasPedidas:
            print(f"Código: {fila[0]}, Nombre: {fila[1]}, Cantidad pedida: {fila[2]}")


def pedir_golosina():
    legajo = input("Ingrese su legajo: ")
    if legajo not in empleados:
        print("Usted no es un empleado de la empresa ")
        return
    
    print(f"Bienvenido {empleados[legajo]} ")
    
    while True:
        mostrargolosinas(Golosinas)
        codigo = input("Ingrese el código de la golosina (o 'salir' para volver al menú): ").lower()
        
        if codigo == "salir":
            break
        
        encontrada = False
        for gol in Golosinas:
            if gol[0] == codigo:
                encontrada = True
                if int(gol[2]) > 0:
                    gol[2] = str(int(gol[2]) - 1)  
                    print(f"Disfrute su {gol[1]} ")

                    
                    registro = None
                    for fila in golosinasPedidas:
                        if fila[0] == gol[0]:
                            registro = fila
                            break
                    if registro:
                        registro[2] += 1
                    else:
                        golosinasPedidas.append([gol[0], gol[1], 1])
                else:
                    print(f"Lo sentimos, {gol[1]} no se encuentra disponible ")
                break
        if not encontrada:
            print("Código de golosina incorrecto ")


def rellenar_golosinas():
    print("\n=== FUNCIÓN DE TÉCNICO: RELLENAR GOLOSINAS ===")

    clave1 = input("Ingrese la primera clave: ")
    clave2 = input("Ingrese la segunda clave: ")
    clave3 = input("Ingrese la tercera clave: ")

    if (clave1, clave2, clave3) == claves_tecnico:
        print("Acceso autorizado ")
        
        while True:
            mostrargolosinas(Golosinas)
            codigo = input("Ingrese el código de la golosina a recargar (o 'salir' para volver): ").lower()

            if codigo == "salir":
                break

            encontrada = False
            for gol in Golosinas:
                if gol[0] == codigo:
                    encontrada = True
                    try:
                        cantidad = int(input("Ingrese la cantidad a recargar (>0): "))
                        if cantidad > 0:
                            gol[2] = str(int(gol[2]) + cantidad)
                            print(f"Se recargaron {cantidad} unidades de {gol[1]}. Nuevo stock: {gol[2]}")
                        else:
                            print("La cantidad debe ser mayor a 0 ")
                    except ValueError:
                        print("Debe ingresar un número válido ")
                    break
            
            if not encontrada:
                print("Código de golosina incorrecto ")
    else:
        print("No tiene permiso para ejecutar la función de recarga ")


# -------------------- MENÚ PRINCIPAL --------------------
while True:
    print("\nBIENVENIDO!!!")
    print("A: PEDIR GOLOSINA")
    print("B: MOSTRAR GOLOSINAS")
    print("C: RELLENAR GOLOSINAS")
    print("D: APAGAR MAQUINA")

    opcion = input("Ingrese opción: ").lower()

    if opcion == "a":
        pedir_golosina()
    elif opcion == "b":
        mostrargolosinas(Golosinas)
        mostrar_golosinas_pedidas()
    elif opcion == "c":
        rellenar_golosinas()
    elif opcion == "d":
        print("Apagando máquina")
        break
    else:
        print("Opción inválida, intente nuevamente ")
#----------------------------------------------------------