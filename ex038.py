v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
if v1 > v2:
    print('O primeiro valor {} é o maior'.format(v1))
elif v2 > v1:
    print('O segundo valor {} é o maior'.format(v2))
else:
    print('NÃO EXISTE um valor maior, os dois são iguais')