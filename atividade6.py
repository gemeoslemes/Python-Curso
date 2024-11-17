def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mutiplicacao = multiplica(10,2,3,4,5)
print(mutiplicacao)

def par_impar(numero):
    multiplo_por_dois = numero % 2 == 0
    if multiplo_por_dois:
        return f'{numero} é par!'
    return f'{numero} é ímpar!'

print(par_impar(13))
print(par_impar(2))
print(par_impar(9))
print(par_impar(65))
print(par_impar(72))