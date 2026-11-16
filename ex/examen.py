import os
import sys
from datetime import datetime

# ---------- Lectura de la carpeta ----------

def procesar_archivos(carpeta):
    for archivo in os.listdir(carpeta):
        if not archivo.endswith(".txt"):
            continue
        ruta = os.path.join(carpeta, archivo)
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                ticket = parsear_lineas(f.read().splitlines())
                print(ticket)
        except Exception as e:
            print(f"Error al procesar el archivo '{archivo}': {e}")

# ---------- Parseo: cada función lee y valida su línea del ticket ----------

def parsear_numero(linea, ticket):
    if linea.startswith("Ticket:"):
        numero = linea.split(":")[1].strip()
        if not numero.isdigit():
            raise ValueError(f"número de ticket incorrecto: {numero}")
        ticket["numero"] = int(numero)


def parsear_cajero(linea, ticket):
    if linea.startswith("Cajero:"):
        codigo, nombre = linea.split(":")[1].split(" - ")
        if not codigo.strip().isdigit():
            raise ValueError(f"código de cajero incorrecto: {codigo}")
        ticket["cajero"] = (int(codigo), nombre.strip())


def parsear_fecha(linea, ticket):
    if linea.startswith("Fecha:"):
        partes = linea.split()
        ticket["fecha"] = datetime.strptime(partes[1] + " " + partes[3], "%d/%m/%Y %H:%M")


def parsear_pago(linea, ticket):
    if linea.startswith("FORMA DE PAGO:"):
        ticket["forma_pago"] = linea.split(":")[1].strip()
    elif linea.startswith("Autorización:"):
        ticket["autorizacion"] = linea.split(":")[1].strip()


def parsear_totales(linea, ticket):
    if linea.startswith("SUBTOTAL"):
        ticket["subtotal"] = float(linea.split()[-2])
    elif linea.startswith("IVA"):
        ticket["iva"] = float(linea.split()[-2])
    elif linea.startswith("TOTAL"):
        ticket["total"] = float(linea.split()[-2])


def parsear_producto(linea, ticket):
    partes = linea.split()
    if linea.startswith(" ") and partes and partes[0][0].isdigit():
        cantidad = float(partes[0])
        importe = float(partes[-2])
        if cantidad <= 0 or importe <= 0:
            raise ValueError(f"cantidad o importe incorrecto: {linea.strip()}")
        ticket["lineas"].append((cantidad, " ".join(partes[1:-2]), importe))


# ---------- Validación del ticket completo ----------

def validar_ticket(ticket):
    for campo in ("numero", "cajero", "fecha", "forma_pago", "subtotal", "iva", "total"):
        if campo not in ticket:
            raise ValueError(f"falta el campo {campo}")
    if not ticket["lineas"]:
        raise ValueError("ticket sin productos")
    if round(ticket["subtotal"] + ticket["iva"], 2) != ticket["total"]:
        raise ValueError("subtotal + IVA no coincide con el total")
    suma = sum(producto[2] for producto in ticket["lineas"])
    if round(suma, 2) != ticket["subtotal"]:
        raise ValueError("la suma de productos no coincide con el subtotal")


# ---------- Unión: recorre las líneas y aplica cada función ----------

def parsear_lineas(lineas):
    ticket = {"autorizacion": None, "lineas": []}
    for linea in lineas:
        parsear_numero(linea, ticket)
        parsear_cajero(linea, ticket)
        parsear_fecha(linea, ticket)
        parsear_pago(linea, ticket)
        parsear_totales(linea, ticket)
        parsear_producto(linea, ticket)
    validar_ticket(ticket)
    return ticket

# ---------- Programa principal ----------

def main():
    if len(sys.argv) < 2:
        print("Debe proporcionar al menos un argumento.")
        sys.exit(1)
    elif not os.path.isdir(sys.argv[1]):
        print(f"La carpeta '{sys.argv[1]}' no existe.")
        sys.exit(1)
    carpeta = sys.argv[1]
    procesar_archivos(carpeta)

if __name__ == "__main__":
    main()