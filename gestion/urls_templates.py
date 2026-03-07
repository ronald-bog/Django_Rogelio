from django.urls import path

from .views_templates import *

urlpatterns = [
    path('saludo', saludo)

]