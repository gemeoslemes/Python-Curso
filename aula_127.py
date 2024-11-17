import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa('Victor', 21)
p2 = Pessoa('Gustavo', 45)
p3 = Pessoa('Bianca', 23)
p4 = Pessoa('Bruna', 18)

bd = [vars(p1), vars(p2), vars(p3), vars(p4)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arq:
    json.dump(bd, arq, ensure_ascii=False, indent=2)