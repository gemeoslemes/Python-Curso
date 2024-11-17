pessoa = {}

chave = 'nome'

pessoa[chave] = 'Victor Lemes'
pessoa['sobrenome'] = 'Oliveira'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa[chave])

print(pessoa[chave])

if pessoa.get('sobrenome') is  None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
