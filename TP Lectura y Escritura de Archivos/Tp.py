import os

# -------------------------------
# FUNCIONES
# -------------------------------

def leer_alumnos(nombre_archivo):
    """Lee el archivo y devuelve un diccionario con los alumnos."""
    alumnos = {}
    try:
        # Si el archivo no existe, se crea vacío
        if not os.path.exists(nombre_archivo):
            open(nombre_archivo, "w", encoding="utf-8").close()
            print(f"Archivo '{nombre_archivo}' creado vacío.")
            return alumnos

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) != 4:
                    print(f"Línea inválida: {linea}")
                    continue
                nombre, apellido, legajo, nota = partes
                alumnos[legajo] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "nota": float(nota)
                }
        return alumnos
    except Exception as e:
        print("Error al leer el archivo:", e)
        return {}


def validar_existe_alumno(legajo, alumnos):
    """Devuelve True si el legajo ya existe."""
    return legajo in alumnos


def agregar_alumno(nombre_archivo, alumnos):
    """Pide datos, valida, y agrega un nuevo alumno."""
    try:
        # Validar nombre y apellido (solo letras)
        nombre = input("Ingrese nombre: ").strip()
        while not nombre.isalpha():
            nombre = input("Nombre inválido. Ingrese solo letras: ").strip()

        apellido = input("Ingrese apellido: ").strip()
        while not apellido.isalpha():
            apellido = input("Apellido inválido. Ingrese solo letras: ").strip()

        # Validar legajo (5 dígitos y que no exista)
        legajo = input("Ingrese legajo (5 dígitos): ").strip()
        while not (legajo.isdigit() and len(legajo) == 5):
            legajo = input("Legajo inválido. Ingrese 5 dígitos: ").strip()

        if validar_existe_alumno(legajo, alumnos):
            print(f" El legajo {legajo} ya existe en el archivo, no se permite su escritura.")
            return alumnos

        # Validar nota promedio
        while True:
            try:
                nota = float(input("Ingrese nota promedio (1 a 10): "))
                if 1 <= nota <= 10:
                    break
                else:
                    print("La nota debe estar entre 1 y 10.")
            except ValueError:
                print("Debe ingresar un número válido.")

        # Guardar en el archivo
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")

        # Actualizar el diccionario en memoria
        alumnos[legajo] = {
            "nombre": nombre,
            "apellido": apellido,
            "nota": nota
        }

        print(f" Alumno {nombre} {apellido} agregado correctamente.\n")
        return alumnos

    except Exception as e:
        print("Error al agregar alumno:", e)
        return alumnos


def guardar_aprobados(nombre_archivo, alumnos):
    """Genera un archivo aprobados.txt y lo muestra."""
    try:
        with open("aprobados.txt", "w", encoding="utf-8") as archivo:
            for legajo, datos in alumnos.items():
                if datos["nota"] >= 6:
                    linea = f"{datos['nombre']};{datos['apellido']};{legajo};{datos['nota']}\n"
                    archivo.write(linea)

        print("\nArchivo 'aprobados.txt' generado con éxito. Contenido:\n")
        with open("aprobados.txt", "r", encoding="utf-8") as archivo:
            print(archivo.read())

    except Exception as e:
        print("Error al guardar aprobados:", e)


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------
def main():
    ARCHIVO = "alumnos.txt"
    alumnos = leer_alumnos(ARCHIVO)

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar archivo de aprobados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if not alumnos:
                print("No hay alumnos cargados.")
            else:
                print("\nListado de alumnos:")
                for legajo, datos in alumnos.items():
                    print(f"{datos['nombre']} {datos['apellido']} (Legajo {legajo}) → Nota: {datos['nota']}")

        elif opcion == "2":
            alumnos = agregar_alumno(ARCHIVO, alumnos)

        elif opcion == "3":
            guardar_aprobados("aprobados.txt", alumnos)

        elif opcion == "4":
            print(" Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
