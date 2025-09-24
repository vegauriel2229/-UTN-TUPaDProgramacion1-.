#1)-

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#2)-

cosas = ["pizza", "helado", "boxeo", "juegos", "series"]
print("Penúltimo elemento:", cosas[-2])

#3)-

lista_vacia = []
lista_vacia.append("uri")
lista_vacia.append("profeMagni")
lista_vacia.append("minecraft")

print(lista_vacia)

#4)- 

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"     # reemplaza el segundo
animales[-1] = "oso"     # reemplaza el último 

print(animales)

#5)- busca el numero mas grande de la lista o de mayor valor y la remueve
#quedaria = numeros[8,15,3,7]


#6)-

numeros = list(range(10, 31, 5))  
print(numeros[:2])  

#7)-

autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["autorojo", "corolla"]  #
print(autos)  


#8)-

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)  # [10, 20, 30]

#9)-

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

#b) Reemplazar "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"

# ) Eliminar "pan" del primer cliente
compras[0].remove("pan")

print(compras)

#10)-

lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(lista_anidada)







