n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite agora a sua razão: '))
c = 1
termo = n
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}  ➸ '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer? '))
print('Progressão finalizada com {} termos mostrados'.format(total))




