def create_function(fun):
    def interna(*args, **kwargs):
        print("Vou te decorar!")
        for arg in args:
            is_string(arg)
        print("OK, agora você foi decorada.")
        resultado = fun(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        return resultado
    return interna

@create_function
def invert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')

invertida = invert_string("123")
print(invertida)