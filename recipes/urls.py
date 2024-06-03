from django.urls import path, include
from recipes.views import index, sobre, contato
# from views import index, sobre, contato

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato')
]
