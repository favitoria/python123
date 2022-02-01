s = 0
cont = 0
for c in range(1,7):
    num = float(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num
        cont += 1
print('A soma de todos os {} valores pares é {}'.format(cont, s))