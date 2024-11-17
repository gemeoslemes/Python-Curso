class Animal:
    def __init__(self, nome):
        self.nome = nome
        variavel = 'valor'
        print(f'{variavel}')


leao = Animal('Leão')
print(leao.nome)