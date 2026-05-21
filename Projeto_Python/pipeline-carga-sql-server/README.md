# Pipeline de Carga de Dados Relacionais (SQL Server) 🗄️

Este projeto consiste em um script automatizado em Python para carga e ingestão de dados em lote (Batch Ingestion) para um banco de dados relacional SQL Server. Ele extrai informações de múltiplas fontes locais (arquivos Excel e CSV), aplica regras de limpeza e conversão de tipos com Pandas, realiza o esvaziamento seguro das tabelas de destino para evitar duplicidade e popula o banco de dados.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para leitura de múltiplos formatos de arquivos (`.csv` e `.xlsx`) e conversão de tipos de dados.
* **PyODBC:** Para conexão robusta e execução de comandos SQL no SQL Server.
* **Openpyxl:** Engine para tratamento de arquivos Excel dentro do Pandas.
* **Python-dotenv:** Para gerenciamento seguro das strings de conexão e caminhos dos arquivos.

## 📐 Estrutura de Tabelas Alimentadas

O script simula um ambiente de vendas/e-commerce alimentando as seguintes tabelas de forma relacional:
* **PRODUTOS:** Informações cadastrais e preços de produtos.
* **CATEGORIA:** Segmentação dos produtos.
* **ITENS:** Itens pertencentes a cada pedido efetuado.
* **ORDENS:** Cabeçalho dos pedidos contendo datas e status.
* **CLIENTES:** Dados cadastrais, demográficos e de contato dos clientes.

## 🚀 Como instalar e rodar

**1. Instale as dependências**
Abra o terminal na pasta deste projeto e execute:
```bash
pip install -r requirements.txt