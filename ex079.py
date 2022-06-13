resposta = 'Ss'
num = list()
while True:
    n = int(input('DIGITE UM VALOR: '))
    if n not in num:
        num.append(n)
    else:
        print('VALOR DUPLICADO!')
    r = str(input('Quer continuar [S/N]? '))
    if r in 'nN':
        break
print('FIM! Esses foram os valores adicionados na lista: ')
print(sorted(num))

