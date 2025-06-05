from django.urls import path
from Produtos.views import produtos_view, editarProdutos_view, deleteProduto_view,cadastrarProdutos_view, updateProdutos_view

urlpatterns = [
    path('',produtos_view, name="produtos_view"),
    path('criaProduto',cadastrarProdutos_view, name="cadastrarProdutos_view"),
    path('editarProdutos/<int:id>',editarProdutos_view, name="editarProdutos_view"),
    path('updateProdutos/<int:id>', updateProdutos_view,name="updateProdutos_view"),
    path('deleteProduto/<int:id>', deleteProduto_view, name="deleteProdutos_view"),
]