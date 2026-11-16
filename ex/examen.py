import os
import sys

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

def parsear_lineas(lineas):
    ticket = {}
    ticket["autorizacion"] = None
    ticket["lineas"] = []
    for linea in lineas:
        if linea.startswith("Ticket:"):
            ticket["numero"] = int(linea.split(":")[1])
        elif linea.startswith("Cajero:"):
            codigo, nombre = linea.split(":")[1].split(" - ")
            ticket["cajero"] = (int(codigo), nombre.strip())
        elif linea.startswith("Fecha:"):
            ticket["fecha"] = linea.split()[1], linea.split()[3]
        elif linea.startswith("FORMA DE PAGO:"):
            ticket["forma_pago"] = linea.split(":")[1].strip()
        elif linea.startswith("Autorización:"):
            ticket["autorizacion"] = linea.split(":")[1].strip()
        elif linea.startswith("SUBTOTAL"):
            ticket["subtotal"] = float(linea.split()[-2])
        elif linea.startswith("IVA"):
            ticket["iva"] = float(linea.split()[-2])
        elif linea.startswith("TOTAL"):
            ticket["total"] = float(linea.split()[-2])
        elif linea.startswith(" ") and linea.split() and linea.split()[0][0].isdigit():
            partes = linea.split()
            cantidad = float(partes[0])
            descripcion = " ".join(partes[1:-2])
            importe = float(partes[-2])
            ticket["lineas"].append((cantidad, descripcion, importe))
    for campo in ("numero", "cajero", "fecha", "forma_pago", "subtotal", "iva", "total"):
        if campo not in ticket:
            raise ValueError(f"falta el campo {campo}")
    if not ticket["lineas"]:
        raise ValueError("ticket sin productos")
    if round(ticket["subtotal"] + ticket["iva"], 2) != ticket["total"]:
        raise ValueError("subtotal + IVA no coincide con el total")
    suma = sum(linea[2] for linea in ticket["lineas"])
    if round(suma, 2) != ticket["subtotal"]:
        raise ValueError("la suma de productos no coincide con el subtotal")
    return ticket

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