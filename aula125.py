from datetime import datetime, timedelta

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
         ano_atual = datetime.today().year
         return ano_atual - self.idade
    

p1 = Pessoa('Victor', 21)
print(p1.get_ano_nascimento())
# p1.nome = 'Lemes'
# del p1.nome
print(p1.__dict__)
print(vars(p1))