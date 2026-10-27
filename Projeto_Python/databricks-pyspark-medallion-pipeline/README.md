# Pipeline de Dados com Databricks e PySpark — Arquitetura Medalhão

Projeto prático de estudos em **Engenharia de Dados** com Databricks, SQL e PySpark. O objetivo é praticar a ingestão de arquivos CSV, sua organização em tabelas na camada Bronze e a transformação dos dados para a camada Silver seguindo os conceitos da **Medallion Architecture**.

> Este repositório documenta um projeto de aprendizado. Os notebooks devem ser executados em um ambiente Databricks configurado com o catálogo, os schemas e o volume descritos abaixo.

## Objetivos do projeto

- Ler arquivos CSV armazenados na área `raw` de um volume do Unity Catalog.
- Criar tabelas Delta na camada Bronze, preservando os dados de origem sem transformações de negócio nessa etapa.
- Utilizar PySpark para padronizar tipos de dados, criar colunas derivadas e aplicar regras de negócio.
- Gravar os dados processados em tabelas da camada Silver.
- Consultar as tabelas SQL para validar os resultados.

## Arquitetura

```text
Arquivos CSV na área raw
        |
        v
Unity Catalog: lakehouse_vertice
        |
        v
Camada Bronze — ingestão dos dados de origem
  ├── bronze.compras
  ├── bronze.financeiro
  └── bronze.colaboradores
        |
        v
Transformações com PySpark
        |
        v
Camada Silver — dados tratados e enriquecidos
  ├── silver.compras
  ├── silver.financeiro
  └── silver.colaboradores
```

A arquitetura acima representa o fluxo planejado para as três entidades. As transformações de cada tabela são descritas a seguir; execute os notebooks correspondentes conforme a implementação disponível no projeto.

## Tecnologias utilizadas

- **Databricks** — ambiente de desenvolvimento e execução dos notebooks.
- **Apache Spark / PySpark** — leitura, transformação e gravação dos dados.
- **SQL** — criação e consulta das tabelas.
- **Unity Catalog** — organização dos dados por catálogo, schema e volume.
- **Delta Lake** — formato utilizado para persistir as tabelas gerenciadas pelo Databricks.
- **Arquitetura Medalhão** — separação entre ingestão (Bronze) e transformação (Silver).

## Organização dos dados

O projeto utiliza o catálogo `lakehouse_vertice`, com os schemas `bronze` e `silver`. Os arquivos CSV de entrada ficam em um volume na área `bronze/raw`.

Exemplos dos caminhos de origem usados nos notebooks:

| Entidade | Diretório de origem | Tabela Bronze |
|---|---|---|
| Compras | `/Volumes/lakehouse_vertice/bronze/raw/compras/` | `lakehouse_vertice.bronze.compras` |
| Financeiro | `/Volumes/lakehouse_vertice/bronze/raw/financeiro/` | `lakehouse_vertice.bronze.financeiro` |
| Colaboradores | `/Volumes/lakehouse_vertice/bronze/raw/rh/` | `lakehouse_vertice.bronze.colaboradores` |

Os diretórios, os schemas e o volume precisam existir no workspace, e o usuário precisa ter permissões de leitura e gravação adequadas.

## Etapas do pipeline

### 1. Raw → Bronze: ingestão dos CSVs

Os arquivos CSV são lidos com `READ_FILES` em SQL e gravados como tabelas. Nessa etapa, o objetivo é disponibilizar os dados de origem em tabelas consultáveis, sem aplicar regras de negócio.

Exemplo para a tabela Financeiro:

```sql
CREATE OR REPLACE TABLE lakehouse_vertice.bronze.financeiro AS
SELECT *
FROM READ_FILES(
    '/Volumes/lakehouse_vertice/bronze/raw/financeiro/',
    FORMAT => 'CSV',
    HEADER => TRUE,
    INFERSCHEMA => TRUE
);
```

O mesmo padrão é usado para as entidades Compras e Colaboradores, alterando o diretório e o nome da tabela.

### 2. Bronze → Silver: transformação com PySpark

