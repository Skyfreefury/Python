def main():
    nombre = input("Ingrese su nombre: ")
    saludo =mensaje(nombre)
    print(saludo)
def mensaje(nombre):
    return f"Hola, {nombre}!"
if __name__ == "__main__":
    main()