#Christian Mogena DAW 2
'''
Este programa solicita el número total de entradas disponibles y el número de grupos que las recibirán, y calcula cuántas entradas completas recibe cada grupo y cuántas quedan sin repartir.
'''
entradas_disponibles = int(input("Introduzca el total de entradas disponibles: "))
grupos_presentes = int(input("Introduzca el total de grupos que recibirán las entradas: "))
entradas_entregadas = entradas_disponibles // grupos_presentes
entradas_sin_repartir = entradas_disponibles % grupos_presentes
print(f"Cada grupo recibe {entradas_entregadas} para estar parejos")
print(f"Quedan sin repartir {entradas_sin_repartir} entradas")
