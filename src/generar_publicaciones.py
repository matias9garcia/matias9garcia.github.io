import requests
from bs4 import BeautifulSoup
import json

# URL del perfil de Google Scholar
url = "https://scholar.google.com/citations?user=Bv5wnYoAAAAJ&hl=es"

# Headers para simular un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

try:
    # Hacer la solicitud
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Procesar el contenido HTML
    soup = BeautifulSoup(response.content, "html.parser")
    publicaciones = []

    # Buscar publicaciones en el HTML
    for fila in soup.select("tr.gsc_a_tr"):
        titulo = fila.select_one(".gsc_a_at").text
        autores = fila.select_one(".gsc_a_at + div").text
        año = fila.select_one(".gsc_a_y span").text if fila.select_one(".gsc_a_y span") else "N/A"
        publicaciones.append({
            "titulo": titulo,
            "autores": autores,
            "año": año
        })

    # Guardar las publicaciones en un archivo JSON
    with open("publicaciones.json", "w", encoding="utf-8") as f:
        json.dump(publicaciones, f, indent=4, ensure_ascii=False)

    print(f"Se generó el archivo publicaciones.json con {len(publicaciones)} publicaciones.")

except requests.exceptions.RequestException as e:
    print("Error al conectar:", e)
