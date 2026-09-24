#Christian Mogena DAW 2
'''
Este ejercicio pide al usuario una cantidad de segundos y lo transforma en horas:minutos:segundos
'''
segundos = int(input("Introduce la cantidad de segundos a transformar: "))
horas = segundos // 3600
resto_tras_horas = segundos % 3600
minutos = resto_tras_horas // 60
segundos_restantes = resto_tras_horas % 60
print(f"{horas:02}:{minutos:02}:{segundos_restantes:02}")