from time import sleep
import random
print('-=-' * 7)
print('Vamos jogar JOKENPÔ!')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
J1 = random.choice(lista)
print('-=-' * 7)
sleep(1)
J2 = (input('PEDRA\nTESOURA\nPAPEL\nESCOLHA UM: ')).upper()
print('-=-' * 7)
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=-' * 7)
sleep(1)
if J1 == J2:
    print(J1)
    print('EMPATE')
elif J1 == 'PEDRA' and J2 == 'PAPEL':
    print('Computador jogou PEDRA!')
    print('Você GANHOU!')
elif J1 == 'PEDRA' and J2 == 'TESOURA':
    print('Computador jogou PEDRA!')
    print('Você PERDEU!')
elif J1 == 'PAPEL' and J2 == 'TESOURA':
    print('Computador jogou PAPEL!')
    print('Você GANHOU!')
elif J1 == 'PAPEL' and J2 == 'PEDRA':
    print('Computador jogou PAPEL!')
    print('Você PERDEU!')
elif J1 == 'TESOURA' and J2 == 'PEDRA':
    print('Computador jogou TESOURA!')
    print('Você GANHOU!')
elif J1 == 'TESOURA' and J2 == 'PAPEL':
    print('Computador jogou TESOURA!')
    print('Você PERDEU!')
else:
    print('OPÇÃO INVÁLIDA')
print('-=-FIM-=-' * 2)
