# Relatório Consolidado de Vendas (SQL) 🛒

Este projeto contém uma query SQL avançada desenvolvida para extrair e consolidar informações de um banco de dados relacional de e-commerce/vendas. O objetivo da consulta é gerar uma visão completa e achatada (flat) de cada item vendido, facilitando a criação de dashboards em ferramentas de BI (como Power BI ou Tableau) ou análises em planilhas.

## 🛠️ Tecnologias Utilizadas
* **SQL (Transact-SQL / SQL Server):** Linguagem utilizada para a consulta.

## 📊 Estrutura da Consulta

A query realiza o relacionamento de 5 tabelas diferentes utilizando `LEFT JOIN` para garantir que o histórico de itens não seja perdido:
1. **Itens (Tabela Fato):** Base da consulta, trazendo a quantidade e o valor total.
2. **Ordens:** Para buscar o status do pedido e a data da compra.
3. **Produtos:** Para resgatar o nome e calcular o preço unitário do produto na época da compra.
4. **Categoria:** Para fins de relacionamento estrutural do produto.
5. **Clientes:** Para anexar os dados demográficos (Nome, Email, Telefone, UF).

## 🚀 Como utilizar
Para rodar este script, basta copiá-lo ou abri-lo em qualquer Sistema Gerenciador de Banco de Dados (SGBD) conectado ao seu banco relacional (ex: SQL Server Management Studio, DBeaver, Azure Data Studio) e executar a consulta.