from django.http import HttpResponse
from django.shortcuts import render
from CRUDfuncionario.models import Funcionario
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        funcionario = Funcionario()

        user = funcionario.autenticar(request, username, password)
        if user:
            user = Funcionario.objects.get(username=username)
            criar_sessao(request, user)
            return redirect('telainicial')  # Use redirect para evitar reenvios de formulário
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')
        
def logout_view(request):
    # Verifica se a chave 'userData' existe na sessão antes de acessá-la
    
    if 'user_id' in request.session:
        # Se existir, retorna os dados do usuário
        del request.session['user_id']
        return render(request, 'login.html')
    else:
        return render(request,'login.html')

def criar_sessao(request, user):
    request.session['user_id'] = user.idFuncionario

def verifica_login(request):
    return 'user_id' in request.session

def Perfil_view(request):
    user_id =request.session.get('user_id')
    user = Funcionario.objects.get(idFuncionario=user_id)
    return render(request, 'perfil.html', {"user":user})


def verifica_login(request):
        return 'user_id' in request.session

def atualizar_perfil(request,id):
    if request.method == 'POST':
        if verifica_login(request):
            try:
                funcionario = Funcionario.objects.get(idFuncionario= id)
                funcionario.username = request.POST.get("username")
                funcionario.enderecoFuncionario = request.POST.get("enderecoFuncionario")
                funcionario.CPF = request.POST.get("CPF")
                funcionario.CEP = request.POST.get("CEP")
                funcionario.telefone = request.POST.get("telefone")
                funcionario.email = request.POST.get("email")
                funcionario.funcao = request.POST.get("funcao")
                if(funcionario.validar_dados(funcionario) == False):
                    messages.warning(request,"Dados na edição incorretos!")
                    return redirect(Perfil_view)
                funcionario.save()
                return redirect(Perfil_view)
            except Funcionario.DoesNotExist:
                messages.warning(request, "Usuario não existe!")
                return redirect(Perfil_view)
        else:
            return redirect(login_view)