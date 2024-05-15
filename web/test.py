import requests
from bs4 import BeautifulSoup
import json

#Funcion para traer los datos de la url
def get_a(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soupresponse = soup.find_all("a", href=True)
    
    jsonsim = {}
    
    if not soupresponse:
        return jsonsim
    else:
        for i in soupresponse:
            #Se verifica que la url no sea un enlace al mismo sitio
            if i.get("href") != "#":
                #Se verifica que la url sea http o https
                if i.get("href").startswith("http://") or i.get("href").startswith("https://"):
                    response_a = requests.get(i.get("href"))
                    soup_a = BeautifulSoup(response_a.text, "html.parser")
                    soupresponse1_a = soup_a.find_all("h1")
                    soupresponse2_a = soup_a.find_all("p")
                    
                    data = []
                    if soupresponse1_a:
                        data += [str(tag) for tag in soupresponse1_a]
                    if soupresponse2_a:
                        data += [str(tag) for tag in soupresponse2_a]
                    jsonsim[i.get("href")] = data
                
                else:
                    jsonsim[i.get("href")] = []
                
        return jsonsim
    
#Url de prueba
url = "https://www.google.com"

response_data = get_a(url)

#Se crea el archivo
with open('output.json', 'w') as outfile:
    json.dump(response_data, outfile)