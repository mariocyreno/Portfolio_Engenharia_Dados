Criando uma pagina para publicar os projetos pythons# 🐍 Portfólio Python: Engenharia de Dados e Automação

Bem-vindo ao meu diretório central de projetos em Python! 

O objetivo desta pasta é demonstrar minha capacidade de resolver problemas reais de negócios utilizando programação. Os scripts aqui presentes focam em **Engenharia de Dados (ETL/Pipelines)**, **Automação de Processos (RPA)** e **Análise de Dados**.

## 📂 Projetos Incluídos

Abaixo você encontra a lista de projetos isolados. Clique na pasta de cada um para ler a documentação completa e ver o código-fonte.

| Projeto | Resumo do que faz | Principais Tecnologias |
| :--- | :--- | :--- |
| **[`carga-dados-relacionais`](./carga-dados-relacionais/)** | Pipeline completo de ingestão em lote (Batch) de múltiplos arquivos para um banco relacional. | `pandas`, `pyodbc`, `SQL Server` |
| **[`etl-clientes-sql-server`](./etl-clientes-sql-server/)** | Script de ETL agendado para leitura de CSV, limpeza e carga contínua no banco de dados. | `pandas`, `pyodbc`, `schedule` |
| **[`extracao-vendas-sql`](./extracao-vendas-sql/)** | Script para conexão e extração de relatório consolidado via query SQL com múltiplos JOINs. | `pandas`, `pyodbc`, `SQL Server` |
| **[`automacao-google-forms`](./automacao-google-forms/)** | Robô de RPA web que lê uma base de dados local e preenche formulários sequencialmente. | `selenium`, `pandas` |
| **[`consolidacao-vendas-excel`](./consolidacao-vendas-excel/)** | Automação de arquivos para unificar múltiplas planilhas do Excel em um relatório único. | `pandas`, `openpyxl`, `os` |
| **[`tratamento-dados-clientes`](./tratamento-dados-clientes/)** | Script de Data Wrangling para tratamento de nulos, feature engineering e formatação de datas. | `pandas`, `datetime` |

## ⚙️ Padrão de Desenvolvimento
Todos os projetos desta pasta seguem boas práticas de desenvolvimento, incluindo:
* Gerenciamento seguro de credenciais utilizando variáveis de ambiente (`.env` / `python-dotenv`).
* Gerenciamento de dependências via `requirements.txt`.
* Documentação individualizada.