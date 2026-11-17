import os
import sys
from datetime import datetime

# ---------- Lectura de la carpeta ----------

def procesar_archivos(carpeta):
    datos = {"sucursal": {}, "empleado": {}, "producto": {}, "forma_pago": {}, "ticket": {}}
    for archivo in os.listdir(carpeta):
        if not archivo.endswith(".txt"):
            continue
        ruta = os.path.join(carpeta, archivo)
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                ticket = parsear_lineas(f.read().splitlines())
                guardar_ticket(ticket, datos)
        except Exception as e:
            print(f"Error al procesar el archivo '{archivo}': {e}")
    print(f"Tickets: {len(datos['ticket'])} | Empleados: {len(datos['empleado'])} | Productos: {len(datos['producto'])} | Formas de pago: {len(datos['forma_pago'])}")
    return datos

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
        
def parsear_sucursal(lineas, ticket):
    ticket["sucursal_nombre"] = lineas[0].strip()
    ticket["sucursal_direccion"] = lineas[1].strip()
    partes = lineas[2].split()
    ticket["cif"] = partes[1].strip()
    ticket["telefono"] = partes[3].strip()
    if len(ticket["cif"]) != 9:
        raise ValueError(f"CIF incorrecto: {ticket['cif']}")

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
    parsear_sucursal(lineas, ticket)
    for linea in lineas:
        parsear_numero(linea, ticket)
        parsear_cajero(linea, ticket)
        parsear_fecha(linea, ticket)
        parsear_pago(linea, ticket)
        parsear_totales(linea, ticket)
        parsear_producto(linea, ticket)
    validar_ticket(ticket)
    return ticket

# ---------- Eliminación de duplicados: guarda cada dato una sola vez ----------

def guardar_ticket(ticket, datos):
    if ticket["numero"] in datos["ticket"]:
        raise ValueError(f"ticket repetido: {ticket['numero']}")
    datos["sucursal"].setdefault(ticket["cif"], {"id": len(datos["sucursal"]) + 1, "nombre": ticket["sucursal_nombre"], "direccion": ticket["sucursal_direccion"], "telefono": ticket["telefono"]})
    datos["empleado"].setdefault(ticket["cajero"][0], {"nombre": ticket["cajero"][1], "sucursal_id": datos["sucursal"][ticket["cif"]]["id"]})
    datos["forma_pago"].setdefault(ticket["forma_pago"], len(datos["forma_pago"]) + 1)
    for cantidad, descripcion, importe in ticket["lineas"]:
        datos["producto"].setdefault(descripcion, {"id": len(datos["producto"]) + 1, "precio": round(importe / cantidad, 2)})
    datos["ticket"][ticket["numero"]] = ticket



# ---------- Generación del SQL: escribe los INSERT en el fichero ----------

def generar_sql(datos, fichero):
    sql = ["USE tickets_db;"]
    for cif, s in datos["sucursal"].items():
        sql.append(f"INSERT INTO sucursal (id, cif, nombre, direccion, telefono) VALUES ({s['id']}, '{cif}', '{s['nombre']}', '{s['direccion']}', '{s['telefono']}');")
    for codigo, e in datos["empleado"].items():
        sql.append(f"INSERT INTO empleado (id, nombre, sucursal_id) VALUES ({codigo}, '{e['nombre']}', {e['sucursal_id']});")
    for nombre, id_pago in datos["forma_pago"].items():
        sql.append(f"INSERT INTO forma_pago (id, nombre) VALUES ({id_pago}, '{nombre}');")
    for descripcion, p in datos["producto"].items():
        sql.append(f"INSERT INTO producto (id, descripcion, precio) VALUES ({p['id']}, '{descripcion}', {p['precio']});")
    for numero, t in datos["ticket"].items():
        autorizacion = f"'{t['autorizacion']}'" if t["autorizacion"] else "NULL"
        sql.append(f"INSERT INTO ticket (numero, fecha_hora, empleado_id, subtotal, iva, total, forma_pago_id, autorizacion) "
                   f"VALUES ({numero}, '{t['fecha']}', {t['cajero'][0]}, {t['subtotal']}, {t['iva']}, {t['total']}, "
                   f"{datos['forma_pago'][t['forma_pago']]}, {autorizacion});")
        for cantidad, descripcion, importe in t["lineas"]:
            sql.append(f"INSERT INTO ticket_linea (ticket_numero, producto_id, cantidad, importe) "
                       f"VALUES ({numero}, {datos['producto'][descripcion]['id']}, {cantidad}, {importe});")
    with open(fichero, "w", encoding="utf-8") as f:
        f.write("\n".join(sql))


# ---------- Programa principal ----------

def main():
    if len(sys.argv) < 2:
        print("Debe proporcionar al menos un argumento.")
        sys.exit(1)
    elif not os.path.isdir(sys.argv[1]):
        print(f"La carpeta '{sys.argv[1]}' no existe.")
        sys.exit(1)
    carpeta = sys.argv[1]
    datos = procesar_archivos(carpeta)
    generar_sql(datos, "insert_ticket.sql")


if __name__ == "__main__":
    main()