from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("lista_artigos/", views.artigos_list , name='artigos_list')
]
