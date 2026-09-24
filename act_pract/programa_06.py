#Christian Mogena
'''
Este programa pide al usuario 2 números y le aplica cálculos como suma, resta, multiplicación, división, división entera, resto o módulo, potencia
'''
primer_numero = float(input("Introduce el primer número: "))
segundo_numero = float(input("Introduce el segundo número: "))
print(f"El resultado entre {primer_numero} + {segundo_numero} es: {primer_numero+segundo_numero}")
print(f"El resultado entre {primer_numero} - {segundo_numero} es: {primer_numero-segundo_numero}")
print(f"El resultado entre {primer_numero} * {segundo_numero} es: {primer_numero*segundo_numero}")
print(f"El resultado entre {primer_numero} / {segundo_numero} es: {primer_numero/segundo_numero}")
print(f"El resultado entre {primer_numero} // {segundo_numero} es: {primer_numero//segundo_numero} (división entera)")
print(f"El resultado entre {primer_numero} % {segundo_numero} es: {primer_numero%segundo_numero} (resto o módulo)")
print(f"El resultado entre {primer_numero} elevado a {segundo_numero} es: {primer_numero**segundo_numero}")

