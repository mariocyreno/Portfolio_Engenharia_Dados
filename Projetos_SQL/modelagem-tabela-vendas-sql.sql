select
    i.id as Id_Venda
    ,i.product_id as Id_Produto
    ,p.Nome as Produto
    ,(i.total_price / i.quantity) as Preço_Unitário
    ,i.quantity as Quantidade
    ,i.total_price as total
    ,o.status
    ,CONCAT(cl.first_name, ' ', cl.last_name) as Cliente
    ,cl.email as Email_Cliente
    ,cl.cell_phone as Telefone_Cliente
    ,cl.[state] as UF
    ,o.created_at

from Itens i
LEFT JOIN Ordens o on i.order_id = o.id
LEFT JOIN Produtos p on i.product_id = p.ID
LEFT JOIN Categoria c on p.Id_Category = c.ID
LEFT JOIN Clientes cl on o.customer_id = cl.id

ORDER BY i.id DESC

