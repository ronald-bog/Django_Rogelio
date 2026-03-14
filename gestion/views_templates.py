import json
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

    # if request.method == 'POST':
    #     nombre = request.POST
    #     print(nombre['opciones'])

    return render(request,'gestion/index.html', datos)