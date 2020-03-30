from django.urls import path
from .views import registro
from .views import post

app_name = 'Registro'

urlpatterns = [
    path('registro',post,name = 'registro' ),
]














#AGREGAR AL DE GRIMALDO