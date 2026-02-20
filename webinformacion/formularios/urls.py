#Con esto traemos la posibilidad de hacer urls
from django.urls import path

#Traemos las vistas para trabajar con ellas
from formularios import views


urlpatterns = [
    path('', views.index, name="index"),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('saludo/', views.saludo, name='saludo'),
    path('sumar/', views.sumarnumeros, name='sumar'),
    path('parimpar/', views.Parimpar, name='parimpar'),
    path('collatz/', views.Collatz, name='collatz'),
    path('tabla/', views.tablaMultiplicar, name='tabla'),
    path('deportes/', views.deportes, name="deporte"),
    path('colores/', views.colores, name="color"),
    path('comics/', views.comics, name='comic'),
]