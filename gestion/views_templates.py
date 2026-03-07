import json
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render

from gestion.models import Product, Category

def saludo(request):
    return render(request, 'gestion/index.html')