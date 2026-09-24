#Christian Mogena DAW 2
'''
Este programa pide al usuario que inserte los grados celsius y los transforma en Fahrenheit y Kelvin
'''
grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
grados_fahrenheit = grados_celsius * 9 / 5 + 32
grados_kelvin = grados_celsius + 273.15
print(f"Los {grados_celsius} transformados en\n Fahrenheit son: {grados_fahrenheit:.2f}\n Kelvin son: {grados_kelvin:.2f}")