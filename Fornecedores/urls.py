from django.urls import path
from Fornecedores.views import fornecedor_view, editarFornecedor_view, deleteFornecedor_view, updateFornecedor_view, cadastrarFornecedor_view

urlpatterns = [
    path('',fornecedor_view, name = "fornecedor_view"),
    path('cadastrarFornecedor', cadastrarFornecedor_view, name="cadastrarFornecedor_view"),
    path('editarFornecedor/<int:id>',editarFornecedor_view, name="editarFornecedor_view"),
    path('updateFornecedor/<int:id>',updateFornecedor_view, name="updateFornecedor_view" ),
    path('deleteFornecedor/<int:id>', deleteFornecedor_view, name="deleteFornecedor_view"),
]