import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv

#Caminho do env com os dados de conexão
caminho_do_arquivo_env = r"C:\Users\Administrador\Documents\00-Projetos\Projeto_Python\Caminhos\caminho.env" #Caminho Completo
load_dotenv(dotenv_path=caminho_do_arquivo_env)

server = os.getenv('Nome_Servidor')
database = os.getenv('Nome_Banco')
user = os.getenv('Usuario')
password = os.getenv('Senha')

#tentando fazer conexão com o banco
try:
    conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                               f'server={server};'
                               f'database={database};'
                               f'user={user};'
                               f'password={password};'
                               'Trusted_Connection=yes;'
                               )
    print('Conexão bem sucessida!')

except Exception as e:
    print('Erro ao conectar ao banco de dados:', e)
cursor = conexaoDB.cursor()

#QUERY DB
query = """
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
"""
tb_Vendas = pd.read_sql(query, conexaoDB)
print(tb_Vendas)