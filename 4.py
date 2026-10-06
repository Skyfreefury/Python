def pedir_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                print("Error: La edad no puede ser negativa.")
                continue
            return edad
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def pedir_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                continue
            return precio
        except ValueError:
            print("Error: Ingrese un valor decimal válido.")

def main():
    edad = pedir_edad()
    precio = pedir_precio()

    print(f"\nEdad ingresada: {edad}")
    print(f"Precio ingresado: {precio:.2f}")

if __name__ == "__main__":
    main()