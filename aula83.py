pessoa = {
    'nome': 'Rosana',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 27,
    'altura': 1.68
}
pessoa_com_dados = {**pessoa, **dados_pessoa}

print(pessoa_com_dados)

def mostrar_qlq_coisa(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

#mostrar_qlq_coisa(nome="Bruno", idade=23)
mostrar_qlq_coisa(**pessoa_com_dados)



