from django.db import models
from datetime import date, timedelta, datetime
from Fornecedores.models import Fornecedor
from django.core.exceptions import ValidationError
from Transacao.models import Transacao
import calendar
# Create your models here.

class Produtos(models.Model):
   idProduto = models.AutoField(primary_key=True)
   idFornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
   idTransacao = models.ForeignKey(Transacao,on_delete=models.CASCADE, default=1)
   nomeProduto=models.CharField(max_length= 30)
   valorUnit= models.DecimalField(max_digits=10,decimal_places=2)
   qntEstoque =models.IntegerField(default = 1)
   categoria = models.CharField(max_length=15)
   subCategoria=models.CharField(max_length=15)
   marcaProduto=models.CharField(max_length=15)

   def validar_dados(self,produto):
      try:
         produto.full_clean()
         return True
      except ValidationError:
         return False
   
   def calcular_estoque_total():
      produtos = Produtos.objects.all()
      total_estoque = 0
      for produto in produtos:
         transacao = Transacao.objects.get(idTransacao=produto.idTransacao.idTransacao)
         if(transacao.tipoTransacao == "ENTRADA"):
            total_estoque += produto.qntEstoque
         else:
            total_estoque -= produto.qntEstoque
         
      return total_estoque
   def calcular_valorEstoque_total():
      # Obtém todos os produtos da tabela
      produtos = Produtos.objects.all()

      # Inicializa o estoque total como zero
      estoque_total = 0
      hoje = date.today()
      inicio = date(hoje.year, hoje.month, 1)  # Data de início do período
      fim = date(hoje.year, hoje.month, calendar.monthrange(hoje.year, hoje.month)[1]) # Data de fim do período
      # Itera sobre cada produto e adiciona sua quantidade de estoque ao total
      for produto in produtos:
         estoque_total += produto.qntEstoque*produto.valorUnit
      return estoque_total

   def entrada_produtos_mensal():
    estoque_total = 0
    hoje = date.today()
    inicio = date(hoje.year, hoje.month, 1)  # Data de início do período
    produtos = Produtos.objects.all()
    fim = date(hoje.year, hoje.month, calendar.monthrange(hoje.year, hoje.month)[1])  # Corrigido aqui

    for produto in produtos:
        try:
            transacao = Transacao.objects.get(idTransacao=produto.idTransacao.idTransacao, dataTransacao__range=(inicio, fim))
            if transacao.tipoTransacao == "ENTRADA":
                estoque_total += produto.qntEstoque * produto.valorUnit
        except Transacao.DoesNotExist:
            continue

    return estoque_total

   def saida_produtos_mensal():
      estoque_total = 0
      hoje = date.today()
      produtos = Produtos.objects.all()
      inicio = date(hoje.year, hoje.month, 1)  # Data de início do período
      fim = date(hoje.year, hoje.month, calendar.monthrange(hoje.year, hoje.month)[1])
      for produto in produtos:
         try:
            transacao = Transacao.objects.get(idTransacao=produto.idTransacao.idTransacao, 
                                          dataTransacao__range=(inicio, fim))
            if(transacao.tipoTransacao == "SAIDA"):
               estoque_total += produto.qntEstoque*produto.valorUnit
         except Transacao.DoesNotExist:
            continue
      
      return estoque_total
