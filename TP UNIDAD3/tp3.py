#1)-

edad=int(input("INGRESA TU EDAD: "))

if edad < 18:

   print("NO ES MAYOR DE EDAD")

elif edad >= 18:
   print("ES MAYOR DE EDAD")


#2)-

nota=int(input("INGRESA LA NOTA: "))

if nota >= 6:
   
   print("APROVADO")
else:
   print("DESAPROBADO") 


#3)- 

num= int(input("INGRESA UN NUMERO PAR: "))

if num %2 == 0:
   print(f"{num} ES UN NUMERO PAR")

else:
   print(f"{num} NO ES UN NUMERO PAR")


#4)-

ed_ad= int(input("INGRESA TU EDAD:"))

if ed_ad < 12:
   print("NIÑO/A")

elif ed_ad >= 12:
   print("ADOLESENTE")

elif ed_ad >= 18 and ed_ad < 30:
   print("ADULTO JOVEN")

elif ed_ad >= 30:
   print("ADULTO")



#5)-

cont_raseña= input("INGRESA TU NUEVA CONTRASEÑA (entre 8 y 14 carateres): ")

long_contraseña= len(cont_raseña)

if 8 <= long_contraseña <= 14:
   print("PORFAVOR INGRESA UNA CONTRASEÑA DE ENTRE 8 Y 14 CARACTERES")
   
else:
   print("CONTRASEÑA CORRECTA")



#6)-

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
                         

print("mode:",mode(numeros_aleatorios))
print("median:",median(numeros_aleatorios))
print("mean:",mean(numeros_aleatorios))

moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)

if media > mediana and mediana > moda:
 print("Es Sesgo positivo")   

elif media < mediana and mediana <= moda:
   print("Es Sesgo negativo ")

elif media == mediana and mediana == moda:
   print("Sin sesgo")



#7)-

frase= input("Ingresá una palabra o frase: ")

frase= frase.strip()

if frase[-1].lower() in "aeiou":
    frase += "!"
print("Resultado:", frase)


#8)-

nombre= input("INGRESA TU NOMBRE:")

print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.") 
print("3. Si quiere su nombre con la primera letra mayúscula.")

numero123= int(input("INGRESA UN NUMERO SEGUN LO QUE QUIERAS "))

if numero123 == 1:
   print(nombre.upper())
elif numero123 == 2:
   print(nombre.lower())
elif numero123 == 3:
   print(nombre.title())


#9)-

terremoto= int(input("INGRESA LA MAGNITUD DEL TEMBLOR/TERREMOTO:"))

if terremoto < 3:
   print("Muy leve (imperceptible)")

elif terremoto >= 3 and terremoto < 4:
   print("leve (ligeramente perceptible)")

elif terremoto >= 4 and terremoto < 5:
   print("Moderado (sentido por personas, pero generalmente no causa daños).")

elif terremoto >= 5 and terremoto < 6:
   print("Fuerte (puede causar daños en estructuras débiles).")

elif terremoto >= 6 and terremoto < 7:
   print("Muy Fuerte (puede causar daños significativos).")

elif terremoto >= 7:
   print("Extremo (puede causar graves daños a gran escala).")   


#10)-

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = input("¿Qué mes es?: ").lower()
dia = int(input("¿Qué día es?: "))

meses = {
    "enero": 1, "febrero": 2, "marzo": 3,
    "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9,
    "octubre": 10, "noviembre": 11, "diciembre": 12
}

if mes not in meses:
    print("Mes inválido.")
else:
    num_mes = meses[mes]

   
    if hemisferio == "N":
        if (num_mes == 12 and dia >= 21) or (1 <= num_mes <= 2) or (num_mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (num_mes == 3 and dia >= 21) or (4 <= num_mes <= 5) or (num_mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (num_mes == 6 and dia >= 21) or (7 <= num_mes <= 8) or (num_mes == 9 and dia <= 20):
            estacion = "Verano"
        else:
            estacion = "Otoño"

   
    elif hemisferio == "S":
        if (num_mes == 12 and dia >= 21) or (1 <= num_mes <= 2) or (num_mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (num_mes == 3 and dia >= 21) or (4 <= num_mes <= 5) or (num_mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (num_mes == 6 and dia >= 21) or (7 <= num_mes <= 8) or (num_mes == 9 and dia <= 20):
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    else:
        estacion = "Hemisferio inválido."

    print(f"En el hemisferio {hemisferio}, el {dia} de {mes.capitalize()} es {estacion}.")


