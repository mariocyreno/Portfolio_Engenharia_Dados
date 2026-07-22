/*
===============================================================================
Projeto: Sales Data Warehouse
Processo: Full Load
Destino: SalesDW

Descrição:
Realiza a carga completa das tabelas do Data Warehouse a partir das fontes
SalesStage e Ecommerce.

Estratégia:
    1. Remove as tabelas existentes no destino.
    2. Recria a estrutura das tabelas.
    3. Realiza a carga completa dos dados.
    4. Executa o processo dentro de uma transação.
===============================================================================
*/

USE SalesDW;
GO

BEGIN TRANSACTION;

/*=============================================================================
    1. FATO VENDAS
    Origem: SalesStage.dbo.VendasStage
=============================================================================*/

PRINT 'Iniciando carga da tabela VendasDW...';

DROP TABLE dbo.VendasDW;

CREATE TABLE dbo.VendasDW
(
    Data              DATETIME NULL,
    IdVenda           INT NULL,
    IdCategoria       INT NULL,
    Categoria         NVARCHAR(255) NULL,
    Pais              NVARCHAR(255) NULL,
    IdProduto         INT NULL,
    Produto           NVARCHAR(255) NULL,
    Custo_Fabricacao  MONEY NULL,
    Unidades_Vendidas FLOAT NULL,
    Preco_Venda       MONEY NULL,
    Vendas_Total      MONEY NULL,
    Descontos         MONEY NULL
);

INSERT INTO dbo.VendasDW
(
    Data,
    IdVenda,
    IdCategoria,
    Categoria,
    Pais,
    IdProduto,
    Produto,
    Custo_Fabricacao,
    Unidades_Vendidas,
    Preco_Venda,
    Vendas_Total,
    Descontos
)
SELECT
    Data,
    IdVenda,
    IdCategoria,
    Categoria,
    Pais,
    IdProduto,
    Produto,
    Custo_Fabricacao,
    Unidades_Vendidas,
    Preco_Venda,
    Vendas_Total,
    Descontos
FROM SalesStage.dbo.VendasStage;

PRINT 'Carga da tabela VendasDW concluída.';


/*=============================================================================
    2. DIMENSÃO CATEGORIA
    Origem: Ecommerce.dbo.Dim_Categoria
=============================================================================*/

PRINT 'Iniciando carga da tabela Dim_Categoria_DW...';

DROP TABLE dbo.Dim_Categoria_DW;

CREATE TABLE dbo.Dim_Categoria_DW
(
    Id   INT IDENTITY(1,1) NOT NULL,
    Name NVARCHAR(MAX) NULL
);

INSERT INTO dbo.Dim_Categoria_DW
(
    Name
)
SELECT
    Name
FROM Ecommerce.dbo.Dim_Categoria;

PRINT 'Carga da tabela Dim_Categoria_DW concluída.';


/*=============================================================================
    3. DIMENSÃO CLIENTE
    Origem: Ecommerce.dbo.Dim_Clientes
=============================================================================*/

PRINT 'Iniciando carga da tabela Dim_Clientes_DW...';

DROP TABLE dbo.Dim_Clientes_DW;

CREATE TABLE dbo.Dim_Clientes_DW
(
    Id          INT IDENTITY(1,1) NOT NULL,
    Created_at  DATETIME NULL,
    First_Name  NVARCHAR(MAX) NULL,
    Last_Name   NVARCHAR(MAX) NULL,
    Email       NVARCHAR(MAX) NULL,
    Cell_Phone  NVARCHAR(50) NULL,
    Country     NVARCHAR(50) NULL,
    State       NVARCHAR(50) NULL,
    Street      NVARCHAR(MAX) NULL,
    Number      NVARCHAR(50) NULL,
    Additionals NVARCHAR(50) NULL
);

INSERT INTO dbo.Dim_Clientes_DW
(
    Created_at,
    First_Name,
    Last_Name,
    Email,
    Cell_Phone,
    Country,
    State,
    Street,
    Number,
    Additionals
)
SELECT
    Created_at,
    First_Name,
    Last_Name,
    Email,
    Cell_Phone,
    Country,
    State,
    Street,
    Number,
    Additionals
FROM Ecommerce.dbo.Dim_Clientes;

PRINT 'Carga da tabela Dim_Clientes_DW concluída.';


/*=============================================================================
    4. DIMENSÃO ITENS
    Origem: Ecommerce.dbo.Dim_Itens
=============================================================================*/

PRINT 'Iniciando carga da tabela Dim_Itens_DW...';

DROP TABLE dbo.Dim_Itens_DW;

CREATE TABLE dbo.Dim_Itens_DW
(
    Id          INT NOT NULL,
    Order_id    INT NULL,
    Product_id  INT NULL,
    Quantity    INT NULL,
    Total_price MONEY NULL
);

INSERT INTO dbo.Dim_Itens_DW
(
    Id,
    Order_id,
    Product_id,
    Quantity,
    Total_price
)
SELECT
    Id,
    Order_id,
    Product_id,
    Quantity,
    Total_price
FROM Ecommerce.dbo.Dim_Itens;

PRINT 'Carga da tabela Dim_Itens_DW concluída.';


/*=============================================================================
    5. DIMENSÃO PRODUTO
    Origem: Ecommerce.dbo.Dim_Produto
=============================================================================*/

PRINT 'Iniciando carga da tabela Dim_Produto_DW...';

DROP TABLE dbo.Dim_Produto_DW;

CREATE TABLE dbo.Dim_Produto_DW
(
    Id          INT NOT NULL,
    Name        NVARCHAR(MAX) NULL,
    Price       MONEY NULL,
    Id_Category INT NULL
);

INSERT INTO dbo.Dim_Produto_DW
(
    Id,
    Name,
    Price,
    Id_Category
)
SELECT
    Id,
    Name,
    Price,
    Id_Category
FROM Ecommerce.dbo.Dim_Produto;

PRINT 'Carga da tabela Dim_Produto_DW concluída.';


/*=============================================================================
    FINALIZAÇÃO DA TRANSAÇÃO
=============================================================================*/

COMMIT TRANSACTION;

PRINT '==============================================';
PRINT 'Carga completa do Data Warehouse concluída.';
PRINT 'Processo executado com sucesso.';
PRINT '==============================================';