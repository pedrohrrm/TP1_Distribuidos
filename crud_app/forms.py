from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = [    'titulo', 'autores', 'resumo', 'abstract', 
                  'palavras_chave', 'data_ano', 'revista', 'arquivo']
        
        
        
