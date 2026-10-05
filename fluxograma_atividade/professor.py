import json

with open('teste.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(type(dados))