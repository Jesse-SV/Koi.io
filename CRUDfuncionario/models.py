from typing import Any
from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.contrib.auth import authenticate
from .validators import valida_texto, valida_cpf
from django.core.exceptions import ValidationError
from django.http import HttpResponse
# Create your models here.
class Funcionario(AbstractUser):
    idFuncionario = models.AutoField(primary_key=True)
    nivelDeAcesso = models.IntegerField(default=1)
    enderecoFuncionario = models.CharField(max_length=30)
    CPF = CPFField('CPF',default='000.000.000-0',validators=[valida_cpf])
    CEP = models.CharField(max_length=8)
    telefone = models.CharField(max_length=20)
    funcao = models.CharField(max_length=30)
    username = models.CharField(max_length=30,default='default_username', unique=True,
                                validators=[valida_texto])
    password = models.CharField(max_length=100, default='default_password')
    email = models.EmailField(unique=True, default='daniel@gmail.com', 
                              validators = [EmailValidator(message="Insira um endereco de email valído")])
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def __str__(self):
        return f"Funcionario: {self.username}"

    def autenticar(self,request,username,password):
        return authenticate(request,username= username, password=password)
    
    def criar_usuario(self,user):
        return Funcionario.objects.create_user(
            nivelDeAcesso=1,
            username=user.username,
            enderecoFuncionario=user.enderecoFuncionario,
            CPF=user.CPF,
            CEP=user.CEP,
            telefone=user.telefone,
            password=user.password,
            funcao=user.funcao,
            email=user.email
        )
    
    def validar_dados(self,funcionario):
        try:
            funcionario.full_clean()
            return True
        except ValidationError:
            return False