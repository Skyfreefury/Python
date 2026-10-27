import requests

from bs4 import BeautifulSoup

URL = "https://www.dolar-scraping.docker.sulbaranjc.com/"

def obtener_valor()-> str:
    # Realiza una solicitud HTTP GET a la URL especificada y devuelve el valor del dólar en formato de cadena.
    respuesta = requests.get(URL, timeout=5)
    respuesta.raise_for_status()
    
    # Analiza el contenido HTML de la respuesta utilizando BeautifulSoup
    sopa = BeautifulSoup(respuesta.text, "html.parser")
    elemento = sopa.find(id="usd-eur-rate")
    if elemento is None:
        raise ValueError("No se encontró el elemento con id 'usd-eur-value' en la página.")
    
    # Devuelve el texto del elemento encontrado, que contiene el valor del dólar
    return elemento.get_text(strip=True)
if __name__ == "__main__":
    try:
        print(f"1 USD = {obtener_valor()} EUR")
    except (requests.RequestException, ValueError) as error:
        print(f"Error al obtener el valor del dólar: {error}")
        raise SystemExit(1)