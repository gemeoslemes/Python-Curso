import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []

for numero in range(10):
    lista.append(numero)

#print(lista)

lista = [numero * 2 for numero in range(10)]

#print(lista)

produtos = [
    {'nome': 'p1', 'preco': 25.50},
    {'nome': 'p2', 'preco': 60.00},
    {'nome': 'p3', 'preco': 71.99},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 50 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep=' \n')


novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 50 else {**produto}
    for produto in produtos
    if produto['preco'] * 1.05 > 50
]

p(novos_produtos)



