# Sales Data Warehouse
Projeto de construção de um Data Warehouse utilizando SQL Server,
com aplicação de conceitos de ETL, Staging Area e Full Load.

## Arquitetura
O projeto utiliza uma arquitetura dividida em camadas:
    * Source → Staging → Data Warehouse

### Fontes de dados
- Sales
- Ecommerce

### Staging
- SalesStage
  - VendasStage

### Data Warehouse
- SalesDW
  - VendasDW
  - Dim_Categoria_DW
  - Dim_Clientes_DW
  - Dim_Itens_DW
  - Dim_Produto_DW

## Processo de Carga
O processo utiliza uma estratégia de Full Load.
A cada execução:
1. As tabelas existentes no Data Warehouse são removidas.
2. As tabelas são recriadas.
3. Os dados são extraídos das fontes.
4. Os dados são carregados no Data Warehouse.
5. O processo é executado dentro de uma transação.

## Tecnologias
- SQL Server
- T-SQL
- Data Warehouse
- ETL
- Staging Area
- Full Load