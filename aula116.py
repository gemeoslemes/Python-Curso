caminho_completo = 'C:\\Users\\victo\\OneDrive\\Desktop\\Python - Curso\\'
caminho_completo += 'aula116.txt'

# arquivo = open(caminho_completo, 'w')

# arquivo.close()

# with open(caminho_completo, 'w+') as arquivo:
#     arquivo.write("Linha 1\n")
#     arquivo.write("Linha 2\n")
#     arquivo.writelines(
#         ('linha 3\n', 'linha 4\n')
#     )
#     arquivo.seek(0, 0)

#     print(arquivo.read())
#     print("Lendo")

#     arquivo.seek(0, 0)
#     print(arquivo.readline().strip())
#     print(arquivo.readline())
#     print("READ LINES")

    
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
    
#     print()

# with open(caminho_completo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_completo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Linha 4\n')