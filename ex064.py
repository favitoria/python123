soma = 0
cont = 0
num = int(input('Digite um número [999 para parar] : '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar] : '))
print('Você digitou no total {} números antes do flag (999)!'.format(cont))
print('A soma de todos eles (desconsiderando o flag) é de: {}'.format(soma))