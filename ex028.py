import random
from time import sleep
pensado = random.randint(0,5)
print('-=-'*20)
num = int(input('Estou pensando em um número entre 0-5..\nConsegue adivinhar qual é?'))
print('PROCESSANDO...')
sleep(2)
if num == pensado:
    print('QUE GENIAL! VOCÊ ACERTOU!')
    print('-=-' * 20)
else:
    print('TENTE OUTRA VEZ AMIGO!')
    print('-=-' * 20)
print('----------------------FIM-DO-JOGO---------------------------')