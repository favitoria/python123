n = str((input('Digite um número entre 1000 - 9999: ')))
n1 = '-'.join(n)
n2 = n1.replace('-', ' ')
n3 = n2.split()
print('unidade: {}'.format(n3 [3]))
print('dezena: {}'.format(n3 [2]))
print('centena: {}'.format(n3 [1]))
print('milhar: {}'.format(n3 [0]))

num = int(input('Informe um número: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Analizando o número {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
