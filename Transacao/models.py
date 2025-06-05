from django.db import models
from django.core.exceptions import ValidationError
from Fornecedores.models import Fornecedor
from .validators import validate_data_nao_futura
# Create your models here.

class Transacao(models.Model):
    idTransacao = models.AutoField(primary_key=True)
    idFornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE, default=1)
    dataTransacao = models.DateField(validators=[validate_data_nao_futura])
    horaTransacao = models.TimeField(default="00:01:02")
    tipoTransacao = models.CharField(max_length=7)

    def validar_dados(self,produto):
      try:
         produto.full_clean()
         return True
      except ValidationError:
         return False
      
    def calcular_valorTotal_transacao(produtos):
      valorTotal = 0
      for produto in produtos:
          valorTotal += produto.valorUnit
      return valorTotal

    