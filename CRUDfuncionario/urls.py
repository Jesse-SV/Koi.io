from django.contrib import admin
from django.urls import path
from .views import Funcionarios, editarFuncionario_view, updateFuncionario_view, deleteFuncionario_view, cadastrarFuncionario_view

urlpatterns = [
    path('', Funcionarios, name="funcionario"),
    path('cadastrar/', cadastrarFuncionario_view, name="cadastrarFuncionario_view"),
    path('editar/<int:id>/', editarFuncionario_view, name="editarFuncionario_view"),
    path('update/<int:id>/', updateFuncionario_view, name="updateFuncionario_view"),
    path('delete/<int:id>/', deleteFuncionario_view, name="deleteFuncionario_view"),
]
    