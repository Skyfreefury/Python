#Christian Mogena DAW 2
'''
Este programa solicita la base y la altura de un rectángulo y calcula su área, su perímetro y la longitud de su diagonal.
'''
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))
area = base*altura
perimetro = 2*(base+altura)
diagonal = ((base**2)+(altura**2))**0.5
print(f"El área del rectángulo es: {area:.2f}\n El perímetro es: {perimetro:.2f}\n La longitud de la diagonal es: {diagonal:.2f}")