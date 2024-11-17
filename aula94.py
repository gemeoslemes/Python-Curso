try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as error:
    print('Nome:',error.__class__.__name__)
else:
    print("Não deu erro")
finally:
    print('FECHAR ARQUIVO')