from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "paginas/index.html")

def ejemplo(request):
    return render(request, "paginas/ejemplo.html")

def saludo(request):
    #Siempre que tengamos un post debemos pregunta rporque no da tiempo a escribir
    if ('cajanombre' in request.POST):
        #Aqui tenemos caja
        dato = request.POST["cajanombre"]
        #Enviamos informacion
        informacion = {
            "nombre":dato
        }
        return render(request, "paginas/saludo.html", informacion)
    else:
        #No enviamos información
        return render(request, "paginas/saludo.html")
    
def sumarnumeros(request):
    if ('cajanum1' in request.POST):
        dato1 = request.POST['cajanum1']
        dato2 = request.POST['cajanum2']
        suma = int(dato1) + int(dato2)
        informacion = {
            "suma":suma
        }
        return render(request, "paginas/sumarnumeros.html", informacion)
    else:
        #No sumamos nada
        return render(request, "paginas/sumarnumeros.html")
    
def Parimpar(request):
    if('cajanum' in request.POST):
        num = request.POST['cajanum']
        resultado = int(num) % 2
        tipo = ""
        if(resultado == 0):
            tipo = "Par"
        else:
            tipo = "Impar"

        informacion = {
            "numero":tipo,
            "datonumero":num
        }
        return render(request, "paginas/parimpar.html",informacion)
    else:
        return render(request, "paginas/parimpar.html")
    
def Collatz(request):
    if('cajanumero' in request.POST):
        #Tenemos datos
        #Devolvemos una lista de numeros
        listanumeros = []
        #Leemos el numero en la caja
        numero = int(request.POST['cajanumero'])
        while(numero != 1):
            if (numero % 2 == 0):
                numero = numero // 2
            else:
                numero = (numero * 3) + 1
            listanumeros.append(numero)
        informacion = {
            "listanumeros":listanumeros
        }
        return render(request, "paginas/collatz.html", informacion)
    else:
        #Sin datos
        return render(request, "paginas/collatz.html")
    
def tablaMultiplicar(request):
    if('cajanumero' in request.POST):
        #Tenemos el dato cogido
        listamultiplicacion = []
        numero = int(request.POST['cajanumero'])
        maximo = int(request.POST['cajamulti'])
        for i in range(maximo):
            i = i + 1
            multi = numero * i
            operacion = f"{numero} * {i}"
            listamultiplicacion.append(
                {
                    "operacion":operacion,
                    "resultado":multi,
                }
            )
        informacion = {
            "listanumeros":listamultiplicacion
        }
        return render(request, "paginas/tablas.html", informacion)
    else:
        return render(request, "paginas/tablas.html")
    
def deportes(request):
    listaDeportes = ["Futbol", "Petanca", "Curling", "Dardos", "Parchis", "Rana", "Voleyball", "Baloncesto"]
    if('selectdeporte' in request.POST):
        deporte = request.POST['selectdeporte']
        informacion = {
            "listadeportes": listaDeportes,
            "deporte": deporte
        }
        return render(request, "paginas/deportes.html", informacion)
    else:
        informacion = {
            "listadeportes": listaDeportes
        }
        return render(request, "paginas/deportes.html", informacion)
    
def colores(request):
    listaColores = [
        {
            "color":"Rojo",
            "valor":"red"
        },
        {
            "color":"Verde",
            "valor":"green"
        },
        {
            "color":"Azul",
            "valor":"blue"
        },
        {
            "color":"Amarillo",
            "valor":"yellow"
        },
        {
            "color":"Morado",
            "valor":"purple"
        },
        {
            "color":"Rosa",
            "valor":"pink"
        },
        {
            "color":"Gris",
            "valor":"grey"
        },
    ]
    if('selectcolor' in request.POST):
        color = request.POST['selectcolor']
        informacion = {
            "listacolores":listaColores,
            "color":color
        }
        return render(request, "paginas/colores.html", informacion)
    else:
        informacion = {
            "listacolores": listaColores
        }
        return render(request, "paginas/colores.html", informacion)
    
def comics(request):
    listaComics = [
        {
            "index": 0,
            "titulo": "Spiderman",
            "imagen": "https://elcoleccionistacomics.com/60266-medium_default/spiderman-de-todd-mcfarlane-vol1-de-6.jpg"
        },
        {
            "index": 1,
            "titulo": "Spawn",
            "imagen": "https://m.media-amazon.com/images/I/91hZO1pjAoL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "index": 2,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 3,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 4,
            "titulo": "Asterix y Obelix",
            "imagen": "https://comicsbarcelona.com/wp-content/uploads/2015/11/127913-Asterix-2.-La-Hoz-de-Oro.jpg"
        } 
    ]
    if ('selectcomic' in request.POST):
        indice = int(request.POST['selectcomic'])
        comic = listaComics[indice]
        informacion = {
            "listacomics":listaComics,
            "comic":comic
        }
        return render(request, "paginas/comics.html", informacion)
    else:
        informacion = {
            "listacomics":listaComics,
        }
        return render(request, "paginas/comics.html", informacion)
