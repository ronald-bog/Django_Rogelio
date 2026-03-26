from django.urls import path

from .views_templates import *

urlpatterns = [
    path('saludo', saludo),
    path('datos', pasarDatos),
    path('motor', demoMotor),
    path('create/', create),

]
