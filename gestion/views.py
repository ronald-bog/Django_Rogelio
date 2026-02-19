from os import name

import json
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from gestion.models import Product, Category


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    data = []
    for prod in products:
        data.append(
            {
            'id':prod.id,
            'name':prod.name,
            'price':prod.price,
            'stock':prod.stock,
            'active':prod.active,
            'created_at':prod.created_at,
        }
        )
    return JsonResponse(data, safe=False)


# CREAR PRODUCTO (POST)

@csrf_exempt
def product_create(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Metodo no es valido'})

    # Aqui convertimos el json de la peticion en un dict
    body = json.loads(request.body)

    # Validamos si la categoria que viene en el json es correcta
    category = get_object_or_404(Category,  id=body['category_id'])

    product = Product.objects.create(
        name = body['name'],
        price = body['price'],
        stock = body['stock'],
        active = body['active'], ### body.get('active', 1 )
        #created_at = body['created_at'],
        category = category
    )
    return JsonResponse(
        {'message': 'Producto se creo exitosamente', 'id': product.id}, status=201
    )

# name, precio, stock, active 0, created_at, category_id

# ACTUALIZACION PARCIAL (PATCH)

@csrf_exempt
def product_update_patch(request, id):
    if request.method != 'PATCH':
        return JsonResponse({'error': 'Metodo no es valido'})

    product = get_object_or_404(Product, pk=id)

    body = json.loads(request.body)

    product.name = body.get('name', product.name)
    product.price = body.get('price', product.price)
    product.stock = body.get('stock', product.stock)
    product.active = body.get('active', product.active)

    if 'category_id' in body:
        product.category = get_object_or_404(Category,  id=body['category_id'])

    product.save()

    return JsonResponse({'message': 'Producto actualizado exitosamente'})


# ELIMINAR PRODUCTO (DELETE)
@csrf_exempt
def deleteProduct(request, id):
    # validacion del metodo usado en la peticion
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Metodo no es valido'})

    product = get_object_or_404(Product, pk=id) # aqui se obtiene el producto, mas no se borra aun

    product.delete() # aqui se borra el producto

    return JsonResponse({'mensaje': 'Producto eliminado con exito'}) # se envia la respuesta al cliente (usuario) o a quien hizo la peticion







