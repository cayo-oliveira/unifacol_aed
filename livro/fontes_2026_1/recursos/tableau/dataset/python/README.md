# Ambiente Virtual para o Notebook de Preparação do Tableau

Este guia explica como configurar um ambiente virtual Python para executar o notebook `preparacao_tableau.ipynb` em diferentes sistemas operacionais (Windows, macOS e Linux).

## Pré-requisitos
- Python 3.8 ou superior instalado.
- Acesso ao terminal/command prompt.

## Passos Gerais
1. Criar um ambiente virtual (.venv).
2. Ativar o ambiente virtual.
3. Instalar as dependências do `requirements.txt`.

## Windows

### 1. Criar Ambiente Virtual
Abra o Command Prompt e navegue até a pasta `python/`:
```
cd caminho\para\a\pasta\python
python -m venv .venv
```

### 2. Ativar Ambiente Virtual
```
.venv\Scripts\activate
```

### 3. Instalar Dependências
```
pip install -r requirements.txt
```

### 4. Desativar (opcional)
```
deactivate
```

## macOS e Linux

### 1. Criar Ambiente Virtual
Abra o Terminal e navegue até a pasta `python/`:
```
cd caminho/para/a/pasta/python
python3 -m venv .venv
```

### 2. Ativar Ambiente Virtual
```
source .venv/bin/activate
```

### 3. Instalar Dependências
```
pip install -r requirements.txt
```

### 4. Desativar (opcional)
```
deactivate
```

## Arquivo requirements.txt
O arquivo `requirements.txt` contém as bibliotecas necessárias:
```
pandas
numpy
scikit-learn
```

## Executar o Notebook
Após ativar o ambiente e instalar as dependências, abra o Jupyter Notebook:
```
jupyter notebook preparacao_tableau.ipynb
```

Ou use o VS Code para abrir e executar as células.