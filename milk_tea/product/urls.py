from django.urls import path

from .views import getAllProduct, getDMProduct, getDetailProduct


# app_name= 'product'

urlpatterns = [
    path('product', getAllProduct, name = 'allmon'), 
    path('product/<mon_id>/', getDetailProduct, name = 'detailmon'), 

    path('category/<id>', getDMProduct, name = 'DMmon'), 
    
]
