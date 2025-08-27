#TP 1 ESTRUCTURAS SECUENCIALES

#1)-
print ("Hola mundo")

#2)-

nombre=input("INGRESA TU NOMBRE ")

print(f"HOLA {nombre}!!!")
 
#3)-

nombre=input("INGRESA TU NOMBRE ")
apellido=input("INGRESA TU APELLIDO ")
edad=input("INGRESA TU EDAD ")
residencia=input("INGRESA TU RESIDENCIA")

print(f"hola me llamo {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#4)-

import math

radiocirculo= float(input("ingresa el radio del circulo: "))

areacirculo= math.pi * (radiocirculo)**2
perimetrocirculo= 2 * math.pi * radiocirculo

print(f"el area es de {areacirculo} y el perimetro es de {perimetrocirculo}.")


#5)-

segundos= float(input("ingresa la cantidad de segundos que deseas convertir "))

horas = round(segundos / 3600)

print(f"{segundos} equivale a {horas}!!")

#6)-

numeromultipicar= int(input("ingresa el numero que deseas multiplicar"))


print(f"""
  {numeromultipicar} x 1 = {numeromultipicar * 1}
  {numeromultipicar} x 2 = {numeromultipicar * 2}
  {numeromultipicar} x 3 = {numeromultipicar * 3}
  {numeromultipicar} x 4 = {numeromultipicar * 4}
  {numeromultipicar} x 5 = {numeromultipicar * 5}
  {numeromultipicar} x 6 = {numeromultipicar * 6}
  {numeromultipicar} x 7 = {numeromultipicar * 7}
  {numeromultipicar} x 8 = {numeromultipicar * 8}
  {numeromultipicar} x 9 = {numeromultipicar * 9}
  {numeromultipicar} x 10 = {numeromultipicar * 10} 
""")


#7)-

num1=float(input("ingresa el primer numero:"))      
num2=float(input("ingresa el segundo numero:"))

suma= num1+num2
resta= num1-num2
multiplicar= num1*num2
dividir= round(num1 / num2,2)

print(f"""
SUMA: {num1}+{num2}= {suma}
RESTA: {num1}-{num2}= {resta}
MULTIPLICACION: {num1}*{num2}= {multiplicar}
DIVISION: {num1}/{num2}= {dividir}
""")



#8)-

peso=float(input("INGRESA TU PESO(KG):"))
altura=float(input("INGRESA TU ALTURA(METROS):"))
             
IMC= round(peso / altura**2,2)

print(f"TU INDICE DE MASA CORPORAL ES: {IMC}")


#9)-

gradoscelcius= float(input("ingresa grados celcius: "))

gradosFahrenheit= round(9/5 * gradoscelcius + 32,2)

print(f"{gradoscelcius} celcius equivalen a {gradosFahrenheit} Fahrenheit")


#10)-

numero1=float(input("ingresa el primer numero: "))
numero2=float(input("ingresa el segundo numero: "))
numero3=float(input("ingresa el tercer numero: "))


promedio=round(numero1 + numero2 + numero3 /3, 2)

print(f"EL PROMEDIO ENTRE {numero1}, {numero2} Y {numero3} ES= {promedio}")


#URIEL VEGA