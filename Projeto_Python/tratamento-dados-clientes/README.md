# Tratamento e Limpeza de Dados de Clientes 🧹

Este projeto consiste em um script Python focado em manipulação e limpeza de dados (Data Wrangling) utilizando a biblioteca Pandas. Ele lê uma base de clientes bruta em formato CSV e aplica uma série de transformações para padronizar as informações.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para manipulação de DataFrames, tratamento de nulos e formatação de dados.
* **Python-dotenv:** Para carregamento seguro do caminho do arquivo de origem.

## 📊 Transformações Realizadas

O script executa as seguintes etapas de limpeza:
1. **Tratamento de Nulos (Missing Values):** Preenchimento de campos vazios com valores padrão (ex: "Não Informado").
2. **Engenharia de Recursos (Feature Engineering):** Criação da coluna `Nome Completo` a partir do primeiro e último nome, e adição de uma coluna padrão de `País`.
3. **Manipulação de Datas:** Conversão de strings para formato datetime, separando a data de criação e o horário de compra em colunas distintas.
4. **Padronização:** Seleção, reordenação e renomeação das colunas do inglês para o português, facilitando a leitura por usuários de negócio.

## 🚀 Como rodar

**1. Instale as dependências**
```bash
pip install -r requirements.txt