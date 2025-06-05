import csv
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "koiProject.settings")
django.setup()
import csv
from Produtos.models import Produtos

def importar_csv(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'r',encoding='latin-1') as produtos:
        leitor_csv = csv.DictReader(produtos)
        for linha in leitor_csv:
            Produtos.objects.create(
                nomeProduto=linha['nomeProduto'],
                valorUnit=float(linha['valorUnit']),
                qntEstoque=int(linha['qntEstoque']),
                categoria = linha['categoria'],
                subCategoria=linha['subCategoria'],
                marcaProduto=linha['marcaProduto']
                # Adicione outros campos conforme necessário
            )

if __name__ == "__main__":
    caminho_do_arquivo_csv = 'C:\\Users\\Usuario\\Documents\\Arquivos\\produtos.csv'
    importar_csv(caminho_do_arquivo_csv)