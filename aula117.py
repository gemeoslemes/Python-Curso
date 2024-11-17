import json

# pessoa = {
#     'nome': 'Victor',
#     'sobrenome': 'Lemes',
#     'enderecos': [
#         {'rua': 'A', 'numero': 332},
#         {'rua': 'B', 'numero': 54},
#     ],
#     'altura': 1.75,
#     'numero_preferido': 8,
#     'dev': True,
#     'nada': None
# }

# with open('aula177.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#     )


with open('aula177.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)