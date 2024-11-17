pessoa = {
    'nome': 'Victor',
    'sobreNome': 'Lemes',
    'idade': 21,
    'altura': 1.75,
    'endereços': [
        {'rua': 'tal tal', 'numero': 120},
        {'rua': 'NOVA', 'numero': 123}
    ]
}

#print(pessoa, type(pessoa))

print(pessoa['nome'])
print(pessoa['sobreNome'])
print()

for chaves in pessoa:
    print(chaves, pessoa[chaves])