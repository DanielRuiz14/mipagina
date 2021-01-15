from django.shortcuts import render

# Create your views here.

def inicio(request):
    return HttpResponse("Prueba de funcionamiento. Hola Fran")