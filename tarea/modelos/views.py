from django.shortcuts import render
from django.http import HttpResponse
from .models import Jugadores, Tecnicos, Clubes


def create_jugador(request):
    new_jugador= Jugadores.objects.create(name= "Juan Riquelme", price = 20)
    print(new_jugador)
    return HttpResponse("Se creo Jugador")

def list_jugadores(request):
    all_jugadores= Jugadores.objects.all()
    context= {
        "jugadores" : all_jugadores
         }
    return render(request, "list_jugadores.html", context=context)




def create_club(request):
    new_club= Clubes.objects.create(name= "River" , country = "Argentina")
    print(new_club)
    return HttpResponse("Se creo el nuevo club")

def list_clubes(request):
    all_clubes= Clubes.objects.all()
    context= {
        "clubes" : all_clubes
         }
    return render(request, "list_clubes.html", context=context)





def create_tecnico(request):
    new_tecnico= Tecnicos.objects.create(name= "Gallardo" , edad = 45)
    print(new_tecnico)
    return HttpResponse("Se creo el nuevo tecnico")

def list_tecnicos(request):
    all_tecnicos= Tecnicos.objects.all()
    context= {
        "tecnicos" : all_tecnicos
         }
    return render(request, "list_tecnicos.html", context=context)
