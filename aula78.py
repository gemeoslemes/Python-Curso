'''
Métodos úteis dos dicionários em Python
'''

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Lemes'
}

#print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

#for chave in pessoa:
#   print(chave)

for chave, valor in pessoa.items():
    print(chave, valor)


pessoa.setdefault('idade', None)
print(pessoa['idade'])