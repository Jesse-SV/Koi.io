from django.shortcuts import render, redirect
from login.views import login_view, verifica_login
from Produtos.models import Produtos
import time
def tela_inicial(request):
    if(verifica_login(request)):
        estoqueTotal = Produtos.calcular_estoque_total()
        valorEstoqueTotal = Produtos.calcular_valorEstoque_total()
        entradaProdutosMensal = Produtos.entrada_produtos_mensal()
        saidaProdutosMensal = Produtos.saida_produtos_mensal()
        return render(request, 'telainicial.html',{"estoqueTotal": estoqueTotal,
                                                    "valorEstoqueTotal": valorEstoqueTotal,
                                                    "EntradaProdutosMensal": entradaProdutosMensal,
                                                    "SaidaProdutosMensal":saidaProdutosMensal})
    else:
        return redirect(login_view)
