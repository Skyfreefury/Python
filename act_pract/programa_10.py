#Christian Mogena DAW 2
'''
Este programa solicita los datos de una compra (cliente, producto, precio, cantidad, descuento e IVA) y muestra un ticket con el subtotal, el descuento, el IVA y el total a pagar.
'''
nombre_cliente = input("Introduzca su nombre: ")
producto = input("Introduzca el nombre del producto: ")
precio_unitario = float(input("Introduzca el precio unitario: "))
cant_comprada = int(input("Introduzca la cantidad comprada: "))
porcentaje_descuento = float(input("Introduzca el porcentaje a descontar: "))
porcentaje_iva = float(input("Introduzca el porcentaje del IVA: "))

subtotal = precio_unitario * cant_comprada
importe_descuento = subtotal * porcentaje_descuento/100
precio_despues_descuento = subtotal - importe_descuento
importe_iva = precio_despues_descuento * porcentaje_iva/100
total_de_pago = precio_despues_descuento + importe_iva

print(f"Cliente:   {nombre_cliente:>20}")
print(f"Producto:  {producto:>20}")
print(f"Cantidad:  {cant_comprada:>20}")
print(f"Subtotal:  {subtotal:>18.2f} €")
print(f"Descuento: {importe_descuento:>18.2f} €")
print(f"IVA:       {importe_iva:>18.2f} €")
print(f"TOTAL:     {total_de_pago:>18.2f} €")
