try:
    dividendo = float(input("A: "))
    divisor = float(input("B: "))
    resultado = dividendo/divisor
    print(f"El resultado es: {resultado:.2f}")
except ValueError:
    print("Formato numerico no valido")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
    
try:
    edad = int(input("Edad: "))
except Exception:
    print("Algo salio mal papi")
else:
    print("Bueno al parecer no eres tan down de introducir la edad mal")
finally:
    print("Gracias por usarme UwU")
    
