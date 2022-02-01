a = 0
a1 = 0
for c in range(1,8):
    ano = int(input('Digite um ano de nascimento: '))
    idade = 2022 - ano
    if idade <= 21:
        a = a + 1
    elif idade > 21:
        a1 = a1 + 1
print('{} são maiores de 21 anos, já {} ainda não atingiram a maioridade'.format(a, a1))