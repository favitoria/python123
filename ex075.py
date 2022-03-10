num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')), int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))
print(f'O valor 9 apareceu: {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 FOI digitado na {num.index(3) +1}º posição')
else:
    print(f'O valor 3 NÃO FOI digitado nenhuma vez')
print('Os valores pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
