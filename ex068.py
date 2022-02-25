from time import sleep
import random
par = impar = cont = soma = 0
while True:
    print('-==-' * 13)
    print('VAMOS JOGAR PAR OU ÍMPAR!')
    print('-==-' * 13)
    Pjogador = str(input('Qual a sua escolha [I = ímpar, P = par]? ')).upper()
    Ncomputador = random.randint(0, 10)
    Njogador = int(input('Digite quantos dedos vai jogar: '))
    soma = Ncomputador + Njogador
    print('3..')
    sleep(0.5)
    print('2..')
    sleep(0.5)
    print('1..')
    print(f'O computador jogou {Ncomputador} e você {Njogador} dando um total de {soma}')
    if soma % 2 == 0:
        print('O número é PAR!')
        if Pjogador in 'p, P':
            print('VOCÊ GANHOU!!')
            cont += 1
        else:
            print('VOCÊ PERDEU!!')
            break
    else:
        print('O número é ÍMPAR!')
        if Pjogador in 'I, i':
            print('VOCÊ GANHOU!!!')
            cont += 1
        else:
            print('VOCÊ PERDEU!!')
            break
print(f'FIM DO JOGO! Total de vitórias foi de {cont}!')