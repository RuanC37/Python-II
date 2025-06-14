from django.urls import path
from .views import index, churrasco
urlpatterns = [
    path('', index, name='index'),
    path('churrasco', churrasco, name='churrasco')    
]