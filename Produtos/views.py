from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from Fornecedores.models import Fornecedor
from django.contrib.auth.decorators import login_required
from login.views import verifica_login, login_view
from Transacao.models import Transacao
from django.contrib import messages

def produtos_view(request):
    if(verifica_login(request)):
        produtos = Produtos.objects.all()
        fornecedores = Fornecedor.objects.all()
        transacoes = Transacao.objects.all()
        return render(request, "produtos.html", {"produtos": produtos, "fornecedores": fornecedores, "transacoes":transacoes})
    else:
        return redirect(login_view)

def cadastrarProdutos_view(request):
    if(verifica_login(request)):
        if request.method == 'POST':
                idFornecedor = request.POST.get("idFornecedor")
                fornecedor = get_object_or_404(Fornecedor, idFornecedor=idFornecedor)
                idTransacao = request.POST.get("idTransacao")
                transacao = get_object_or_404(Transacao, idTransacao=idTransacao)
                produto = Produtos(
                    idFornecedor=fornecedor,
                    idTransacao=transacao,
                    nomeProduto=request.POST.get("nomeProduto"),
                    valorUnit=request.POST.get("valorUnit"),
                    qntEstoque=request.POST.get("qntEstoque"),
                    categoria=request.POST.get("categoria"),
                    subCategoria=request.POST.get("subCategoria"),
                    marcaProduto=request.POST.get("marcaProduto")
                )
                if(produto.validar_dados(produto) == False):
                    messages.warning(request,"Dados de cadastro incorretos!")
                    return redirect(cadastrarProdutos_view)
                produto = Produtos.objects.create(
                    idFornecedor=fornecedor,
                    idTransacao =transacao,
                    nomeProduto=request.POST.get("nomeProduto"),
                    valorUnit=request.POST.get("valorUnit"),
                    qntEstoque=request.POST.get("qntEstoque"),
                    categoria=request.POST.get("categoria"),
                    subCategoria=request.POST.get("subCategoria"),
                    marcaProduto=request.POST.get("marcaProduto")
                )
                produto.save()
                return redirect(produtos_view)
        else:
            fornecedores = Fornecedor.objects.all()
            transacoes = Transacao.objects.all()
            return render(request, "cadastrarProdutos.html", {"fornecedores": fornecedores, "transacoes": transacoes})
    else:
         redirect(login_view)

def editarProdutos_view(request, id):
    if(login_view(request)):
        produto = get_object_or_404(Produtos, idProduto=id)
        fornecedores = Fornecedor.objects.all()
        transacoes = Transacao.objects.all()
        return render(request, "updateProduto.html", {"produto": produto, "fornecedores": fornecedores, "transacoes": transacoes})
    else:
         redirect(login_view)
def updateProdutos_view(request, id):
    if(verifica_login(request)):
        if request.method == 'POST':
            produtos = get_object_or_404(Produtos, idProduto=id)
            idFornecedor = request.POST.get("idFornecedor")
            idTransacao = request.POST.get("idTransacao")
            fornecedor = get_object_or_404(Fornecedor, idFornecedor=idFornecedor)
            transacao = get_object_or_404(Transacao, idTransacao=idTransacao)
            produtos.nomeProduto = request.POST.get("nomeProduto")
            produtos.idFornecedor = fornecedor
            produtos.idTransacao = transacao
            produtos.valorUnit = request.POST.get("valorUnit")
            produtos.qntEstoque = request.POST.get("qntEstoque")
            produtos.categoria = request.POST.get("categoria")
            produtos.subCategoria = request.POST.get("subCategoria")
            produtos.marcaProduto = request.POST.get("marcaProduto")
            if(produtos.validar_dados(produtos) == False):
                messages.warning(request,"Dados de edição incorretos!")
                return redirect(editarProdutos_view)
            produtos.save()
            return redirect(produtos_view)
        else:
            return HttpResponse('Método não permitido')
    else:
         redirect(login_view)

def deleteProduto_view(request, id):
    if(verifica_login(request)):
        produto = get_object_or_404(Produtos, idProduto=id)
        produto.delete()
        return redirect(produtos_view)
    else:
         redirect(login_view)
