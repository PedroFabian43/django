# Estos son las rutas del servidor https://paco
from django.urls import path
# Estos son los métodos que tenemos el views.py
from aplicacion import views

# Aquí creamos las ruta smediante algo llamado url patterns
# Aquí ponemos las url de cada url del webproject
urlpatterns = [
    path('', views.index, name="index"), #http://127.0.0.1:8000/aplicacion/
    path('prueba/', views.prueba, name="prueba"), #http://127.0.0.1:8000/aplicacion/prueba/
    path('noticias/', views.monstruos, name='monstruos'), #http://127.0.0.1:8000/aplicacion/noticias/
    path("futbol/", views.futbol, name="futbol"),
    path("nombres/", views.nombres, name="nombres"),
    path("animales/", views.mascota, name="mascota"),
    path("colores/", views.colores, name="colores"),
]