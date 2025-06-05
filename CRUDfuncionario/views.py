from django.shortcuts import render, redirect
from CRUDfuncionario.models import Funcionario
from django.http import HttpResponse
from login.views import login_view, verifica_login
from django.contrib import messages

def Funcionarios(request):
    if verifica_login(request):
        funcionarios = Funcionario.objects.all()
        return render(request, "funcionarios.html", {"funcionarios": funcionarios})
    else:
        return redirect(login_view)
    
def cadastrarFuncionario_view(request):
    if request.method == 'POST':
        if verifica_login(request):
            username = request.POST.get("username")
            try:
                usuarioAux = Funcionario.objects.get(username=username)
                messages.warning(request,"Já existe um funcionário com este username")
                return redirect(cadastrarFuncionario_view)
            except Funcionario.DoesNotExist:
                funcionario = Funcionario(
                    nivelDeAcesso=1,
                    username=request.POST.get("username"),
                    enderecoFuncionario=request.POST.get("enderecoFuncionario"),
                    CPF=request.POST.get("CPF"),
                    CEP=request.POST.get("CEP"),
                    telefone=request.POST.get("telefone"),
                    password=request.POST.get("password"),
                    funcao=request.POST.get("funcao"),
                    email=request.POST.get("email")
                )
                if(funcionario.validar_dados(funcionario) == False):
                    messages.warning(request,"Dados de cadastro incorretos!")
                    return redirect(cadastrarFuncionario_view)
                novo_funcionario = funcionario.criar_usuario(funcionario)
                user = funcionario.autenticar(request,username, funcionario.password)
                if user:
                    return redirect(Funcionarios)
                else:
                    return HttpResponse("Falha na autenticação do usuário")
        else:
            return redirect(login_view)
    else:
        return render(request, "cadastrarFuncionario.html")

def editarFuncionario_view(request, id):
    if verifica_login(request):
        funcionario = usuario_existe(id)
        if(funcionario == None):
            return redirect(Funcionarios)
        return render(request, "updateFuncionario.html", {"funcionario": funcionario})
    else:
        return redirect(login_view)

def updateFuncionario_view(request, id):
    if request.method == 'POST':
        if verifica_login(request):
            funcionario = usuario_existe(id)
            if(funcionario == None):
                messages.warning(request, "Usuario não existe!")
                return redirect('editarFuncionario_view', id=id)
            # Atualiza os campos do funcionário com base nos dados do formulário
            funcionario.username = request.POST.get("username")
            funcionario.enderecoFuncionario = request.POST.get("enderecoFuncionario")
            funcionario.CPF = request.POST.get("CPF")
            funcionario.CEP = request.POST.get("CEP")
            funcionario.telefone = request.POST.get("telefone")
            funcionario.email = request.POST.get("email")
            funcionario.funcao = request.POST.get("funcao")
            if(funcionario.validar_dados(funcionario) == False):
                messages.warning(request,"Dados na edição incorretos!")
                return render(request, "updateFuncionario.html", {"funcionario": funcionario})
            funcionario.save()
            return redirect(Funcionarios)
        else:
            return redirect(login_view)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')

def deleteFuncionario_view(request, id):
    if verifica_login(request):
        funcionario = usuario_existe(id)
        funcionario.delete()
        return redirect(Funcionarios)
    else:
        return redirect(login_view)
    
def usuario_existe(id):
    try:
        funcionario = Funcionario.objects.get(idFuncionario= id)
        return funcionario
    except Funcionario.DoesNotExist:
        return None
