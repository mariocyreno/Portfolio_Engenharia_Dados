# Análise de Desempenho de Vendedores (Data Warehouse) 🏆

Este projeto contém uma query SQL avançada executada sobre uma arquitetura de Data Warehouse (modelo Star/Snowflake Schema). O objetivo é avaliar a performance da equipe comercial, gerando um ranking detalhado dos vendedores com base no total de vendas e lucro gerado por produtos.

## 🛠️ Tecnologias e Conceitos Aplicados
* **SQL (Transact-SQL)**
* **CTE (Common Table Expressions):** Utilização da cláusula `WITH` para organizar e pré-processar as métricas de vendas e custos antes da seleção final.
* **Window Functions:** Aplicação da função `DENSE_RANK()` para classificar o desempenho dos vendedores (ranking) de forma contínua, sem pular posições em caso de empate.
* **Modelagem Dimensional:** Cruzamento de dados entre tabelas Fato (`FactResellerSales`) e Dimensões (`DimEmployee`, `DimProduct`, `DimProductCategory`).

## 📊 Estrutura da Consulta

O script realiza as seguintes operações:
1. **Agregação Base (CTE):** Calcula o preço unitário, total de vendas, custo total e lucro, agrupando as informações no nível do Vendedor e Produto.
2. **Classificação (Main Query):** Lê a CTE pré-processada e aplica o ranqueamento global com base na soma do total de vendas.

## 🚀 Como utilizar
Para testar este script, copie o código e execute em um SGBD conectado a um Data Warehouse contendo o schema de tabelas `Fact` e `Dim` (como o Microsoft AdventureWorks ou modelos similares).