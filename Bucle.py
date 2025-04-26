# Bucle True

numero1 = 16
numero2 = 8

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
    
    
# Bucle false

numero3 = 8
numero4 = 4

if numero3 < numero4:
    print(f"{numero3} es menor que {numero4}")
    
    
# Ejemplo de la condicion if-else

tuEdad = 17
edadMinimaParaVotar = 18

if tuEdad>=edadMinimaParaVotar:
    print("Puedes votar")
    
else:
    print("No puedes votar")
    
    


# Ejemplo de la condicion if-elif-else

tuCalificacion = int(input("Ingresa tu calificacion por favor=>"))

if tuCalificacion == 0:
    print("Tu calificacion es 0, no tienes premios.")
    
elif tuCalificacion == 1:
    print("Tu calificacion es 1, ganas un premio de 100 puntos.")
    
elif tuCalificacion == 2:
    print("Tu calificacion es 2, ganas un premio de 200 puntos.")
    
elif tuCalificacion == 3:
    print("Tu calificacion es 3, ganas un premio de 300 puntos.")
    
elif tuCalificacion == 4:
    print("Tu calificacion es 4, ganas un premio de 400 puntos.")
    
elif tuCalificacion == 5:
    print("Tu calificacion es 5, tienes un premio de 500 puntos.")
    
else:
    print("Tu califiacion no esta en el rango valido (0-5).")
    
    


# Ejemplo de ciclos
# ciclos con for y sin for

#sin for

nombrecompleto = "Noah beleño"
print(nombrecompleto)
print(nombrecompleto)
print(nombrecompleto)
print(nombrecompleto)
print(nombrecompleto)



# con for

nombrecompleto = "Noah beleño"

for i in range(10):
    print(nombrecompleto)
    


# range(final):Genera numeros desde 0 hasta el final"

for i in range(5):
    print(i)
    


# range(inicio,final) genera numeros desde el inicio hasta el final

for i in range(2,6):
    print(i)

    

# range (inicio,final,salto) genera numeros desde inicio hasta el final, saltando

for i in range(5,40,5):
    print(i)
    


# Ejemplo de ciclos while

flag = "si"

while flag != "no":
    print("hola mundo")
    flag = input("Quieres imprimir el mensaje otra vez?=>")
    


# Ciclo while con iterador

iterador = 0

# while iterador "< 10 el ciclo termina un numero menor a 10 
while iterador < 10:
    print("El iterador es:", iterador)
    # saltos "depende la secuencias de saltos le des" puede ser (1,2,3,10,50..etc)
    iterador+=1
    


# Ciclos while con else

nombreCorrecto = "Noah"
nombreusuario = ""
contraseñaCorrecta = "Noah123"
contraseñaUsuario = ""

while nombreusuario != nombreCorrecto:
    nombreusuario = str(input("Introducir nombre de usuario=>"))
else:
    print("Nombre usuario correcto!")
    


while contraseñaUsuario != contraseñaCorrecta:
    contraseñaUsuario = str(input("Introducir contraseña=>"))
else:
    print("Contraseña correcta!")
print("Bienvenido a tu programa!")



