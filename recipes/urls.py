from django.urls import path, include
from recipes.views import home
# from views import index, sobre, contato

urlpatterns = [
    path('', home, name='home'),

]
