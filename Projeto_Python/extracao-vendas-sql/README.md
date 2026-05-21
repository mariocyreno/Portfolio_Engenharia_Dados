# Extração de Relatório de Vendas (SQL Server) 📈

Este projeto contém um script em Python focado em extração de dados. Ele estabelece uma conexão segura com um banco de dados SQL Server e executa uma query SQL avançada (utilizando múltiplos relacionamentos com `LEFT JOIN`) para consolidar informações de Vendas, Produtos, Categorias e Clientes em uma única visualização estruturada.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para recebimento e visualização dos dados via `pd.read_sql`.
* **PyODBC:** Para estabelecer a conexão com o Microsoft SQL Server.
* **Python-dotenv:** Para leitura segura das credenciais do banco.

## 🚀 Como instalar e rodar

**1. Instale as dependências**
```bash
pip install -r requirements.txt