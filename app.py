import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.fravega.com/e/categorias/tecnologia-celulares/'
response = requests.get(url)

def obtencion_enlaces():
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []  # Lista donde se almacenarán los enlaces
        
        search = soup.find_all('a')
        for link in search:
            href = link.get('href')
            if href and (href.startswith('http') or href.startswith('https')):
                links.append(href)
        return links
    else:
        print('Error en la petición, Pagina no encontrada', response.status_code)
        return []


json_enl = {} # Diccionario donde se almacenarán los enlaces

def almacenar_enlaces(enlaces):
    for enlace in enlaces:
        try:
            response_enl = requests.get(enlace)
            if response_enl.status_code == 200:
                soup_enl = BeautifulSoup(response_enl.text, 'html.parser')
                res1 = soup_enl.find_all('h1')
                res2 = soup_enl.find_all('p')
                
                datos = []
                
                if res1:
                    datos += [str(i) for i in res1]
                if res2:
                    datos += [str(i) for i in res2]
                    
                json_enl[enlace] = datos
            else:
                json_enl[enlace] = []
        except requests.exceptions.RequestException as e:
            print(f'Error al acceder al enlace {enlace}: {e}')
            json_enl[enlace] = []
        except Exception as e:
            print(f'Error al procesar el enlace {enlace}: {e}')
            json_enl[enlace] = []
    print('Enlaces almacenados correctamente')

    # Guardar el diccionario en un archivo JSON
    with open('resultados.json', 'w', encoding='utf-8') as file:
        json.dump(json_enl, file, ensure_ascii=False, indent=4)

enlaces = obtencion_enlaces()
almacenar_enlaces(enlaces)