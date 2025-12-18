from django.urls import path, re_path

from . import views

urlpatterns = [
    path('salud/', views.saludarApp),
    path('saludo2/', views.saludarApp2),
    path('saludo3/', views.saludarApp3),
    path('saludo4/', views.saludarApp4),
    path('saludo5/', views.saludarApp5),

]