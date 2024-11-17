def parametros_decorador(nome): 
    def decorador(fun):
        print("Decorator:", nome)

        def nova_funcao(*args, **kwargs):
            res = fun(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return nova_funcao
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def somar(x, y):
    return x + y


dez_mais_cinco = somar(10, 5)
print(dez_mais_cinco)
