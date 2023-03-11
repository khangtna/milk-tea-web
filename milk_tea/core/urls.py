from django.urls import path


from .views import Index, search


urlpatterns = [
    path('', Index.as_view(), name = 'index'), 
    path('search/', search, name='search'),
    
] 
