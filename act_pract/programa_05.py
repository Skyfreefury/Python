#Christian Mogena DAW 2
'''
Este programa solicita el nombre del trabajador, las horas trabajadas, el precio por hora y el porcentaje de retención, y calcula el salario bruto, el importe de la retención y el salario neto.
'''
nombre_trabajador = input("Introduce tu nombre: ")
horas_trabajadas = int(input("Cantidad de horas trabajadas: "))
precio_hora = float(input("Precio por hora trabajada: "))
retencion_porcentaje = float(input("¿Qué % te retienen?: "))

salario_bruto = horas_trabajadas * precio_hora
importe_retencion = salario_bruto * (retencion_porcentaje/100)
salario_neto = salario_bruto - importe_retencion

print(f"Nombre: {nombre_trabajador}\n Salario bruto: {salario_bruto:.2f}\n Importe de retención: {importe_retencion:.2f}\n Salario neto: {salario_neto:.2f}")
