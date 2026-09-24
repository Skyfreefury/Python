#Christian Mogena DAW 2
'''
Este programa solicita al usuario que ingrese su nombre, edad, altura, residencia y experiencia en programación. Luego, muestra un mensaje personalizado con la información proporcionada y también indica el tipo de dato de la edad y la altura.
'''

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros: "))
residencia = input("Ingrese su residencia: ")
exp_programacion = input("Ingrese su experiencia en programación (Sí/No): ")
print(f"¡Hola, {nombre}! Tienes {edad} años, mides {altura} metros y vives en {residencia} // {exp_programacion} tiene experiencia en programación.")
print(f"Tipo de dato de edad: {type(edad)} y de altura: {type(altura)}")