resposta = 'Ss'
num = []
while resposta != 'N':
    valores = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar [S/N]? '))
    num.append(valores)
print(f'A lista é: {num}')
print(f'Foram digitados: {len(num)} números.')
num.sort(reverse=True)
print(f'A lista em decrescente é: {num}')
if 5 in num:
    print('O valor 5 FAZ parte da lista!')
else:
    print('O valor 5 NÃO FAZ parte da lista!')
