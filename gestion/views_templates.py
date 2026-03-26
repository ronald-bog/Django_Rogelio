import json
from os import name

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render

from gestion.models import Product, Category


def saludo(request):
    return render(request, 'gestion/index.html')


def pasarDatos(request):
    datos = {
        'estudiante': 'www'
    }

    return render(request, 'gestion/index.html', datos)


def create(request):
    if request.method == 'POST':
        data = request.POST

        category = get_object_or_404(Category, id=data.get('opciones'))

        product = Product.objects.create(
            name=data.get('nombre'),
            price=data.get('precio'),
            stock=data.get('stock'),
            active='activo' in request.POST,
            category=category
        )

    return render(request, 'gestion/index.html')


def demoMotor(request):
    data = {
        'activo': False,
        'nombres': ['Sofia', 'Rogelio', 'Carlos', 'Ana', 'Oscar', 'Vicente', 'Michael', 'Steve']
    }
    return render(request, 'gestion/motor.html', data)
