import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.fravega.com/e/categorias/tecnologia-celulares/'
response = requests.get(url)


def obtención_enlaces():
    soup = BeautifulSoup(response.text, 'html.parser')
    search = soup.find_all('a')
    for link in search:
        if link.get('href') is not None:
            if link.get('href').startswith('http') or link.get('href').startswith('https'):
                return link.get('href') 


enlaces = obtención_enlaces()
json_enl = {} 

def almacenar_enlaces():
    
    response_enl = requests.get(enlaces)
    soup_enl = BeautifulSoup(response_enl.text, 'html.parser')
    res1 = soup_enl.find_all('h1')
    res2 = soup_enl.find_all('p')

    datos = []
    
    if res1:
        datos += [ str(i) for i in res1 ]
    if res2:
        datos += [ str(i) for i in res2 ]
    json_enl[enlaces] = datos
    
    return json_enl

response_data = almacenar_enlaces()

with open('enlaces.json', 'w') as file:
    json.dumps(response_data, file)