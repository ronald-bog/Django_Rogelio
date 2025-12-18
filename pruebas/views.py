from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse('!!! Nuestra primera aplicacion con Django !!!')

def saludarApp(request):
    return HttpResponse('!!! Desde una ruta propia de la APP - pruebas !!!')

def saludarApp2(request):
    return HttpResponse('!!! Desde una ruta propia de la APP - pruebas 2 !!!')

def saludarApp3(request):
    return HttpResponse('!!! Desde una ruta propia de la APP - pruebas 3 !!!')

def saludarApp4(request):
    return HttpResponse('!!! Desde una ruta propia de la APP - pruebas 4 !!!')

def saludarApp5(request):
    return HttpResponse('!!! Desde una ruta propia de la APP - pruebas 5 !!!')

def sumar(request):
    n1 = 10
    n2 = 15
    return HttpResponse(n1 + n2)

def multiplicar(request, n1, n2, numero3):
    resultado = n1 * n2 * numero3
    return HttpResponse(f'El resultado de la mutiplicacion es: {resultado}')

def sumaqp(request):
    # Obtenemos los parametros de la url /?x=70&z=5
    xx = request.GET.get('x', 0)
    zz = request.GET.get('z', 0)

    #convertir a enteros
    x1 = int(xx)
    z1 = int(zz)

    result = x1 + z1
    return HttpResponse(f'La suma de los query params es: {result}')


def notFound(request):
    return HttpResponse('*** LA RUTA NO EXISTE ***')