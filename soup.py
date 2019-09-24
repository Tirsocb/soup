#!/usr/bin/env python3
from idlelib.multicall import r

from bs4 import BeautifulSoup
import requests, sys, csv, json


def Navigate(zelda):
    try:
        html = requests.get(zelda).text
        print("success")

    except:

        sys.exit(1)

    maruchan = BeautifulSoup(html, "html.parser")

    return maruchan


url = "http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
# print(soup.prettify())

print(soup.title)
print(soup.title.string)

for div in soup.find_all("div"):
    print(div)
    print("--------------------------")


def Separador():
    print("---------------------------------------")


def Separador_Inciso():
    print("=======================================")


def Nombre():
    print("Tirso Córdova Briz")


def Portal():
    Separador_Inciso()
    print("Portal")
    Separador_Inciso()
    Separador()
    Nombre()
    Separador()

    Separador()
    print(f"GET the title and print it: {soup.title.string}")
    Separador()
    direction = soup.find("a", {"href": "#myModal"})
    print(f"Complete address: {direction.text}")
    Separador()
    email = soup.find("a", {"href": "mailto:inf@ufm.edu"})
    tel = phone = soup.find("a", {"href": "tel:+50223387700"})
    print(f"Email: {email.text}")
    print(f"Teléfono: {tel.text}")
    Separador()
    menubar = soup.find("table", {"id": "menu-table"})
    print(f"menubar: {menubar.text}")
    Separador()
    allHref = soup.find_all("a", href=True)
    print(f"all properties that have href (link to somewhere): {allHref}")
    Separador()
    ufmMail = soup.find(id='ufmail_')['href']
    print(f"UFM mail button href: {ufmMail}")
    Separador()
    miu = soup.find(id='miu_')['href']
    print(f"MiU href: {miu}")
    Separador()
    imgs = soup.find_all("img")
    for img in imgs:
        print(f"image URL: {img['src']}")

    Separador()
    counter = 0
    for a in soup.find_all("a"):
        counter = counter + 1
    print(f"Number of <a> tags: {counter}")
    Separador_Inciso()





def Estudios():
    Separador_Inciso()
    print("Estudios")
    Separador_Inciso()
    link = "http://ufm.edu/Estudios"
    ramen = Navigate(link)
    Separador()
    Nombre()
    Separador()
    topmenu = ramen.find('div', {"id": "topmenu"})
    print(f"top menu items: {topmenu.text}")
    Separador()
    estudios = ramen.find_all("div", {"class": "estudios"})
    print(f"Estudios disponibles: {estudios} \n")
    Separador()
    leftbar = ramen.find("div", {"class": "leftbar"}).find_all("li")
    print(f"leftbar list Items: {leftbar}")
    Separador()
    redes = ramen.find("div", {"class": "social pull-right"}).find_all("a")
    print(f"redes sociales: {redes}")
    Separador()
    counter = 0
    for a in ramen.find_all("a"):
        counter = counter + 1
    print(f"Number of <a> tags: {counter}")
    Separador_Inciso()


def CS():
    Separador_Inciso()
    print("CS")
    Separador_Inciso()
    link = "https://fce.ufm.edu/carrera/cs/"
    ramen = Navigate(link)
    Separador()
    Nombre()
    Separador()
    print(f"title : {ramen.title.string}")
    Separador()
    foto = ramen.find("img", {"class": "fl-photo-img wp-image-500 size-full"})
    print(f"foto: {foto}")
    open('Facultad_de_Ciencias_Economicas.png', 'wb')
    print("la foto se encuentra en el proyecto")
    Separador()
    print("meta" + str(ramen.find("meta",  property="og:title")))
    print("meta" + str(ramen.find("meta",  property="og:description")))
    Separador()
    counter = 0
    for a in ramen.find_all("a"):
        counter = counter + 1
    print(f"Number of <a> tags: {counter}")
    Separador()
    counter = 0
    for a in ramen.find_all("div"):
        counter = counter + 1
    print(f"Number of <div> tags: {counter}")
    Separador_Inciso()
# CS()
# Estudios()
# Portal()
