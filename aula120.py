# string = "Victor"
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Victor', 'Lemes')
print(p1.nome)
print(p1.sobrenome)