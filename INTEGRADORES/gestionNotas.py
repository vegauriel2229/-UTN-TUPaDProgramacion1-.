
#------------DATOS INICIALES-------------

Alumnos = {
"60902" : "Rodolfo Fernandez" ,
"61654" : "Luis Gomez" ,
"61852" : "Andrea Pereira" ,
"61754" : "Juan Cruz Gonzales" ,
}

Materias = [
    ["Ciencias", None, None, None ],
    ["Historia", None, None, None],
    ["Geografia", None, None, None],
    ["Matematicas", None, None, None],
    ["Fisica",None, None, None]     
 ]

notasFinales = [
    ["Rodolfo Fernandez", None],
    ["Luis Gomez", None ],
    ["Andrea Pereira", None],
    ["Juan Cruz Gonzales", None ]
] 

mejorAlumno= None
mejorPromedio= 0

# -------------------------------------------


for alumno_id, alumno_nombre in Alumnos.items():
    print(f"Alumno: {alumno_nombre}")
    
    
    materias = [fila[:] for fila in Materias]

    
    for fila in materias:
        print(f"\nIngrese las notas para la materia {fila[0]}:")

        # Validación de Nota 1
        while True:
            try:
                nota1 = float(input("  Nota 1: "))
                if 0 <= nota1 <= 10:
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Ingrese un número válido.")

        # Validación de Nota 2
        while True:
            try:
                nota2 = float(input("  Nota 2: "))
                if 0 <= nota2 <= 10:
                    break
                else:
                    print(" La nota debe estar entre 0 y 10.")
            except ValueError:
                print(" Ingrese un número válido.")

        
        fila[1] = nota1
        fila[2] = nota2
        fila[3] = (nota1 + nota2) / 2
        print(f"  Nota Final: {fila[3]:.2f}")

   
    print("\n Materias y notas finales:")
    print("Materia       | Nota1 | Nota2 | Promedio")
    print("-----------------------------------------")
    for f in materias:
        print(f"{f[0]:12} | {f[1]:5} | {f[2]:5} | {f[3]:7.2f}")

    # Determinar la materia con la nota final más alta
    mejorMateria = max(materias, key=lambda x: x[3])
    print(f"\n La materia con mayor calificación es {mejorMateria[0]} con {mejorMateria[3]:.2f}")

    # Calcular promedio general del alumno
    promedioAlumno = sum(f[3] for f in materias) / len(materias)
    print(f"Promedio General de {alumno_nombre}: {promedioAlumno:.2f}")

    # Guardar en notasFinales
    for fila in notasFinales:
        if fila[0] == alumno_nombre:
            fila[1] = promedioAlumno

    # Verificar si este alumno es el mejor hasta ahora
    if promedioAlumno > mejorPromedio:
        mejorPromedio = promedioAlumno
        mejorAlumno = alumno_nombre

# Mostrar resumen final
print("\ Promedios finales de los alumnos:")
for fila in notasFinales:
    print(f"{fila[0]} → {fila[1]:.2f}")

print(f"\n El mejor promedio lo tiene {mejorAlumno} con {mejorPromedio:.2f}")






