# Hola, Bienvenido a tu minisuper
# Espacio
print("'''''''''''''''''''''''''''''''''''''''''''")
print("''''''''''''''''Hola!!'''''''''''''''''''''")
print("'''''''''Bienvenido a tu Minisuper'''''''''")
print("'''''''''''''''''''''''''''''''''''''''''''")
print("'''''''''''''''''''''''''''''''''''''''''''")

# Datos de cliente
# Ingresar numero de cajero "tiene que ser 0 hasta 9999", sino no te dejara pasar
while True:
    try:
        Numero_de_cajero = int(input("Ingresa numero del cajero 🏧=>"))
        if Numero_de_cajero == "" or Numero_de_cajero <0 or Numero_de_cajero>9999:
            print("Numero de cajero incorrecto, Por favor confirmar numero del cajero!")
            continue
        break
    except ValueError:
        print("Error al ingresar datos!")   

print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print()        
# Datos de cliente
# Ingresar nombre de cliente
Nombre_del_cliente = str(input("Ingresa nombre de cliente 👤=> "))
# Codigo para que no imprima numeros como caracteres de texto
Nombre_del_cliente = "".join(char for char in Nombre_del_cliente if not char.isdigit())
#print(Nombre_del_cliente)
# Hola!, "nombre del cliente"
print("'''''''''''''''''''''''''''''''''''''''''''")
print("        Hola!", Nombre_del_cliente )
print("'''''''''''''''''''''''''''''''''''''''''''")
# Ingresar Numero de identidad
#Numero_de_documento = int(input("Ingresa numero de identidad=> "))

while True:
    try:
        Numero_de_documento = int(input("Ingresa numero de identidad 🪪=>"))
        if Numero_de_documento == "" or Numero_de_documento < 0 or Numero_de_documento >9999999999:
            print("Numero de identidad incorrecto, Por favor confirmar numero de identidad")
            continue
        break
    except ValueError:
        print("Error al ingresar datos!")

# Datos Guardados del cliente
print("''''''''''''''''''''''''''''''''''''''''''''")
print("              Datos del cliente                 ")
print("  Nombre de cliente      Numero de identidad")
print(f"    {Nombre_del_cliente}                  {Numero_de_documento}")
print("''''''''''''''''''''''''''''''''''''''''''''")


# Sistema de ingreso de productos,precios y cantidad

Nombre_del_producto = str(input("Ingrese el nombre del producto => "))

while True:
    try:
        Precio_unitario = float(input("Ingrese el precio unitario 💲=>"))
        if Precio_unitario < 0:
            print("El precio no debe ser negativo. Intenta de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada invalida. Por favor, Ingresa un numero valido para el precio.")
        
        
while True:
    try:
        Cantidad_de_productos = float(input("Ingrese la cantidad de productos📦=>"))
        if Cantidad_de_productos < 0:
            print("La cantidad no debe ser negativo. Intenta de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada invalida. Por favor, Ingresa un numero valido para la cantidad.")


        
# Valor de la compra
valor_de_la_compra = Precio_unitario * Cantidad_de_productos
print(f"Valor a pagar ${Precio_unitario * Cantidad_de_productos:.2f}")

# Formato de pedido
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("                        Formato de pedido                       ")
print("  Nombre Del Producto       Precio Unitario       Cantidad")
print(f"  {Nombre_del_producto}                   $ {Precio_unitario:.2f}                 {Cantidad_de_productos:.0f}")
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")


# Ingresa "si" tu producto tienes descuento, sino tiene di "no"
#print("Ingresa Si o 0,el producto tiene descuento")
print("Ingresa valor el descuento (0 si no hay descuento)")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''")

# Valor de descuento del producto
print(f"Ingresa el valor de descuento del {Nombre_del_producto}:")
while True:
    try:
        Valor_de_descuento_del_producto = float(input("Ingrese el valor de descuento=>"))
        if Valor_de_descuento_del_producto<0 or Valor_de_descuento_del_producto>100:
            print("El Valor no debe ser negativo,ni puede ser mayor a 100%. Intenta de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada invalida. Por favor, Ingresa un numero valido para el descuento.")
        
#Valor_de_descuento_del_producto = int(input(""))
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print()

# Valor total del producto con descuento
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")
Valor_total_del_producto_con_descuento = valor_de_la_compra * (1 -(Valor_de_descuento_del_producto / 100))
print(f"Valor con descuento a pagar del {Nombre_del_producto} es: ${valor_de_la_compra * (1 -(Valor_de_descuento_del_producto / 100)):.2f}")
print(f"Valor ahorrado ${valor_de_la_compra - Valor_total_del_producto_con_descuento:.2f}")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")

