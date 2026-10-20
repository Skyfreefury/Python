def buscar_palabra(palabra,doc):
    with open(doc, "r", encoding="utf-8") as f:
        contenido = f.read()
        palabra_doc = contenido.lower().split()
        veces = palabra_doc.count(palabra.lower())
    return f"Se encontró la palabra '{palabra}' en el documento '{doc}': {veces} veces"

def pedir_palabra_doc():
    palabra = input("Ingrese la palabra a buscar: ")
    doc = input("Ingrese el nombre del documento (con extensión): ")
    return palabra, doc

def main():
    palabra, doc = pedir_palabra_doc()
    resultado = buscar_palabra(palabra, doc)
    print(resultado)

if __name__ == "__main__":
    main()