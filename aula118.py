def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []

    lista.append(nome)
    return lista

lista1 = []

clientes1 = adiciona_clientes('Victor', lista1)
adiciona_clientes('Bianca', clientes1)
adiciona_clientes('Renan', clientes1)
clientes1.append('Julia')

clientes2 = adiciona_clientes('Gustavo')
adiciona_clientes('Maria', clientes2)

clientes3 = adiciona_clientes('Marcos')
clientes3.append('Viviane')

print(clientes1)
print(clientes2)
print(clientes3)