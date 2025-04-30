#Determinar signo y paridad

signo_numero = int(input("Ingresa el numero =>"))

    
if signo_numero > 0:
    print("Tu numero es positivo.")
elif signo_numero < 0:
    print("Tu numero es negativo.")
else:
    print("Tu numero es cero")
    
if signo_numero != 0:   
    if signo_numero %2 ==0:
        print("tu numero es par")
    else:  
        print("Tu numero es impar")
        
