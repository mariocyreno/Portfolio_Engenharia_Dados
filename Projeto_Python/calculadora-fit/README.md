# 💪 Calculadora de Dieta FIT (Terminal)

Uma calculadora de linha de comando desenvolvida em Python para gerar estimativas de planos alimentares com foco em **perda de peso e preservação de massa magra**.

## 📌 Sobre o Projeto
Este script recebe os dados físicos do usuário e calcula métricas importantes de saúde e nutrição baseadas na equação científica de Mifflin-St Jeor. A calculadora possui travas de segurança para impedir deficits calóricos extremos ou dietas prejudiciais para pessoas já abaixo do peso.

## 🚀 Funcionalidades
- **Cálculo de IMC:** Classificação atual do Índice de Massa Corporal com ressalva para perfis atléticos.
- **Taxa Metabólica Basal (TMB):** Estimativa de calorias gastas em repouso.
- **Gasto Diário Total (TDEE):** Ajustado pelo nível de atividade física (Sedentário a Extremamente Ativo).
- **Meta Calórica com Deficit:** Aplicação de 20% de deficit calórico (travado em um limite de segurança máximo de 1000 kcal).
- **Distribuição de Macronutrientes:** - Proteína focada em manutenção muscular (1.8g/kg).
  - Gordura para manutenção hormonal (0.9g/kg).
  - Carboidratos ajustados conforme a sobra calórica.
- **Estimativa de Perda de Peso:** Projeção semanal e mensal.

## 📋 Pré-requisitos
- **Python 3.6** ou superior instalado na máquina.
- Nenhuma biblioteca externa é necessária.

## 🔧 Como executar
1. Faça o clone deste repositório ou baixe o arquivo `main.py`.
2. Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do VS Code).
3. Navegue até a pasta do projeto:
   ```bash
   cd calculadora-fit