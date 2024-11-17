class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def method_class(cls):
        print("Hey")

    @classmethod
    def created_with_50_year(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def created_anonimo(cls, idade):
        return cls('Anônimo', idade)

p1 = Pessoa('Victor', 21)
p2 = Pessoa.created_with_50_year('Bianca')
p3 = Pessoa.created_anonimo(24)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
# print(Pessoa.ano)
# Pessoa.method_class()