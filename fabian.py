# Hola, Bienvenido a tu minisuper
# Espacio
print("'''''''''''''''''''''''''''''''''''''''''''")
print("''''''''''''''''Hola!!'''''''''''''''''''''")
print("'''''''''Bienvenido a tu Minisuper'''''''''")
print("'''''''''''''''''''''''''''''''''''''''''''")
print("'''''''''''''''''''''''''''''''''''''''''''")

# Datos de cliente
# Ingresar nombre de cliente
while True:
    try:
        Nombre_de_cajero = str(input("Ingresa nombre del cajero =>"))
        if Nombre_de_cajero == "" :
            print("Por favor confirmar nombre del cajero!")
            continue
        break
    except ValueError:
        print()   

print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print()        
# Datos de cliente
# Ingresar nombre de cliente
Nombre_del_cliente = str(input("Ingresa nombre de cliente=> "))
# Codigo para que no lea numeros como caracteres de texto
Nombre_del_cliente = "".join(char for char in Nombre_del_cliente if not char.isdigit())
#print(Nombre_del_cliente)
# Hola!, "nombre del cliente"
print("'''''''''''''''''''''''''''''''''''''''''''")
print("        Hola!", Nombre_del_cliente )
print("'''''''''''''''''''''''''''''''''''''''''''")
# Ingresar Numero de identidad
Numero_de_documento = int(input("Ingresa numero de identidad=> "))

# Datos Guardados del cliente
print("''''''''''''''''''''''''''''''''''''''''''''")
print("              Datos del cliente                 ")
print("  Nombre de cliente      Numero de identidad")
print(f"    {Nombre_del_cliente}                  {Numero_de_documento}")
print("''''''''''''''''''''''''''''''''''''''''''''")


# Sistema de ingreso de productos,precios y cantidad

Nombre_del_producto = str(input("Ingrese el nombre del producto=> "))

while True:
    try:
        Precio_unitario = float(input("Ingrese el precio unitario=>"))
        if Precio_unitario < 0:
            print("El precio no debe ser negativo. Intenta de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada invalida. Por favor, Ingresa un numero valido para el precio.")
        
        
while True:
    try:
        Cantidad_de_productos = float(input("Ingrese la cantidad de productos=>"))
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
print(f"    {Nombre_del_producto}                     $ {Precio_unitario:.2f}                {Cantidad_de_productos:.0f}")
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")


# Ingresa "si" tu producto tienes descuento, sino tiene di "no"
#print("Ingresa Si o 0,el producto tiene descuento")
print("Ingresa el descuento (0 si no hay descuento)")
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
print("Que metodo de pago desea pagar")
Metodo_de_pago = str(input("Ingresa el metodo de pago=>"))
Metodo_de_pago = "".join(char for char in Metodo_de_pago if not char.isdigit())
print(Metodo_de_pago)

# Ingresa el valor en efectivo
#Valor_en_efectivo = float(input("Ingresa el valor en efectivo $"))
while True:
    try:
        Valor_en_efectivo = float(input("Ingrese el valor en efectivo=>"))
        if Valor_en_efectivo < 0:
            print("El valor no debe ser negativo. Intenta de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada invalida. Por favor, Ingresa un numero valido para el valor.")

# Valor pagado y valor devuelto
print(f"Valor pagado en efectivo ${Valor_en_efectivo:.2f}")
print(f"Valor devuelto ${Valor_en_efectivo - Valor_total_del_producto_con_descuento:.2f}")
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")


# Factura de compra
print("'''''''''''''''''''''''''''''''''''''''''''''''''''")
print("            Factura de compra                  ")
print(f"Nombre del cliente        {Nombre_del_cliente}")
print(f"Numero de identidad       {Numero_de_documento}")
print(f"Valor del producto       ${Precio_unitario:.2f}")
print(f"Cantidad de producto      {Cantidad_de_productos:.0f}")
print(f"Valor por los productos  ${valor_de_la_compra:.2f}")
print(f"valor de descuento        {Valor_de_descuento_del_producto:}%")
print(f"Valor con descuento a pagar   ${Valor_total_del_producto_con_descuento:.2f}")
print(f"Valor ahorrado            ${valor_de_la_compra - Valor_total_del_producto_con_descuento:.2f}")
print(f"Metodo de pago            {Metodo_de_pago}")
print(f"Recibido en efectivo      ${Valor_en_efectivo:.2f}")
print(f"Valor devuelto           ${Valor_en_efectivo - Valor_total_del_producto_con_descuento:.2f}")


# Muchas Gracias por su comprar Nombre_de_cliente
print(f"Muchas gracias por tu compra {Nombre_del_cliente}!")