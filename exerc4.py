nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome != '' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'seu nome tem {len(nome)} letras')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else: 
        print('Seu nome não contém espaços')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios")