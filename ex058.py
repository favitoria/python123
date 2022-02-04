import random
from time import sleep
pensadorC = random.randint(0, 11)
num = 1
c = 0
while num != pensadorC:
    print('-=-' * 20)
    num = int(input('Estou pensando em um número de 0-10...\nEm qual número eu pensei: '))
    print('PROCESSANDO..')
    sleep(1)
    c += 1
    if num != pensadorC:
        if num < pensadorC:
            print('MAIS... TENTE OUTRA VEZ AMIGO!')
        if num > pensadorC:
            print('MENOS... TENTE OUTRA VEZ AMIGO!')
print('QUE GENIAL! VOCÊ ACERTOU!')
print('Você digitou {} vezes até acertar!!'.format(c))
print('----------------------FIM-DO-JOGO---------------------------')
