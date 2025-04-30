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
        





#Calificacion de edad

edadCalificacion = int(input("Ingresa tu edad=>"))

if edadCalificacion >0 and edadCalificacion <18:
    print("Eres menor de edad.")

elif edadCalificacion >=18 and edadCalificacion <=30:
    print("Eres adulto joven.")
    
elif edadCalificacion >=31 and edadCalificacion <=65:
    print("Eres adulto maduro.")
    
elif edadCalificacion >=65 and edadCalificacion <=100:
    print("Eres un adulto mayor")
    
else:
    print("Ya eres un inmortal!.")
    
    
    
## Tarifa de transporte según día y hora

dia_laborable = (input("Ingresa si el dia es laborable? (S/N): ")).upper()

if dia_laborable == "N":
    print("Fin de semana!.")
    
elif dia_laborable == "S":
    hora = int(input("Ingresa la hora (0-23): "))
    if (7 <= hora <= 9) or (17 <= hora <= 19):
        tarifa = "Hora pico"
    else:
        tarifa = "Hora normal"
    print(f"La tarifa aplicada es: {tarifa}")
        
else:
    tarifa = "Entrada invalida"
    

#Descuento en tienda VIP

codigoCorrecto = "Noah26"
codigoVIP = ""
Valor_compra = int(input("Ingresa el valor de la compra=>"))
Cliente_VIP = input("Ingresa si eres cliente? (S/N): ").upper()
 
if Cliente_VIP == "N":
    if Valor_compra>=500:
                descuento = 0.05
                print("No eres VIP, tienes descuento de 10%")
    else:
                print("No eres VIP, no tienes descuento!")
                
elif Cliente_VIP == "S":
    while codigoVIP != codigoCorrecto:
        codigoVIP = str(input("Introducir codigo VIP!=>"))
    else:
        print("Codigo correcto VIP!")
    if Valor_compra>=500:
                descuento = 0.20
                print("Eres VPI, tienes un descuento de 20%")
    else:
                descuento = 0.10
                print("Eres VIP, tienes descuento de 10%")
                
Valor_final = Valor_compra * (1 - descuento)
print(f"Tu Valor a pagar es: {Valor_final:.2f}")