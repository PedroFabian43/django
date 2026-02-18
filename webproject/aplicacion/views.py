from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Las vistas con los dibujos en web que haremos con nuestro código
#Creamos métodos para dibujar las vistas
def index(request):
    return render(request, "paginas/index.html")

def prueba(request):
    return render(request, "paginas/prueba.html")

def monstruos(request):
    return render(request, "paginas/monstruos.html")

def futbol(request):
    informacion = {
        "equipo": "Real Sociedad"
    }
    return render(request, "paginas/futbol.html", informacion)

def nombres(request):
    listanombres = ["Adrian", "Lucía", "Aitana", "Juan", "Paco"]
    #En este mismo ejemplo me gustaria enviar el nombre y la edad
    listapersonas = [
        {
            "nombre": "Adrian",
            "edad": 26
        },
        {
            "nombre": "Lucia",
            "edad": 23
        },
        {
            "nombre": "Paco",
            "edad": 50
        },
    ]
    #La informacion la debemos enviar mediante diccionarios
    informacion = {
        "listanombres":listanombres,
        "listapersonas":listapersonas
    }
    return render(request, "paginas/nombres.html", informacion)

def mascota(request):
    listamascotas = [
        {
            "nombre": "Pepito",
            "raza": "Perro",
            "edad": "7"
        },
        {
            "nombre": "Coco",
            "raza": "Perro",
            "edad": "2"
        },
        {
            "nombre": "Lola",
            "raza": "Agaporni",
            "edad": "6"
        },
        {
            "nombre": "Cuqui",
            "raza": "Tortuga",
            "edad": "15"
        }
    ]
    #Guardamos la info en un diccionario a enviar
    informacion = {
        "listamascotas":listamascotas
    }
    return render(request, "paginas/mascotas.html", informacion)

def colores(request):
    #Hay que comprobar si recibimos algo o no
    if('micolor' in request.GET):
        #La informacion viene mediante GET en la URL
        colorRecibido = request.GET["micolor"]
    else:
        colorRecibido = "Negro como tu alma"
    #Ya tenemos un color y que hacemos con él?
    #Devolvemos el color para dibujarlo
    informacion = {
        "color": colorRecibido
    }
    return render(request, "paginas/colores.html", informacion)