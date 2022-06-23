import random
from time import sleep
jogo = list()
print('=*=' * 9)
print('    JOGO DA MEGA SENA    ')
print('=*=' * 9)
resposta = int(input('Quantos jogo você quer que eu sorteie? '))
print(f'-=-=-=-=- SORTEANDO {resposta} JOGOS -=-=-=-=-')
for c in range(0, resposta):
    while True:
       numeros = random.randint(1, 61)
       if numeros not in jogo:
        jogo.append(numeros)
        if len(jogo) == 6:
                break
    print(f'Jogo {c+1}: {jogo}')
    sleep(1)
    jogo.clear()


