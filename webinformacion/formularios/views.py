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
