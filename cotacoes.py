# Importando as bibliotecas necessárias
import requests
import json
import pandas as pd

# Fazer a requisição no site de cotações
requisicao = requests.get("https://economia.awesomeapi.com.br/json/all")
cotacoes_json = requisicao.json()

# Percorrer cada moeda e cotação usando list comprehension
dados = [{'Moeda':moeda, 'Valor':valor['bid']} for moeda, valor in cotacoes_json.items()]

# Armazena em um dataframe
dataframe = pd.DataFrame(dados)

# Colocando as cotações em ordem descrescente
dataframe = dataframe.sort_values('Valor', ascending=False) 

# Resetando os índices que estavam fora de ordem
dataframe = dataframe.reset_index(drop=True) 
display(dataframe)

# Salvar em um arquivo csv na pasta atual:
dataframe.to_csv(r'tabela-cotacoes.csv', sep=';')
