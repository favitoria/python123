r = 'Ss'
média = cont = soma = 0
maior = 0
menor = 0
while r in 'Ss':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    cont += 1
    soma += n
    média = soma / cont
    if n > maior:
        maior = n
    if n < maior:
        menor = n
print('A média entre os números digitados é {:.2f}'.format(média))
print('O maior número informado foi {} e o menor foi {}'.format(maior, menor))

