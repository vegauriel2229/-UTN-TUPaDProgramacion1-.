#1)-

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2)-

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Programa principal
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

#3)-

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


#4)-

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingrese el radio del círculo: "))
print("Área:", round(calcular_area_circulo(radio), 2))
print("Perímetro:", round(calcular_perimetro_circulo(radio), 2))

#5)-

def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
print("Equivalente en horas:", round(segundos_a_horas(segundos), 2))


#6)-

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)


#7)-

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Error: división por cero")

# Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")


#8)-

def calcular_imc(peso, altura):
    return peso / (altura**2)

# Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print("Su IMC es:", round(calcular_imc(peso, altura), 2))


#9)-

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingrese la temperatura en Celsius: "))
print("Equivalente en Fahrenheit:", round(celsius_a_fahrenheit(celsius), 2))


#10)-

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print("El promedio es:", round(calcular_promedio(a, b, c), 2))


    