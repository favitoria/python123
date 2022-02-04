v1 = 0
v2 = 0
menu = 0
while menu != 5:
    print('-=-' * 20)
    v1 = int(input('Digite um número inteiro: '))
    v2 = int(input('Digite um número inteiro: '))
    menu = int(input('MENU\n[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - NOVOS NÚMEROS\n[5] - SAIR\nRESPOSTA: '))
    print('-=-' * 20)
    if menu == 1:
        soma = v1 + v2
        print('A soma de {} + {} é: {}'.format(v1, v2, soma))
    elif menu == 2:
        multiplicar = v1 * v2
        print('O produto de {} * {} é: {}'.format(v1, v2, multiplicar))
    elif menu == 3:
        maior = 0
        if v1 > v2:
            maior = v1
            print('O maior valor entre {} e {}, é: {}'.format(v1, v2, maior))
        elif v1 < v2:
            maior = v2
            print('O maior valor entre {} e {}, é: {}'.format(v1, v2, maior))
        elif v1 == v2:
            print('O número {} e {} são iguais!'.format(v1, v2))
    elif menu == 4:
        print('Recomeçando...')
    else:
        print('OPÇÃO INVÁLIDA')
print('--FIM--')


