# Classificação de Vinhos com Regressão Logística

Projeto de Machine Learning desenvolvido em Python utilizando o dataset **Wine**, disponibilizado pela biblioteca `scikit-learn`.

O objetivo do projeto é aplicar um modelo de **Regressão Logística** para classificação dos tipos de vinho e avaliar seu desempenho utilizando diferentes estratégias de validação.

## 📌 Objetivos

* Carregar e explorar o dataset Wine;
* Separar as variáveis de entrada e saída;
* Dividir os dados em conjuntos de treinamento e teste;
* Treinar um modelo de Regressão Logística;
* Realizar previsões sobre dados não utilizados no treinamento;
* Avaliar a acurácia do modelo;
* Aplicar **K-Fold Cross Validation** para avaliar o desempenho do modelo.

## 🗂️ Dataset

O projeto utiliza o dataset **Wine**, disponível diretamente através do `scikit-learn`.

O conjunto de dados possui:

* **178 registros**
* **13 variáveis de entrada**
* **3 classes de classificação**

As variáveis representam diferentes características químicas dos vinhos, enquanto a variável `target` representa a classe à qual cada vinho pertence.

## 🛠️ Tecnologias utilizadas

* Python
* NumPy
* Scikit-learn
* Logistic Regression
* Train/Test Split
* K-Fold Cross Validation
* Accuracy Score

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entre no diretório:

```bash
cd SEU-REPOSITORIO
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Execução

Execute o script Python:

```bash
python nome_do_arquivo.py
```

Caso esteja utilizando Jupyter Notebook, basta executar as células sequencialmente.

## 🔎 Etapas do projeto

### 1. Carregamento dos dados

O dataset Wine é carregado através do módulo `datasets` do Scikit-learn:

```python
wine = datasets.load_wine()

x = wine.data
y = wine.target
```

### 2. Separação entre treinamento e teste

Os dados são divididos utilizando `train_test_split`, com:

* **60%** para treinamento;
* **40%** para teste;
* `random_state=42` para permitir a reprodução dos resultados.

```python
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.4,
    random_state=42
)
```

### 3. Treinamento do modelo

É utilizado um modelo de **Regressão Logística**:

```python
clf = LogisticRegression(
    solver='lbfgs',
    max_iter=10000
)

clf.fit(x_train, y_train)
```

### 4. Predição

Após o treinamento, o modelo realiza a classificação dos dados de teste:

```python
y_pred = clf.predict(x_test)
```

### 5. Avaliação

A performance do modelo é avaliada utilizando a métrica **Accuracy Score**:

```python
accuracy_score(y_test, y_pred)
```

A acurácia representa a proporção de classificações realizadas corretamente pelo modelo.

### 6. K-Fold Cross Validation

O projeto também utiliza **K-Fold Cross Validation** com 5 folds:

```python
kd = KFold(n_splits=5)
```

Nesse processo, os dados são divididos em cinco partes. Em cada iteração, uma parte é utilizada para teste e as demais para treinamento.

Essa abordagem permite avaliar o comportamento do modelo em diferentes divisões dos dados, proporcionando uma avaliação mais robusta do desempenho.

## 📊 Resultados

O projeto apresenta a acurácia obtida pelo modelo na divisão entre treinamento e teste e também utiliza Cross Validation como estratégia complementar de avaliação.

Os resultados podem variar caso parâmetros como `random_state`, `test_size` ou a configuração do modelo sejam alterados.

## 📚 Conceitos praticados

Este projeto foi desenvolvido com foco no aprendizado e prática dos seguintes conceitos de Machine Learning:

* Classificação supervisionada;
* Regressão Logística;
* Separação entre treino e teste;
* Predição de dados não vistos;
* Avaliação de modelos;
* Acurácia;
* Cross Validation;
* K-Fold;
* NumPy;
* Scikit-learn.

## 📁 Estrutura sugerida

```text
.
├── README.md
├── requirements.txt
└── nome_do_arquivo.py
```

## 👨‍💻 Autor

**Mario Cyreno**

Projeto desenvolvido para estudos e prática de conceitos de **Data Science, Machine Learning e Python**.