from django.shortcuts import render, loader
from django.http import HttpResponse
import json
from .models import Characters, Location, Episode
import requests

urlu = "https://rickandmortyapi.com/api/"

def index(request):
    respuesta = todos_episodios()
    lista = []
    for epi in respuesta:
        lista.append(Episode(id=epi["id"], name=epi["name"],
                             air_date=epi["air_date"], episode=epi["episode"],
                             characters=epi["characters"],url=epi["url"],
                             created=epi["created"]))

    context = {
        'lista_episodios': lista,
    }
    return render(request, 'RickyM/index.html', context)


def Characters_page(request, Characters_id):
    respuesta = personaje(urlu + "character/" + str(Characters_id))
    lista_episodios = []

    for i in respuesta["episode"]:
        epi = episodio(i)
        lista_episodios.append((epi["id"], epi["name"]))

    if respuesta["origin"]["url"] != "":
        loc = lugar(respuesta["origin"]["url"])
        origen = (loc["id"], loc["name"])

        if respuesta["location"]["url"] != "":
            locf = lugar(respuesta["location"]["url"])
            actual = (locf["id"], locf["name"])
            character = (Characters(id=respuesta["id"], name=respuesta["name"], status=respuesta["status"],
                                    species=respuesta["species"], type=respuesta["type"],
                                    gender=respuesta["gender"], origin=origen, image=respuesta["image"],
                                    location=actual, episode=lista_episodios,
                                    url=respuesta["url"], created=respuesta["created"]))
        else:
            character = (Characters(id=respuesta["id"], name=respuesta["name"], status=respuesta["status"],
                                    species=respuesta["species"], type=respuesta["type"],
                                    gender=respuesta["gender"], origin=origen, image=respuesta["image"],
                                    episode=lista_episodios,
                                    url=respuesta["url"], created=respuesta["created"]))

    elif respuesta["location"]["url"] != "":
        locf = lugar(respuesta["location"]["url"])
        actual = (locf["id"], locf["name"])
        character = (Characters(id=respuesta["id"], name=respuesta["name"], status=respuesta["status"],
                                species=respuesta["species"], type=respuesta["type"],
                                gender=respuesta["gender"], image=respuesta["image"],
                                location=actual, episode=lista_episodios,
                                url=respuesta["url"], created=respuesta["created"]))
    else:
        character = (Characters(id=respuesta["id"], name=respuesta["name"], status=respuesta["status"],
                                species=respuesta["species"], type=respuesta["type"],
                                gender=respuesta["gender"], image=respuesta["image"],
                                episode=lista_episodios,
                                url=respuesta["url"], created=respuesta["created"]))

    context = {
        'personaje': character
    }
    return render(request, 'RickyM/Personaje.html', context)

def Location_page(request, Location_id):
    respuesta = lugar(urlu + "location/" + str(Location_id))
    lista_personajes = []
    for i in respuesta["residents"]:
        per = personaje(i)
        lista_personajes.append((per["id"], per["name"]))
    location = Location(id=respuesta["id"], name=respuesta["name"], type=respuesta["type"],
                        dimension=respuesta["dimension"], residents=lista_personajes,
                        url=respuesta["url"], created=respuesta["created"])
    context = {
        'lugar': location
    }
    return render(request, 'RickyM/Lugar.html', context)


def Episode_page(request, Episode_id):
    respuesta = episodio(urlu + "episode/" + str(Episode_id))
    lista_personajes = []

    for i in respuesta["characters"]:
        per = personaje(i)
        lista_personajes.append((per["id"], per["name"]))
    episode = Episode(id=respuesta["id"], name=respuesta["name"], air_date=respuesta["air_date"],
                      episode=respuesta["episode"], characters=lista_personajes,
                      url=respuesta["url"], created=respuesta["created"])
    context = {
        'episodio': episode
    }
    return render(request, 'RickyM/Episodio.html', context)




def api_request(url):
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data

def todos_episodios():
    url = urlu + "episode/"
    data = api_request(url)
    data_final = data["results"]
    for i in range(1, data["info"]["pages"]):
        data = api_request(data["info"]["next"])
        data_final = data_final + data["results"]
    return data_final

def episodio(url):
    data = api_request(url)
    return data

def personaje(url):
    data = api_request(url)
    return data

def lugar(url):
    data = api_request(url)
    return data
