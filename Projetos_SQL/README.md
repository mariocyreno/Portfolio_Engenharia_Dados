# 🗄️ Portfólio SQL: Consultas e Data Warehousing

Bem-vindo ao meu diretório de scripts SQL!

Esta pasta contém consultas avançadas desenvolvidas para extrair inteligência de negócio a partir de bancos de dados relacionais e arquiteturas de Data Warehouse. O foco aqui é demonstrar domínio em modelagem de dados, agregações complexas e otimização de consultas.

## 📂 Consultas Incluídas

| Projeto | Resumo da Consulta | Conceitos Aplicados |
| :--- | :--- | :--- |
| **[`ranking-vendedores-dw`](./ranking-vendedores-dw/)** | Consulta em um Data Warehouse (Star Schema) para gerar o ranking de performance comercial da equipe. | `CTEs (WITH)`, `Window Functions (DENSE_RANK)`, `LEFT JOIN`, `GROUP BY` |
| **[`relatorio-vendas-ecommerce`](./relatorio-vendas-ecommerce/)** | Query de consolidação para "achatar" tabelas relacionais de um e-commerce visando consumo por ferramentas de BI. | `Múltiplos LEFT JOINs`, `CONCAT`, `Aliases`, `Modelagem Relacional` |

## 🎯 Objetivo
Os códigos aqui presentes foram estruturados pensando em performance e legibilidade, utilizando as melhores práticas de formatação (uppercase para palavras reservadas e indentação clara) para facilitar a manutenção por times de dados.