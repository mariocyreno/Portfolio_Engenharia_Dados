# 🔥 Lakehouse Queimadas

Pipeline de dados em **Databricks** que ingere arquivos CSV de focos de queimadas, trata os dados com **PySpark** e disponibiliza uma tabela analítica pronta para consumo (BI, dashboards, análises exploratórias).

O projeto segue a ideia da **arquitetura medalhão**: os dados brutos ficam na camada **Bronze** e, após limpeza e padronização, são gravados na camada **Gold**.

> **Fonte dos dados:** dados abertos de focos de queimadas no Brasil, referentes a 2026 (até o início de outubro). https://dados.gov.br/dados/conjuntos-dados/monitoramento-de-queimadas

---

## 🧱 Arquitetura

```
CSV (Volume)  ──►  Bronze (Delta)  ──►  Transformações (PySpark)  ──►  Gold (Delta)
/Volumes/...        queimadas                                           queimadas
```

| Camada | Tabela | Descrição |
|--------|--------|-----------|
| Raw | `/Volumes/lakehouse_queimada/bronze/raw` | Arquivos CSV originais, sem alteração |
| Bronze | `lakehouse_queimada.bronze.queimadas` | Cópia fiel dos CSVs em Delta, com schema inferido |
| Gold | `lakehouse_queimada.gold.queimadas` | Dados tratados, com colunas selecionadas e prontos para análise |

> O schema `silver` já existe no catálogo, mas ainda não é utilizado: por enquanto o tratamento é feito entre a Bronze e a Gold.

---

## ⚙️ O que o pipeline faz

1. **Ingestão (Bronze):** lê todos os CSVs do Volume com `READ_FILES` (cabeçalho habilitado, schema inferido e `schemaEvolutionMode = NONE`) e cria a tabela `bronze.queimadas`.
2. **Tratamento de nulos:** em `numero_dias_sem_chuva`, o valor `-999` indica ausência de informação e é convertido para `NULL`.
3. **Padronização de percentuais:** `precipitacao` e `risco_fogo` são multiplicados por 100, arredondados, convertidos para inteiro e gravados como texto com o símbolo `%` (ex.: `0.35` → `35%`).
4. **Seleção de colunas:** são mantidas apenas as colunas relevantes para análise.
5. **Carga (Gold):** grava o resultado em `gold.queimadas` com `mode('overwrite')`.

---

## 📋 Dicionário de dados (Gold)

| Coluna | Descrição |
|--------|-----------|
| `id` | Identificador do foco |
| `lat` | Latitude |
| `lon` | Longitude |
| `data_hora_gmt` | Data e hora da detecção (GMT) |
| `satelite` | Satélite que detectou o foco |
| `municipio` | Município |
| `estado` | Estado |
| `pais` | País |
| `numero_dias_sem_chuva` | Dias sem chuva (`NULL` quando não informado) |
| `precipitacao` | Precipitação, formatada com `%` |
| `risco_fogo` | Risco de fogo, formatado com `%` |
| `bioma` | Bioma |
| `frp` | _Fire Radiative Power_ (potência radiativa do fogo) |

---

## 🛠️ Tecnologias

- Databricks (com Unity Catalog e Volumes)
- PySpark / Spark SQL
- Delta Lake

---

## 🚀 Como executar

### Pré-requisitos

- Workspace Databricks com **Unity Catalog** habilitado
- Permissão para criar catálogo, schemas e volumes

### 1. Criar a estrutura no Databricks

```sql
CREATE CATALOG IF NOT EXISTS lakehouse_queimada;
CREATE SCHEMA  IF NOT EXISTS lakehouse_queimada.bronze;
CREATE SCHEMA  IF NOT EXISTS lakehouse_queimada.silver;
CREATE SCHEMA  IF NOT EXISTS lakehouse_queimada.gold;
CREATE VOLUME  IF NOT EXISTS lakehouse_queimada.bronze.raw;
```

### 2. Carregar os arquivos

Faça upload dos CSVs para o Volume:

```
/Volumes/lakehouse_queimada/bronze/raw
```

### 3. Executar o notebook

Importe o notebook `pipeline_queimadas_bronze_gold` no workspace, anexe a um cluster (ou compute serverless) e execute todas as células.

Ao final, a tabela `lakehouse_queimada.gold.queimadas` estará disponível para consulta:

```sql
SELECT * FROM lakehouse_queimada.gold.queimadas LIMIT 10;
```

---

## 📁 Estrutura do repositório

```
.
├── pipeline_queimadas_bronze_gold.py   # Notebook com o pipeline Bronze → Gold
├── requirements.txt                    # Dependências Python
└── README.md
```

---

## 🔭 Próximos passos

- Usar a camada **Silver** (já criada) para tipagem, deduplicação e validações de qualidade, deixando a Gold apenas com o modelo final
- Ingestão incremental com **Auto Loader**
- Orquestração com **Databricks Workflows**
- Dashboard no Power BI conectado à camada Gold

---

📚 Conceitos praticados

 * Engenharia de Dados;
 * Arquitetura Lakehouse;
 * Arquitetura Medallion;
 * Organização de catálogos, schemas e Volumes;
 * Ingestão de arquivos CSV;
 * Databricks SQL;
 * Processamento distribuído com Apache Spark;
 * Transformação de dados com PySpark;
 * Tratamento de valores ausentes;
 * Seleção e organização de colunas;
 * Persistência de tabelas;
 * Preparação de dados para análise.

O projeto foi desenvolvido para execução em um ambiente Databricks.
Configure o catálogo lakehouse_queimada e os schemas bronze, silver e gold.
Crie o Volume raw no schema bronze.
Disponibilize os arquivos CSV no Volume raw.
Verifique as permissões necessárias para leitura dos arquivos e gravação das tabelas.
Importe o notebook para o Databricks.
Execute as células SQL e Python na ordem definida.

## 👤 Autor

**Mario Henrique**
