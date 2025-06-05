from .models import Fornecedor
from django import forms



class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nomeFornecedor','endereco','telefone','cep','cnpj']