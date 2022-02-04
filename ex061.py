n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite agora a sua razão: '))
c = 0
while c != 10:
    c += 1
    pa = n + (c - 1) * r
    print('{}'.format(pa), end=' ➸ ')
print('FIM')


