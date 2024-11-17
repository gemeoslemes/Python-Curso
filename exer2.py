nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura: exemplo(1.80) "))
peso = float(input('Informe seu peso: exemplo(65.5) '))
imc = peso / (altura **2)
traco = "-"*10
print(traco + "IMC" + traco)

print(f"Olá {nome} seu IMC é: {imc:.2f}")