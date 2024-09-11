from django.shortcuts import render
from crud_app.models import Artigo

from django.shortcuts import get_object_or_404
from django.http import FileResponse

from django.db.models import Q

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

from django.shortcuts import render
from django.db.models import Q
from .models import Artigo

def buscar_artigo(request):
    campo_busca = request.GET.get('campo')
    termo_busca = request.GET.get('q')
    ano_publicacao = request.GET.get('ano')

    # Se nenhum termo de busca ou ano for fornecido, mostrar todos os artigos
    if not termo_busca and not ano_publicacao:
        artigos = Artigo.objects.all()
    else:
        # Inicializa a queryset com uma consulta vazia
        query = Q()

        # Adiciona filtros à query com base no campo de busca e termo de busca
        if termo_busca:
            if campo_busca == 'titulo':
                query &= Q(titulo__icontains=termo_busca)
            elif campo_busca == 'autores':
                query &= Q(autores__icontains=termo_busca)
            elif campo_busca == 'palavras_chave':
                query &= Q(palavras_chave__icontains=termo_busca)
            elif campo_busca == 'revista':
                query &= Q(revista__icontains=termo_busca)
            else:  # Busca em todos os campos se nenhum campo específico for selecionado
                query &= (
                    Q(titulo__icontains=termo_busca) |
                    Q(autores__icontains=termo_busca) |
                    Q(palavras_chave__icontains=termo_busca) |
                    Q(revista__icontains=termo_busca)
                )

        # Aplica o filtro por ano de publicação, se fornecido
        if ano_publicacao:
            query &= Q(data_ano=ano_publicacao)

        # Filtra os artigos com base na query construída
        artigos = Artigo.objects.filter(query)

    return render(request, 'buscar_artigo.html', {'artigos': artigos})