# Metodo de pago

print("""Que metodo de pago desea pagar:
1. Efectivo 💵
2. Transferencia 📱
3. Datafono 💳""")

# Selecion de metodo de pago
metodos=["nada","efectivo", "transferencia", "datafono"]
while True:
    try:
        Metodo_de_pago = int(input("Ingrese el metodo de pago=>"))
        if Metodo_de_pago > 3 or Metodo_de_pago < 1:
            print()
        break
    except ValueError:
        print("Entrada invalida. Por favor, Ingresa bien el metodo de pago.")


match Metodo_de_pago:
    case 1 :
        print("Efectivo 💵")
        while True:
            try:
                Valor_en_efectivo = float(input("Ingrese el valor en efectivo=>"))
                while Valor_en_efectivo < 0 :
                    print("Dinero insuficiente. nececitas mas dinero!")
                    Valor_en_efectivo = float(input("Ingresa el valor en efectivo=>."))
                    

                break
            except ValueError:
                print("Entrada invalida. Por favor, Ingresa un numero valido para el valor.")
                
        # Valor pagado y valor devuelto
        print(f"Valor pagado en efectivo ${Valor_en_efectivo:.2f}")
        print(f"Valor devuelto ${Valor_en_efectivo - Valor_total_del_producto_con_descuento:.2f}")
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

    
    case 2 :
        print("Transferencia 📱")
        while True:
            try:
                Valor_de_transferencia = float(input("Ingrese el valor de tranferencia=>"))
                while Valor_de_transferencia !=Valor_total_del_producto_con_descuento:
                    print("Error de pago!. Monto insufuciente!")
                    Valor_de_transferencia = float(input("Ingrese el valor de tranferencia=>"))
                    
                break
            except ValueError:
                print("Ingresar el valor correcto de la comprar.")
        print(f"Valor pagado en transferencia ${Valor_de_transferencia:.2f}")
        print(f"Valor devuelto ${Valor_de_transferencia - Valor_total_del_producto_con_descuento:.2f}")
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        
        
    case 3 :
        print("Datafono 💳")
        while True:
            try:
                Valor_pagado_datafono = float(input("Ingrese el valor de pago=>"))
                while Valor_pagado_datafono !=Valor_total_del_producto_con_descuento:
                    print("Tarjeta rechazada!. Saldo insuficiente!")
                    Valor_pagado_datafono = float(input("Ingresa el valor de la compra=>"))
                    
                break
            except ValueError:
                print("Ingresa nuevamente tu pago")
        print(f"Valor pagado por datafono ${Valor_pagado_datafono}")

#Metodo_de_pago = str(input("Ingresa el metodo de pago=>"))
#Metodo_de_pago = "".join(char for char in Metodo_de_pago if not char.isdigit())
#print(Metodo_de_pago)

# Ingresa el valor en efectivo
#Valor_en_efectivo = float(input("Ingresa el valor en efectivo $"))



# Factura de compra
print("'''''''''''''''''''''''''''''''''''''''''''''''''''")
print("            Factura de compra                  ")
print(f"Nombre del cliente        {Nombre_del_cliente}")
print(f"Numero de identidad       {Numero_de_documento}")
print(f"Valor del producto       ${Precio_unitario:.2f}")
print(f"Cantidad de producto      {Cantidad_de_productos:.0f}")
print(f"Valor por los productos  ${valor_de_la_compra:.2f}")
print(f"valor de descuento        {Valor_de_descuento_del_producto:.0f}%")
print(f"Valor con descuento a pagar   ${Valor_total_del_producto_con_descuento:.2f}")
print(f"Valor ahorrado            ${valor_de_la_compra - Valor_total_del_producto_con_descuento:.2f}")
print(f"Metodo de pago            {metodos[Metodo_de_pago]}")
if Metodo_de_pago == 1:
    print(f"Valor pagado en efectivo, {Valor_en_efectivo:.2f}")
    print(f"Valor devuelto           ${Valor_en_efectivo - Valor_total_del_producto_con_descuento:.2f}")
elif Metodo_de_pago == 2:
    print(f"Valor pagado en transferencia, {Valor_de_transferencia:.2f}")
elif Metodo_de_pago == 3:
    print(f"Valor pagado por datafono, {Valor_pagado_datafono:.2f}")

print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

# Muchas Gracias por su comprar Nombre_de_cliente
print(f"Muchas gracias por tu compra {Nombre_del_cliente}!")