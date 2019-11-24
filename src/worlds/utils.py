import urllib.request as rq

from bs4 import BeautifulSoup

from worlds.models import Image


def web_scraping():
    imagenes_actuales = list(Image.objects.values_list("url", flat=True))
    try:
        contenido_html = rq.urlopen(
            "https://www.eso.org/public/images/potw/list/1/"
        ).read().decode()
        soup = BeautifulSoup(contenido_html)
        publicaciones = soup.find_all("div", {"class": "news-wrapper"})
        for pub in publicaciones:
            url = pub.find("div", {"class": "news-image"}).find("img").get("src")
            titulo = pub.find("div", {"class": "news-title"}).get_text()
            descripcion = pub.find("div", {"class": "news-teaser"}).get_text()
            if url not in imagenes_actuales:
                Image.objects.create(url=url, title=titulo, description=descripcion)
    except:
        print("Hubo un error.")
