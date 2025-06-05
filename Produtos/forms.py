from django import forms
from .models import Produtos, Fornecedor  # Importe o modelo associado

class criaProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nomeProduto','idFornecedor', 'valorUnit', 'qntEstoque', 'categoria', 'subCategoria', 'marcaProduto']
