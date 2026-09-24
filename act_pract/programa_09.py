#Christian Mogena DAW 2
'''
Este programa solicita la edad del usuario, si tiene autorización y si dispone de identificación, y calcula distintos resultados booleanos sobre su acceso.
'''
edad_usuario = int(input("Introduzca su edad: "))
autorizacion = input("¿Tiene autorización? (Si/No): ")
identificacion = input("¿Dispone de identificación? (Si/No): ")
tiene_autorizacion = autorizacion.lower() == "si"
tiene_identificacion = identificacion.lower() == "si"
es_mayor_de_edad = edad_usuario >= 18
acceso_completo = es_mayor_de_edad and tiene_autorizacion and tiene_identificacion
acceso_supervisado = tiene_autorizacion or es_mayor_de_edad
acceso_bloqueado = not tiene_identificacion
print(f"¿Es mayor de edad?: {es_mayor_de_edad}")
print(f"¿Acceso completo?: {acceso_completo}")
print(f"¿Acceso supervisado?: {acceso_supervisado}")
print(f"¿Acceso bloqueado?: {acceso_bloqueado}")
