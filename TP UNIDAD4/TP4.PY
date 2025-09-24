
#1)-

i = 0
while i <= 100:
    print(i)
    i += 1


#2)-

numero = int(input("Ingrese un número entero: "))

contador = 0
num = abs(numero)  
if num == 0:
    contador = 1
else:
    while num > 0:
        num //= 10 
        contador += 1

print("El número tiene", contador, "dígitos")


#3)-

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))


if a > b:
    a, b = b, a

suma = 0
for i in range(a + 1, b):  
    suma += i

print("La suma de los números entre", a, "y", b, "es:", suma)


#4)-

suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número (0 para terminar): "))

print("La suma total es:", suma)

#5)-

import random

numero_secreto = random.randint(0, 9)  
intentos = 0
adivinanza = -1

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

print("¡Correcto! El número era", numero_secreto)
print("Lo lograste en", intentos, "intentos")

#6)-

for i in range(100, -1, -2):  
    print(i)

#7)-

n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(n + 1):  # de 0 hasta n inclusive
    suma += i

print("La suma de los números de 0 a", n, "es:", suma)

#8)-


cantidad = 100   # podés cambiar para probar 
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    
    # Par o impar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Positivo o negativo
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)



#9)-

cantidad = 100   # podés cambiarlo para probar
suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / cantidad
print("La media de los", cantidad, "números es:", media)



#10)-

num = input("Ingrese un número: ")
invertido = ""

for i in range(len(num)-1, -1, -1):
    invertido += num[i]

print("Número invertido:", invertido)





