"""
Closure e funções que retornam outras funções 
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!' 
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Victor'))
print(falar_boa_noite('Victor'))

for nomes in ['Vinicius', 'Nucoly', 'Bianca', 'José']:
    print(falar_bom_dia(nomes))
    print(falar_boa_noite(nomes))