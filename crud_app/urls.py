from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("listar_artigos/", views.artigos_list , name='artigos_list'),
    path('visualizar/<int:artigo_id>/', views.visualizar_artigo, name='visualizar_artigo'),

]
