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
    print("Tienes 3 intentos para escribir los datos correcto!")
    contador = 1
    while contador <= 3:
        codigoVIP = input("Introducir codigo VIP=>")
        if codigoVIP == codigoCorrecto:
            print("Codigo correcto VIP!")
            contador = 4
        else:
            print("Codigo VIP incorrecto")
            if contador == 3:
                print("Comunicate con soporte, has fallado tus 3 intentos.")
                exit("")
            contador = contador +1
                
    if Valor_compra>=500:
                descuento = 0.20
                print("Eres VPI, tienes un descuento de 20%")
    else:
                descuento = 0.10
                print("Eres VIP, tienes descuento de 10%")
                
Valor_final = Valor_compra * (1 - descuento)
print(f"Tu Valor a pagar es: ${Valor_final:.2f}")
