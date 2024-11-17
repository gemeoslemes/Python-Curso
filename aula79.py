import copy

d1 = {
    'c1': 1,    
    'c2': 2,
    'lista': [1,2,3],  
}

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Lemes'
}

d2 = d1.copy()

d2['c1'] = 1000
d2['lista'][1] = 99999

print(d1)
print(d2)

print()
print(pessoa.get('nome', 'Não existe'))

#ultima = pessoa.popitem()
#print(ultima)
print(pessoa)

#pessoa.update({
#   'nome': "Victor Gêmeos", 
#    'idade': 21
#})

pessoa.update(nome='Victor Gêmeos', idade=21)

print(pessoa)