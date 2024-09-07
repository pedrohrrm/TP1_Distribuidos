from django.shortcuts import render
from crud_app.models import Artigo

from django.shortcuts import get_object_or_404
from django.http import FileResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def artigos_list(request):
    template_name = 'listar_artigos' 
    artigos = Artigo.objects.all() 
    context = { 
        'artigos': artigos
        }
    return render(request, 'listar_artigos.html', {'artigos': artigos})

def visualizar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return FileResponse(artigo.arquivo, content_type='application/pdf')