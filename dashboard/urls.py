from django.urls import path
from .views import tela_inicial
from login.views import logout_view, Perfil_view
from CRUDfuncionario.views import Funcionarios
from Produtos.views import produtos_view
from Fornecedores.views import fornecedor_view

urlpatterns = [
    path('', tela_inicial, name='telainicial'),
    path('logout/', logout_view, name='logout'),
    path('funcionarios/', Funcionarios, name='funcionarios'),
    path('produtos/', produtos_view, name='produtos'),
    path('fornecedor/', fornecedor_view, name='fornecedor'),
    path('EditarPerfil/', Perfil_view, name='perfil'),
]