Após a leitura da tabela Bronze, as transformações são realizadas com DataFrames PySpark e o resultado é gravado na camada Silver.

**Financeiro**

- Padronização do separador decimal, substituindo vírgula por ponto em valores textuais como `1234,56`.
- Conversão da coluna `valor` para `DecimalType(15, 2)`.
- Criação da coluna `cliente`, classificando os registros por faixa de valor:
  - Valor maior que zero e menor que 10.000: `Cliente Bronze`.
  - Valor entre 10.000 (inclusive) e 50.000 (exclusive): `Cliente Prata`.
  - Valor a partir de 50.000: `Cliente Ouro`.
  - Valor nulo: `Não atribuído`.
  - Valor igual ou inferior a zero: `Cliente não orçado`.
- Gravação do resultado em `lakehouse_vertice.silver.financeiro` no formato Delta.

**Compras**

- Comparação entre `data_entrega` e `data_prometida` para identificar entregas atrasadas ou no prazo.
- Cálculo da diferença em dias entre as datas e tratamento de diferenças negativas, de acordo com a regra de negócio adotada.
- Gravação do resultado em `lakehouse_vertice.silver.compras`.

**Colaboradores**

- Criação da coluna `ativo` a partir de `data_desligamento`.
- Seleção das colunas relevantes para a tabela Silver.
- Gravação do resultado em `lakehouse_vertice.silver.colaboradores`.

> Observação sobre valores monetários: a padronização descrita considera números com vírgula decimal e sem separador de milhar, como `1234,56`. Se os arquivos contiverem valores como `1.234,56`, é necessário tratar o separador de milhar antes da conversão. Também é recomendável validar os valores de origem e o comportamento do `cast` no ambiente utilizado.

### 3. Validação dos resultados

Após a gravação, as tabelas podem ser consultadas no Databricks SQL ou em células SQL dos notebooks. Exemplo:

```sql
SELECT *
FROM lakehouse_vertice.silver.financeiro
LIMIT 100;
```

A consulta permite inspecionar uma amostra dos dados transformados. Para uma validação mais completa, também podem ser adicionadas verificações de nulos, tipos de dados, contagem de registros e regras de classificação.

## Como executar

1. Abra ou importe os notebooks em um workspace Databricks.
2. Configure o Unity Catalog com o catálogo `lakehouse_vertice`, os schemas `bronze` e `silver` e o volume usado para os arquivos de origem.
3. Disponibilize os CSVs nos diretórios indicados na seção **Organização dos dados**.
4. Execute primeiro as células SQL de ingestão Raw → Bronze.
5. Execute as transformações PySpark de cada entidade para gerar as tabelas Silver.
6. Execute as consultas SQL de validação e confira os resultados.

Os nomes de catálogo, schemas, volume e diretórios são específicos deste exercício e devem ser ajustados para outro ambiente. As células com `%sql` são magics de notebook Databricks e não devem ser executadas diretamente como um script Python comum.

## Dependências

As operações usadas neste projeto são fornecidas pelo Databricks Runtime: Spark/PySpark, SQL e suporte ao formato Delta. Portanto, não é necessário instalar dependências Python adicionais dentro de um cluster Databricks já configurado. Consulte [`requirements.txt`](requirements.txt) para essa observação.

Se o projeto for executado fora do Databricks, será necessário preparar um ambiente Apache Spark compatível e adaptar recursos específicos do workspace, como Unity Catalog, caminhos `/Volumes/...` e comandos `%sql`.

## Possíveis evoluções

- Adicionar validações de qualidade de dados e métricas de registros rejeitados.
- Tratar explicitamente datas e valores ausentes ou inválidos.
- Implementar logs e métricas de execução.
- Avaliar estratégias de carga incremental quando fizer sentido para a origem.
- Criar documentação de esquema, regras de negócio e exemplos de consultas analíticas.

## Contexto

Este projeto tem finalidade educacional e registra a evolução prática nos estudos de Engenharia de Dados com Databricks, PySpark, SQL e arquitetura Lakehouse.
