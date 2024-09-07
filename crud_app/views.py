from django.shortcuts import render
from crud_app.models import Artigo
# Create your views here.

def index(request):
    return render(request, 'index.html')

def artigos_list(request):
    template_name = 'listar_artigos' 
    artigos = Artigo.objects.all() 
    context = { 
        'artigos': artigos
        }
    return render(request, template_name, context) 