class Caneta:
    def __init__(self, cor, cor_tampa):
        self._cor = cor
        self._cor_tampa = cor_tampa

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul', 'Azul claro')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Pink'

print(caneta.cor)
print(caneta.cor_tampa)