import math
from time import sleep
'''num = 0
while num != 0.5:
    num = int(input('Digite um número inteiro para saber seu fatorial: '))
    print('{}! é igual à: {}'.format(num, math.factorial(num)))'''
num = int(input('Digite um número inteiro para saber seu fatorial: '))
c = num
f = 1
print('CALCULANDO O FATORIAL {}!...'.format(num))
sleep(1)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))