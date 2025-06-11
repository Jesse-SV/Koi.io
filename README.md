# 🐟 Koi.io

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Rodolfoovo/projetoIntegrador)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/framework-Django-092E20?logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/database-SQLite-lightgrey)](https://www.sqlite.org/)
[![Bootstrap 5](https://img.shields.io/badge/frontend-Bootstrap%205-purple)](https://getbootstrap.com/)
[![Plotly Dash](https://img.shields.io/badge/visualization-Plotly%20Dash-orange)](https://dash.plotly.com/)

> Um painel de controle sofisticado para gestão de estoque e visualização de dados empresariais.

---

## 📊 Visão Geral

**Koi.io** é um sistema web de controle de inventário que oferece visualização intuitiva de dados via dashboards e gráficos. Ele facilita a gestão de entrada e saída de produtos, além do monitoramento de fornecedores.

## 👥 Equipe

- Daniel Andrade de Souza  
- Jessé Santana Veloso  
- Victor Cauã da Silva Aguiar

## ✨ Funcionalidades

- 📈 Dashboards dinâmicos e gráficos
- 📦 Gestão de estoque com histórico
- 👥 Gerenciamento de usuários com permissões
- 📋 Relatórios e indicadores operacionais
- 🔎 Filtros e segmentações por tipo, fornecedor, data etc.
- 🧾 Cadastro e edição de produtos, fornecedores e transações

## 💻 Tecnologias

- **Backend:** Django 4.x (Python 3.12+)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Gráficos:** Plotly Dash
- **Banco de Dados:** SQLite
- **Bibliotecas:** Pandas

## ⚙️ Requisitos

- Python 3.12+
- Pip
- Git

## 🚀 Instalação

```bash
git clone https://github.com/Rodolfoovo/projetoIntegrador.git
cd projetoIntegrador

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```
Documentação: https://docs.google.com/document/d/18vrYpGEQqibemTo2g1HQj2KqEpbsIBHvCTMD2dfdRDk/edit?usp=sharing
