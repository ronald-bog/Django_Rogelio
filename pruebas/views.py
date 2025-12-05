from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse('!!! Nuestra primera aplicacion con Django !!!')

def sumar(request):
    n1 = 10
    n2 = 15
    return HttpResponse(n1 + n2)

def notFound(request):
    return HttpResponse('*** LA RUTA NO EXISTE ***')