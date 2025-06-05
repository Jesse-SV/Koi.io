from django.urls import path
from .views import transacao_view, cadastrarTransacao_view, editarTransacao_view, deletarTransacao_view, updateTransacao_view

urlpatterns = [
    path('', transacao_view, name="transacao_view"),
    path('cadastrarTransacao/', cadastrarTransacao_view, name="cadastrarTransacao_view"),
    path('editarTransacao/<int:id>', editarTransacao_view, name="editarTransacao_view"),
    path('updateTransacao/<int:id>', updateTransacao_view, name="updateTransacao_view"),
    path('deletarTransacao/<int:id>', deletarTransacao_view, name="deletarTransacao_view")
]
