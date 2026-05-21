from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import os
from dotenv import load_dotenv
import pandas as pd

chromedriver_autoinstaller.install()

caminho_env = r'C:\Users\Administrador\Documents\00-Projetos\Projeto_Python\Caminhos\caminho.env'
load_dotenv(dotenv_path=caminho_env)

navegador = webdriver.Chrome()
Link = os.getenv('URL_Formulario')
navegador.get(Link)
Clientes = pd.read_csv(os.getenv('CLIENTE_CSV'), delimiter=',')

for index, row in Clientes.iterrows():  #index = indice identifica cada linha do nosso DF row = linha de cada passo 
    NomeOrigem =        row['first_name']
    SobrenomeOrigem =   row['last_name']
    emailOrigem =       row['email']
    CelularOrigem =     row['cell_phone']
    EstadoOrigem =      row['state']
    
    # Prenchimento automatico
    sleep(3)
    nome =      navegador.find_element(
        by= By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        ).send_keys(NomeOrigem)
    sobrenome=  navegador.find_element(
        by= By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        ).send_keys(SobrenomeOrigem)
    email=      navegador.find_element(
        by= By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        ).send_keys(emailOrigem)
    telefone=   navegador.find_element(
        by= By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
        ).send_keys(CelularOrigem)
    uf=         navegador.find_element(
        by= By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea'
        ).send_keys(EstadoOrigem)
    Enviar =    navegador.find_element(
        by= By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        ).click()
    sleep(2)
    navegador.get(Link)
navegador.quit()