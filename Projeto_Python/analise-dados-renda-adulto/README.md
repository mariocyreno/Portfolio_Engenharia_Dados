# Adult Income Data Analysis

Projeto de análise de dados desenvolvido em Python utilizando o dataset **Adult**, disponibilizado pelo **UCI Machine Learning Repository**.

O objetivo do projeto é realizar uma análise inicial da distribuição de renda dos indivíduos presentes no dataset, utilizando técnicas de análise exploratória de dados e visualização.

## 📌 Objetivos

* Carregar dados diretamente do UCI Machine Learning Repository;
* Estruturar o dataset utilizando o Pandas;
* Inspecionar informações e características dos dados;
* Analisar a distribuição da variável de renda (`income`);
* Separar os registros em diferentes classes de renda;
* Utilizar visualizações para compreender a distribuição das classes;
* Praticar conceitos de análise exploratória de dados (EDA).

## 🗂️ Dataset

O projeto utiliza o dataset **Adult**, também conhecido como **Census Income Dataset**.

O dataset contém informações demográficas e socioeconômicas de indivíduos, incluindo:

* Idade;
* Classe de trabalho;
* Escolaridade;
* Estado civil;
* Ocupação;
* Relacionamento familiar;
* Raça;
* Sexo;
* Ganho de capital;
* Perda de capital;
* Horas trabalhadas por semana;
* País de origem;
* Faixa de renda.

A variável `income` representa a classe de renda dos indivíduos:

* `<=50K`
* `>50K`

Os dados são carregados diretamente do UCI Machine Learning Repository.

## 🛠️ Tecnologias utilizadas

* Python
* NumPy
* Pandas
* SciPy
* Matplotlib
* Seaborn

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entre no diretório:

```bash
cd adult-income-data-analysis
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Execução

Execute o script Python:

```bash
python adult_income_analysis.py
```

Também é possível executar o projeto em um ambiente Jupyter Notebook.

## 🔎 Etapas do projeto

### 1. Carregamento dos dados

Os dados são obtidos diretamente do UCI Machine Learning Repository:

```python
url_dados = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
```

O Pandas é utilizado para carregar o arquivo e definir os nomes das colunas:

```python
dados = pd.read_csv(
    url_dados,
    header=None,
    sep=',',
    na_values=[' ?', ' ?', ' ?'],
    names=colunas
)
```

### 2. Inspeção dos dados

O método `info()` é utilizado para obter informações sobre a estrutura do dataset:

```python
dados.info()
```

Essa etapa permite verificar informações como:

* Quantidade de registros;
* Quantidade de variáveis;
* Tipos de dados;
* Valores ausentes.

### 3. Análise da variável de renda

A variável `income` é utilizada para visualizar a distribuição das classes:

```python
sns.displot(dados, x="income", hue="income")

plt.show()
```

Essa visualização permite observar a quantidade relativa de indivíduos em cada faixa de renda.

### 4. Separação das classes

Os registros são separados em dois grupos:

```python
classe_menor50 = dados[dados['income'] == ' <=50K']

classe_maior50 = dados[dados['income'] == ' >50K']
```

Em seguida, a quantidade de registros de cada classe é apresentada:

```python
print(f"Classe <=50K: {len(classe_menor50)}")
print(f"Classe >50K: {len(classe_maior50)}")
```

## 📊 Análise

A análise inicial permite observar a distribuição da variável de renda e identificar possíveis diferenças de representatividade entre as classes.

Essa etapa é importante antes da aplicação de técnicas de Machine Learning, pois permite compreender a estrutura dos dados e identificar características como **desbalanceamento de classes**.

## 📚 Conceitos praticados

Este projeto aborda conceitos importantes de:

* Análise Exploratória de Dados (EDA);
* Manipulação de dados com Pandas;
* Estatística com SciPy;
* Visualização de dados;
* Distribuição de classes;
* Identificação de possíveis dados ausentes;
* Preparação de dados para Machine Learning.

## 📁 Estrutura do projeto

```text
adult-income-data-analysis/
├── README.md
├── requirements.txt
└── adult_income_analysis.py
```

## 👨‍💻 Autor

**Mario Cyreno**

Projeto desenvolvido para estudos e prática de conceitos de **Data Analysis, Data Science, Estatística e Python**.
