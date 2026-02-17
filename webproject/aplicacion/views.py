from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Las vistas con los dibujos en web que haremos con nuestro código
#Creamos métodos para dibujar las vistas
def index(request):
    return render(request, "paginas/index.html")

def prueba(request):
    return render(request, "paginas/prueba.html")
