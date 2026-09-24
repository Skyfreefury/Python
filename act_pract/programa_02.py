#Christian Mogena DAW 2
'''
Este programa solicita al usuario el nombre del producto, su precio y la cantidad de unidades. Luego calcula el importe sin IVA, el IVA correspondiente y el importe total con IVA, mostrando los resultados en pantalla.
'''

nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
und_producto = int(input("Ingrese la cantidad de unidades del producto: "))
iva = float(input("Ingrese el porcentaje de IVA del producto: "))
importe_producto_sin_iva = precio_producto * und_producto
iva_del_producto = importe_producto_sin_iva * (iva/100)
importe_producto_con_iva = importe_producto_sin_iva + iva_del_producto
print(f"El precio de {nombre_producto} sin IVA es de {importe_producto_sin_iva:.2f} euros")
print(f"El IVA del producto es de {iva_del_producto:.2f} euros")
print(f"El importe con IVA es de {importe_producto_con_iva:.2f} euros")