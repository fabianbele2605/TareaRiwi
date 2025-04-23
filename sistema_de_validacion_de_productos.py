# Hola, Bienvenido a tu minisuper
print("Hola!,Bienvenido a tu minisuper!")

# Espacios
print("'''''''''''''''''''''''''''''''''''''''''''")
print("''''''''''''''''Hola!!'''''''''''''''''''''")
print("'''''''''Bienvenido a tu Minisuper'''''''''")
print("'''''''''''''''''''''''''''''''''''''''''''")
print("'''''''''''''''''''''''''''''''''''''''''''")

# Datos de cliente
Nombre_del_cliente = str(input("Ingresa tu nombre=> "))
# Hola!, "nombre del cliente"
print("Hola!", Nombre_del_cliente)
Numero_de_documento = int(input("Ingresa numero de identidad=>"))
# 

# Sistema de validacion de Productos

Nombre_del_producto = str(input("Ingrese el nombre del producto=> "))
Precio_unitario = float(input("Ingrese el precio unitario=> "))
Cantidad_de_productos = int(input("Ingresa la cantidad de productos adquiridos=>" ))

# Valor de la compra
valor_de_la_compra = Precio_unitario * Cantidad_de_productos
print(f"Valor a pagar ${Precio_unitario * Cantidad_de_productos:.2f}")

# Ingresa "si" tu producto tienes descuento, sino tiene di "no"
print("Ingresa Si o No,el producto tiene descuento")
Si_O_No = bool(input(""))

# Valor de descuento del producto
print(f"Ingresa el valor de descuento del {Nombre_del_producto}:")
Valor_de_descuento_del_producto = int(input(""))

# Valor total del producto con descuento
Valor_total_del_producto_con_descuento = valor_de_la_compra * (1 -(Valor_de_descuento_del_producto / 100))
print(f"Valor con descuento a pagar del {Nombre_del_producto} es: ${valor_de_la_compra * (1 -(Valor_de_descuento_del_producto / 100)):.2f}")
print(f"Valor ahorrado ${valor_de_la_compra - Valor_total_del_producto_con_descuento:.2f}")

# Metodo de pago
print("Que metodo de pago desea pagar")
Metodo_de_pago = str(input("Ingresa el metodo de pago=>"))

# Ingresa el valor en efectivo
Valor_en_efectivo = float(input("Ingresa el valor en efectivo $"))

# Valor pagado y valor devuelto
print(f"Valor pagado en efectivo ${Valor_en_efectivo:.2f}")
print(f"Valor devuelto ${Valor_en_efectivo - Valor_total_del_producto_con_descuento:.2f}")


# Muchas Gracias por su comprar Nombre_de_cliente
print(f"Muchas gracias por tu compra {Nombre_del_cliente}!")