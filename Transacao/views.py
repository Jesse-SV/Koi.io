from django.shortcuts import render, redirect
from .models import Transacao, Fornecedor
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from login.views import login_view, verifica_login
from django.contrib import messages

def transacao_view(request):
    if verifica_login(request):
        transacoes = Transacao.objects.all()
        fornecedores = Fornecedor.objects.all()
        return render(request, "transacao.html", {"transacoes": transacoes, "fornecedores":fornecedores})
    else:
        return redirect(login_view)

def cadastrarTransacao_view(request):
    if verifica_login(request):
        if request.method == 'POST':
            vDataTransacao = request.POST.get("dataTransacao")
            vTipoTransacao = request.POST.get("tipoTransacao")
            vHoraTransacao = request.POST.get("horaTransacao")
            fornecedor = request.POST.get("idFornecedor")
            transacao = Transacao(dataTransacao=vDataTransacao,idFornecedor = fornecedor, tipoTransacao=vTipoTransacao, horaTransacao=vHoraTransacao)
            if(transacao.validar_dados(transacao) == False):
                messages.warning(request,"Dados de criação incorretos!")
                return redirect(cadastrarTransacao_view)
            transacao.save()
            return redirect(transacao_view)
        else:
            return render(request, "cadastrarTransacao.html")
    else:
        return redirect(login_view)


def editarTransacao_view(request, id):
    if verifica_login(request):
        transacao = Transacao.objects.get(idTransacao=id)
        produtos = transacao.produtos_set.all()
        return render(request, "updateTransacao.html", {"transacao": transacao, "produtos":produtos})
    else:
        return redirect(login_view)

def updateTransacao_view(request, id):
    if verifica_login(request):
        if request.method == 'POST':
            transacao = Transacao.objects.get(idTransacao=id)
            transacao.dataTransacao = request.POST.get("dataTransacao")
            transacao.tipoTransacao = request.POST.get("tipoTransacao")
            transacao.idFornecedor = request.POST.get("idFornecedor")
            transacao.horaTransacao = request.POST.get("horaTransacao")
            if(transacao.validar_dados(transacao) == False):
                messages.warning(request,"Dados de edição incorretos!")
                return redirect('editarTransacao_view', id=id)
            transacao.save()
            return redirect(transacao_view)
        else:
            return redirect(login_view)

def deletarTransacao_view(request, id):
    if verifica_login(request):
        try:
            transacao = Transacao.objects.get(idTransacao=id)
            transacao.delete()
            return redirect(transacao_view)
        except Transacao.DoesNotExist:
            messages.warning(request,"Dados não existentes!")
            return redirect(transacao_view)
    else:
        return redirect(login_view)