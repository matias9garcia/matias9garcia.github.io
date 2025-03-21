import requests
from bs4 import BeautifulSoup
import json

# URL del perfil de Google Scholar
URL = "https://scholar.google.com/citations?user=q8bu48MAAAAJ&hl=es"

def obtener_publicaciones():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        print("Error al acceder a Google Scholar")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    publicaciones = []
    
    for row in soup.select(".gsc_a_tr"):
        titulo_elem = row.select_one(".gsc_a_t a")
        autores_elem = row.select_one(".gsc_a_t .gs_gray")
        año_elem = row.select_one(".gsc_a_y")
        
        if titulo_elem and autores_elem and año_elem:
            publicaciones.append({
                "titulo": titulo_elem.text,
                "autores": autores_elem.text,
                "año": año_elem.text.strip(),
                "enlace": f"https://scholar.google.com{titulo_elem['href']}"
            })
    
    return publicaciones

# Guardar en JSON
publicaciones = obtener_publicaciones()
with open("publicaciones.json", "w", encoding="utf-8") as f:
    json.dump(publicaciones, f, indent=4, ensure_ascii=False)

print("Publicaciones actualizadas correctamente.")
