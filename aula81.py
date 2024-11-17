lista = [
    {'nome': 'Victor', 'sobrenome': 'Lemes'},
    {'nome': 'Ana', 'sobrenome': 'Souza'},
    {'nome': 'Bianca', 'sobrenome': 'Augusto'},
    {'nome': 'Thiago', 'sobrenome': 'Camargo'},
    {'nome': 'Alex', 'sobrenome': 'Pimentel'},
    {'nome': 'Gustavo', 'sobrenome': 'Oliveira'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)