# Web Scraping con Python

Este proyecto implementa un web crawler en Python que recorre un sitio web extrae todas las etiquetas `<a>` con sus respectivos enlaces y accede a cada página enlazada. Por cada enlace encontrado, se obtienen todas las etiquetas `<h1>` y `<p>` y se almacenan en un archivo JSON.

## Funcionalidad

- **Extracción de enlaces**: El web crawler recorre el sitio web especificado y extrae todas las etiquetas `<a>` con sus respectivos enlaces.
- **Acceso a enlaces**: Accede a cada enlace encontrado y obtiene el contenido de la página enlazada.
- **Almacenamiento de datos**: Extrae todas las etiquetas `<h1>` y `<p>` de cada página enlazada y las almacena en un archivo JSON en el formato especificado.

## Requisitos para su uso

- Python 3.x
- Bibliotecas `requests` y `BeautifulSoup` (pueden instalarse mediante `pip`)

### Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias:

```bash
pip install requests beautifulsoup4
```

### Ejecución

Ejecuta el script `app.py` para iniciar el web crawler:

```bash
python app.py
```