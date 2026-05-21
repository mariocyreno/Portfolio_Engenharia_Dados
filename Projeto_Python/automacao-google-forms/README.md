# ETL de Clientes: CSV para SQL Server

Este projeto é um script automatizado de ETL desenvolvido em Python. Ele extrai dados de clientes de um arquivo CSV, realiza tratamentos e limpezas (substituição de valores nulos, conversão de datas e formatação de strings) e carrega os dados em um banco de dados SQL Server. 

O script foi configurado para rodar de forma contínua em segundo plano, atualizando o banco de dados em intervalos programados.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para manipulação e tratamento dos dados.
* **PyODBC:** Para conexão e execução de comandos no SQL Server.
* **Schedule:** Para agendamento da execução do script.
* **Python-dotenv:** Para gerenciamento seguro de credenciais via variáveis de ambiente.

## ⚙️ Pré-requisitos

Antes de rodar o projeto, você precisará ter instalado na sua máquina:
1. Python 3.x
2. [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server) (Necessário para o `pyodbc` funcionar corretamente).

## 🚀 Como instalar e rodar

**1. Clone o repositório ou baixe os arquivos**

**2. Instale as dependências**
Abra o terminal na pasta do projeto e execute:
```bash
pip install -r requirements.txt
