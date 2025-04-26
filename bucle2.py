'''
# ejemplo de uso de ciclos for con una lista

frutas = ["manzana","pera","mango"]


for fruta in   frutas:
    print(frutas)
    

 
# Ejemplo de ciclos for con ina tupla

cuidades = ["madrid","barcelona","valencia"]

for cuidad in  cuidades:
    print(cuidad)
    


# Ejemplo de ciclo for con Str

mensaje = "Hola mundo"

for caracter in mensaje:
    print(caracter)
    


# Ejemplo de ciclo for cadena de caracteres

Numeros = [2,8,25,41,3,7,14]
Umbral = 20

for Numero in Numeros:
    if Numero>Umbral:
        print(f"El primer numero mayor que {Umbral} es {Numero}")
        break
else:
     print(f"Ningun numero en la lista es mayor que {Umbral}.")
     
'''

# ejemplo 2

while True:
    texto = input("Escribe algo(o'salir'para terminar):")
    