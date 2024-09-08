from django.shortcuts import render
from crud_app.models import Artigo

from django.shortcuts import get_object_or_404
from django.http import FileResponse

from django.urls import reverse
from django.http import HttpResponseRedirect
from crud_app.forms import ArtigoForm
from django.contrib import messages
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

def artigo_create(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
    
            messages.success(request, 'O artigo foi enviado com sucesso.')
            return HttpResponseRedirect(reverse('artigos_list'))
    form = ArtigoForm()
    return render(request, 'artigo_create.html', {"form": form})

def artigo_detalhes(request, id):
    template_name = 'artigo_detalhe.html' 
    artigo = Artigo.objects.get(id=id)
    artigo = get_object_or_404(Artigo, id=id)  
    context = { 
        'artigo': artigo,
        'url_visualizar': reverse('visualizar_artigo', args=[artigo.id])  

        }
    return render(request, template_name, context) 
    
def artigo_update(request, id):
    artigo = get_object_or_404(Artigo, id=id) 
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo) 
    if form.is_valid(): 
        form.save() 
        
        messages.success(request, 'O artigo foi atualizado com sucesso') 
        return HttpResponseRedirect(reverse('artigo_detalhe', args=[artigo.id])) 
         
    return render(request, 'artigo_create.html', {"form": form}) 

def artigo_delete(request, id):
    artigo = Artigo.objects.get(id=id)
    if request.method == 'POST':
        artigo.delete() 
        messages.success(request, 'O artigo foi deletado com sucesso') 
        return HttpResponseRedirect(reverse('artigos_list')) 
    return render(request, 'artigo_delete.html')