import sys

def buscar_palabra(palabra, doc):
    try:
        with open(doc, "r", encoding="utf-8") as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{doc}'")
        sys.exit(1)
    palabra_doc = contenido.lower().split()
    veces = palabra_doc.count(palabra.lower())
    return f"{palabra}: {veces}"

# def pedir_palabra_doc():
#     palabra = input("Ingrese la palabra a buscar: ")
#     doc = input("Ingrese el nombre del documento (con extensión txt): ")
#     return palabra, doc

def main():
    if len(sys.argv) < 3:
        print("Uso: python Buscar_palabra_en_fichero.py <palabra> <archivo>")
        sys.exit(1)
    palabra = sys.argv[1]
    doc = sys.argv[2]
    resultado = buscar_palabra(palabra, doc)
    print(resultado)

if __name__ == "__main__":
    main()