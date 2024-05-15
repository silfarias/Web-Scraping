import requests
from bs4 import BeautifulSoup


url = 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)


# Busca las imagenes que tengan la clase "dynamic-carousel__img"
results = soup.find_all('img', class_="dynamic-carousel__img")

for img in results:
    print(img['data-src'])

