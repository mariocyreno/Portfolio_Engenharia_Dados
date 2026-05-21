# Consolidação de Planilhas de Vendas 📊

Este projeto é um script em Python focado em automação de tarefas com arquivos. Ele varre um diretório específico em busca de múltiplas planilhas de Excel (`.xlsx`), junta todos os dados em uma única estrutura usando Pandas e exporta um arquivo consolidado (`Vendas_Totais.xlsx`).

É uma solução ideal para eliminar o trabalho manual de copiar e colar dados de dezenas de planilhas diferentes.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para leitura, concatenação e exportação dos dados.
* **Openpyxl:** Motor (engine) utilizado pelo Pandas para manipular arquivos Excel.
* **Python-dotenv:** Para gerenciar os caminhos das pastas de forma segura e configurável.

## ⚙️ Pré-requisitos

1. Python 3.x instalado.
2. Arquivos de origem no formato `.xlsx` com a mesma estrutura de colunas.

## 🚀 Como instalar e rodar

**1. Clone o repositório ou baixe os arquivos**

**2. Instale as dependências**
Abra o terminal na pasta do projeto e execute:
```bash
pip install -r requirements.txt