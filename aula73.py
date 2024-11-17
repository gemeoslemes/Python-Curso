"""
Higher order Functions
Funções de primeira classe
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia!', "Vinicius")
)
print(
    executa(saudacao, 'Bom dia!', "Victor")
)