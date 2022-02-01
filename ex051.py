print('='* 30)
print('10 TERMOS DE UMA PA')
print('='* 30)
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite agora a sua razão: '))
for pa in range(1,11):
    x = n + (pa - 1) * r
    print('{}'.format(x), end=' ➸ ')
print('Esses são os 10 primeiros termos desta progressão!')
