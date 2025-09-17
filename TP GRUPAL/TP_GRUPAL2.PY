#LISTAS UNIDIDEMSIONALES:

#1)-
numeros = input("Ingrese números separados por espacio: ")

lista = [int(x) for x in numeros.split()]

suma = sum(lista)
print("La suma de los elementos es:", suma)


#2)-

entrada = input("Ingrese números separados por espacio: ")

lista = [int(x) for x in entrada.split()]

mayor = max(lista)
menor = min(lista)

print("El número mayor es:", mayor)
print("El número menor es:", menor)

#3)-

num_ = input("Ingrese elementos separados por espacio: ")

lista = num_.split()

lista.reverse()

print("Lista invertida:", lista)


#4)-

num = input("Ingrese números separados por espacio: ")

lista = [int(x) for x in num.split()]

pares = 0
impares = 0

for numero in lista:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)



#LISTAS BIDIMENSIONALES

#1)-

def generar_matriz(filas, columnas):
    matriz = []      
    valor = 1        
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(valor)
            valor += 1
        matriz.append(fila)
    
    return matriz

f = int(input("Ingrese número de filas: "))
c = int(input("Ingrese número de columnas: "))

matriz = generar_matriz(f, c)

for fila in matriz:
    print(fila)


#2)-

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma_total = sum(sum(fila) for fila in matriz)
print("La suma de todos los elementos es:", suma_total)


#3)-

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, fila in enumerate(matriz):
    suma_fila = sum(fila)
    print(f"La suma de la fila {i+1} es: {suma_fila}")





