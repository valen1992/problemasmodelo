"""tarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from modelos.views import create_club, create_jugador, create_tecnico, list_jugadores, list_clubes, list_tecnicos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-jugador/', create_jugador),
    path('list-jugadores/', list_jugadores),
    path('create-club/', create_club),
    path('list-clubes/', list_clubes),
    path('create-tecnico/', create_tecnico),
    path('list-tecnicos/', list_tecnicos),
]

