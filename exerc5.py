numero = input("Informe um número: ")

if '.' in numero:
    print('Este número não é inteiro')
else:
    numero_a_verificar = int(numero)
    if numero_a_verificar % 2 == 0:
        print(f'o número {numero_a_verificar} é par')
    else:
        print(f'o número {numero_a_verificar} é impar')


