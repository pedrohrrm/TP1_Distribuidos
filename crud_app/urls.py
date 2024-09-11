from django.urls import path
from . import views

urlpatterns = [
    path("", views.artigos_list , name='artigos_list'),
    path('visualizar/<int:artigo_id>/', views.visualizar_artigo, name='visualizar_artigo'),
    path('artigo_create', views.artigo_create, name='artigo_create'),
    path('artigo_detalhe/<int:id>', views.artigo_detalhes, name='artigo_detalhe'),
    path('artigo_update/<int:id>', views.artigo_update, name='artigo_update'),
    path('artigo_delete/<int:id>', views.artigo_delete, name='artigo_delete'),
    path('buscar/', views.buscar_artigo, name='buscar_artigo'), 
    

    ]
