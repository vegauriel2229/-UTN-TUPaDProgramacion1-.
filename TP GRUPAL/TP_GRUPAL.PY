
#8)-

texto = input("Ingrese una palabra: ")

resultado = texto.replace("a", "e").replace("A", "E")

print("palabra modificada:", resultado)


#9)-

frase= "La lluvia en Mendoza es escasa"

for caracter in frase:

    print(ord(caracter), end=" ")


#10)-

texto_ =input("Ingrese una cadena: ")

print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")

opcion =input("Elija una opción (1 o 2): ")

if opcion == "1":
    print("Resultado:", texto_.upper())
elif opcion == "2":
    print("Resultado:", texto_.lower())


#11)-

palabra1= input("Ingrese la primera palabra: ")
palabra2= input("Ingrese la segunda palabra: ")

if palabra1 == palabra2:
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")


#12)- 

cadena= "hipopotamo"

letras= cadena[3:5]   
print("Cuarta y quinta letra:", letras)

#13)-

cadena1= input("Ingrese la primera cadena: ")
cadena2= input("Ingrese la segunda cadena: ")

if cadena2 in cadena1:
    print("La segunda cadena SÍ se encuentra dentro de la primera")
else:
    print("La segunda cadena NO se encuentra dentro de la primera")


#14)-

#En Python no existe una distinción formal entre variables de tipo valor 
# y tipo referencia como en lenguajes como Java o C#.
#Sin embargo, el comportamiento es parecido:

#Tipos inmutables (enteros, flotantes, cadenas, tuplas, booleanos) 
#  se comportan como tipo valor, ya que cada vez que se modifican, 
# en realidad se crea un nuevo objeto en memoria.

#Tipos mutables (listas, diccionarios, conjuntos)
#se comportan como tipo referencia, porque varias variables pueden apuntar al mismo objeto,
#y un cambio en una de ellas se refleja en las demás.

