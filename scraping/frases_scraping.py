import sys
import requests
from bs4 import BeautifulSoup

# Fuerza que la consola de Windows imprima en UTF-8, para que tildes, comillas
# tipográficas y otros caracteres especiales se vean bien.
sys.stdout.reconfigure(encoding="utf-8")

URL = "https://quotes.toscrape.com/"

def obtener_frases() -> list[dict]:
    # Realiza una solicitud HTTP GET a la URL especificada
    respuesta = requests.get(URL, timeout=5)
    respuesta.raise_for_status()

    # Analiza el contenido HTML de la respuesta utilizando BeautifulSoup
    sopa = BeautifulSoup(respuesta.text, "html.parser")

    # Cada frase está dentro de un <div class="quote">, y hay varias en la página
    divs_frases = sopa.find_all("div", class_="quote")
    if not divs_frases:
        raise ValueError("No se encontraron frases en la página.")

    frases = []
    for div in divs_frases:
        texto = div.find("span", class_="text").get_text(strip=True)
        autor = div.find("small", class_="author").get_text(strip=True)
        etiquetas = [tag.get_text(strip=True) for tag in div.find_all("a", class_="tag")]
        frases.append({"texto": texto, "autor": autor, "etiquetas": etiquetas})

    return frases

if __name__ == "__main__":
    try:
        frases = obtener_frases()
        for i, frase in enumerate(frases, start=1):
            print(f"{i}. \"{frase['texto']}\" — {frase['autor']}")
            print(f"   Etiquetas: {', '.join(frase['etiquetas'])}")
    except (requests.RequestException, ValueError) as error:
        print(f"Error al obtener las frases: {error}")
        raise SystemExit(1)
