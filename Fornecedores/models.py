from django.db import models
from CRUDfuncionario.validators import valida_texto
from django.core.exceptions import ValidationError
# Create your models here.

class Fornecedor(models.Model):
    idFornecedor = models.AutoField(primary_key=True)
    nomeFornecedor = models.CharField(max_length=30, validators = [valida_texto], unique=True)
    endereco = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    cnpj = models.CharField(max_length=14)

    def validar_dados(self,funcionario):
        try:
            funcionario.full_clean()
            return True
        except ValidationError:
            return False