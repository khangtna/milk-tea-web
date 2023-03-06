from django.urls import path

from .views import getDonHang


# app_name= 'product'

urlpatterns = [
    path('checkout/', getDonHang, name = 'bill'), 
   
    
    
]
