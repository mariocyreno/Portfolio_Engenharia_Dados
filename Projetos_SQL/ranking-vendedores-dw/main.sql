with Vendas_Produto as(
    select 
        e.FirstName as Nome
        ,e.LastName as Sobrenome
        ,e.Title as Cargo
        ,e.DepartmentName as Departamento
        ,p.EnglishProductName as Produto
        ,psc.EnglishProductSubCategoryName as Subcategoria
        ,pc.EnglishProductCategoryName as Categoria
        ,round(sum(frs.UnitPrice), 2) as PrecoUnitario
        ,frs.OrderQuantity as Qtde
        ,round(sum(frs.SalesAmount), 2) as TotalVendas
        ,round(sum(frs.TotalProductCost), 2) as CustoTotal
        ,round(SUM(frs.SalesAmount - frs.TotalProductCost), 2) as Lucro

From FactResellerSales frs
Left join DimEmployee e on frs.EmployeeKey = e.EmployeeKey
Left Join DimProduct p on frs.ProductKey = p.ProductKey
Left Join DimProductSubCategory psc on p.ProductSubCategoryKey = psc.ProductSubCategoryKey
Left Join DimProductCategory pc on psc.ProductCategoryKey = pc.ProductCategoryKey
GROUP BY
        frs.UnitPrice
        ,frs.OrderQuantity
        ,frs.TotalProductCost
        ,e.FirstName
        ,e.LastName
        ,e.Title
        ,e.DepartmentName
        ,p.EnglishProductName
        ,psc.EnglishProductSubCategoryName
        ,pc.EnglishProductCategoryName
)
select 
    Nome
    ,Sobrenome
    ,Cargo
    ,Departamento
    ,Produto
    ,Subcategoria
    ,Categoria
    ,PrecoUnitario
    ,Qtde
    ,TotalVendas
    ,CustoTotal
    ,Lucro
    ,DENSE_RANK() OVER (ORDER BY SUM(TotalVendas) DESC) AS Posicao from Vendas_Produto

Group By
    Nome
    ,Sobrenome
    ,Cargo
    ,Departamento
    ,Produto
    ,Subcategoria
    ,Categoria
    ,PrecoUnitario
    ,Qtde
    ,TotalVendas
    ,CustoTotal
    ,Lucro