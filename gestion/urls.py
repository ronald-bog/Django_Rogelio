from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('creacion/', views.product_create),
    path('patch/<int:id>', views.product_update_patch),
    path('borrar/<int:id>', views.deleteProduct)
]