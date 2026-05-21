## Use CTRL + C para interromper a execução do script
import schedule
import time
import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv

def job():
    caminho_env = r"C:\Users\Administrador\Documents\00-Projetos\Projeto_Python\Caminhos\caminho.env" #Caminho Completo
    load_dotenv(dotenv_path=caminho_env)

    server = os.getenv('Nome_Servidor')
    database = os.getenv('Nome_Banco')
    username = os.getenv('Usuario')
    password = os.getenv('Senha')
    conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' \
                                f'SERVER={server};'
                                f'DATABASE={database};'
                                f'USERNAME={username};'
                                f'PASSWORD={password};'
                                'Trusted_Connection=yes;')
    cursor = conexaoDB.cursor()

    dados = pd.read_csv(os.getenv('CLIENTE_CSV'), delimiter=',')

    dados['created_at'] = pd.to_datetime(dados['created_at'])
    dados['email'] = dados['email'].fillna('Sem registro')
    dados['street'] = dados['street'].fillna('Sem Info')
    dados['number'] = dados['number'].fillna('Sem Numero')
    dados['additionals'] = dados['additionals'].fillna('Sem Info')

    cursor.execute('truncate table [Clientes]')
    cursor.commit()

    for index, linha in dados.iterrows():
        linha.email = str(linha.email)  # Converter para o tipo 'str' antes da inserção
        linha.country = str(linha.country)
        linha.state = str(linha.state)
        linha.street = str(linha.street)
        linha.number = str(linha.number)
        linha.additionals = str(linha.additionals)

        cursor.execute("INSERT INTO CLIENTES (id, created_at,first_name, last_name,email,cell_phone,country, state,street, number, additionals) VALUES (?,?,?,?,?,?,?,?,?,?,?)", 
                    linha.id,
                    linha.created_at,
                    linha.first_name,
                    linha.last_name,
                    linha.email,
                    linha.cell_phone,
                    linha.country,
                    linha.state,
                    linha.street,
                    linha.number,
                    linha.additionals)
    cursor.commit()
    cursor.close()
    conexaoDB.close()

schedule.clear()
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)