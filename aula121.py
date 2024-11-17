# Métodos em instâncias de classes Python
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O carro {self.nome} está acelerando!')


fusca = Carro('Fusca')
fusca.acelerar()