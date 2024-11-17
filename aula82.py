def executa(funcao, *args):
    return funcao(*args)

def soma(x, y): 
    return x + y

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

