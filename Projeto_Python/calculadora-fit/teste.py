# Calculadora de Dieta FIT
def calcular_dieta():
    print("==== Bem-vindo à Calculadora de Dieta FIT! ====\n" \
          "=== Calculadora de Dieta para Perda de Peso ===\n")

#Coletando o nome do usuário
nome = input("Informe o seu nome: ").strip().title()
peso = float(input("Informe seu peso em kg(ex: 70.0): "))
altura = float(input("inorme sua altura em cm (ex: 170): "))
idade = int(input('Informe sua idade (ex: 25): '))
sexo = input("Informe seu sexo (M/F): ").strip().upper()
    
print('''
    === Nível de Atividade Física ===
    1- Sedentário (pouco ou nenhum exercício)
    2- Levemente ativo (exercício leve 1-3 dias/semana)
    3- Moderadamente ativo (exercício moderado 3-5 dias/semana)
    4- Muito ativo (exercício intenso 6-7 dias/semana)
    5- Extremamente ativo (exercício intenso diário ou trabalho físico)
          ''')

fatores = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725, "5": 1.9}
nivel = input("Informe seu nível de atividade física (1-5): ").strip()

fator = fatores[nivel]

    # Calculando 
    #IMC
    #altura_m = altura / 100
    #imc = peso / (altura_m ** 2)
imc = peso / ((altura / 100) ** 2)
    
if imc < 18.5:
        print('\n🚨 Atenção: seu IMC indica abaixo do peso.')
        print('Uma dieta de emagrecimento pode ser prejudicial.')
        print('Consulte um médico ou nutricionista antes de continuar.\n')

    
    #TMB (Taxa Metabolica Basal) — Mifflin-St Jeor
if sexo == 'M':
    tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    kcal_min = 1500
else:
    tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    kcal_min = 1200
    
    #TDEE e Deficit
    tdee = tmb * fator
    kcal = tdee * 0.80

    # Deficit máximo seguro: nunca abaixo do mínimo
    if kcal < kcal_min:
        kcal = kcal_min
        print(f'\n⚠️  Deficit ajustado para o mínimo seguro: {kcal_min} kcal/dia')

    # Deficit máximo: nunca maior que 1000 kcal/dia
    if (tdee - kcal) > 1000:
        kcal = tdee - 1000
        print('\n⚠️ Deficit ajustado para o máximo seguro: 1000 kcal/dia')
    
    #Macros
    proteina = peso * 1.8
    gordura  = peso * 0.9
    fibra    = (kcal / 1000) * 14
    carbo    = (kcal - (proteina * 4) - (gordura * 9)) / 4

    # Carboidratos mínimos: nunca abaixo de 100g/dia
    if carbo < 0:
        # Se os carbos ficarem negativos, a gordura é levemente reduzida para acomodar a proteína      
        print('\n⚠️ Carboidratos negativos detectados. Ajustando gordura paragarantir a proteína necessária.')
        carbo = 0
        gordura = (kcal - (proteina * 4)) / 9
    elif carbo < 50:
        print('\n⚠️  Atenção: A dieta resultou em carboidratos baixos (Low Carb) para não comprometer sua proteína.')
    
    # Perda Estimada
    deficit_semanal = (tdee - kcal) * 7
    perda_kg_semana = deficit_semanal / 7700 # -> 1kg = ~7700 kcal

     # Classificação IMC
    if imc < 18.5:
        classe_imc = 'Abaixo do peso'
    elif imc < 25:
        classe_imc = 'Peso normal'
    elif imc < 30:
        classe_imc = 'Sobrepeso'
    elif imc < 35:
        classe_imc = 'Obesidade grau I'
    elif imc < 40:
        classe_imc = 'Obesidade grau II'
    else:
        classe_imc = 'Obesidade grau III'

    # Resultados
    print(f'''
    ╔══════════════════════════════════════╗
    ║         RESULTADO DA DIETA           ║
    ╚══════════════════════════════════════╝
    👤 Paciente: {nome}
          
    📊 Avaliação
        IMC     : {imc:.2f} ({classe_imc})
        TBM     : {tmb:.0f} kcal/dia
        TDEE    : {tdee:.0f} kcal/dia
        META    : {kcal:.0f} kcal/dia
        DEFICT  : {tdee - kcal:.0f} kcal/dia
        
    ⚠️ ⚠️ ⚠️  ATENÇÃO SOBRE O IMC: ⚠️ ⚠️ ⚠️
    O IMC é uma métrica geral e não diferencia massa muscular de gordura corporal. 
    Indivíduos muito musculosos (como atletas) podem apresentar um IMC na faixa de 
    "Sobrepeso" ou "Obesidade" mesmo tendo um percentual de gordura muito baixo. 
    Portanto, o IMC não deve ser avaliado isoladamente. Para uma avaliação precisa, 
    um profissional deve medir sua composição corporal utilizando métodos específicos 
    (como dobras cutâneas ou bioimpedância).
    
    🍽️  Macronutrientes
        🔥 Calorias     : {kcal:.0f}
        🥩 Proteína     : {proteina:.2f}g - ({proteina * 4:.0f} kcal)
        🥑 Gordura      : {gordura:.2f}g - ({gordura * 9:.0f} kcal)
        🍚 Carboidrato  : {carbo:.2f}g - ({carbo * 4:.0f} kcal)
        🌿 Fibra        : {fibra:.2f}g

    📉 Estimativa de Perda
        ~{perda_kg_semana:.2f} kg/semana
        ~{perda_kg_semana * 4:.2f}kg/mês
    
    ⚠️  Este cálculo é uma estimativa.
    Consulte um nutricionista para um
    plano alimentar personalizado.    
    ''')
calcular_dieta()
    
