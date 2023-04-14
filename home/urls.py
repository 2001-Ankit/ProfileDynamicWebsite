
from django.urls import path
from .views import *
urlpatterns = [
#path('url_path_name','function_name','internal_redirect')
path('', home, name='home'),
path('about',about,name='about'),
path('contact',contact,name='contact'),
path('services',services,name='services'),
path('price',price,name ='price'),
path('portfolio',portfolio,name='portfolio'),
path('bsingle',bsingle,name='bsingle'),
path('bhome',bhome,name='bhome'),
    path('elements',elements,name="elements")
    ]
