
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('saludo/', views.saludar),
    #path('suma/', views.sumar),
    #path('multi/<int:n1>/<int:n2>/<int:numero3>/', views.multiplicar),
    #path('sumaqp/', views.sumaqp),
    path('', include('pruebas.urls')), # el argumento del include se pasa como un string ('').
    path('api/', include('gestion.urls'))
    # path('', include('usuarios.urls')),
    # path('', include('productos.urls')),
    # path('', include('categorias.urls')),
    #re_path(r'^.*$', views.notFound) #Para manejo de rutas no existentes
]


