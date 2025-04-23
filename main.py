# Primero para comenzar el codigo que todos conocemos "Hola mundo"

print("Hola mundo")

# Tipos de datos

Numero_enteros = int  #ejemplo => 20
Numero_flotantes = float #ejemplo => 20.5
Cadena_de_texto = str #ejemplo => "hola mundo"
Booleanos = bool #ejemplo => true y false

# ejemplos en ejecucion

#Numero enteros (int)
numeros_positivos = 10
numeros_negativos = -10
numero_neutro = 0

print(type(numeros_positivos).__name__)
print(type(numeros_negativos).__name__)
print(type(numero_neutro).__name__)

# Entradas de datos
primer_numero_ingresado = float(input("Ingrese el primer numero: "))
segundo_numero_ingresado = float(input("Ingrese el segudno numero: "))

operacion = input("Escribir el tipo de operacion: ")


# Procesamiento

if operacion == "suma": 
   resultado = primer_numero_ingresado + segundo_numero_ingresado

if operacion == "recta": 
   resultado = primer_numero_ingresado - segundo_numero_ingresado

if operacion == "multiplicacion":
   resultado = primer_numero_ingresado * segundo_numero_ingresado
   
if operacion == "division":
   resultado = primer_numero_ingresado / segundo_numero_ingresado

print("El resuldo es", resultado)

# para corregir el valor sea int y no float
print(f"El resultado es {resultado:.0f}")


# Ingreso de datos por consola

nombre=input("ingresar tu nombre=>")
apellido=input("ingresar tu apellido=>")
edad=input("ingresa tu edad=>")

print(f"hola soy{nombre} {apellido} y tengo {edad} años")



