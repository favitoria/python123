from time import sleep
import emoji
print('FALTAM APENAS 10 SEGUNDOS!!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('FELIZ ANO NOVOOOO!!!!'))
print(emoji.emojize('BUM! BUM! POOOW!:fireworks::sparkler:', use_aliases=True))