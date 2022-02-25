resposta = 'S, s'
produto = ''
preço = 0
total = 0
mais1000 = 0
prodbarato = ''
maisbarato = 0
print('=-=-=-=-=-=-=LOJINHA HIHI=-=-=-=-=-=-=')
while resposta in 'S, s':
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    resposta = str(input('Comprou algo mais [S/N]? '))
    total += preço
    if preço > 1000:
        mais1000 += 1
    if maisbarato < preço:
        maisbarato = preço
        prodbarato = produto
print(f'TOTAL DA COMPRA: R${total:.2f}')
print(f'Cerca de {mais1000} produtos custam MAIS de R$1000.00')
print(f'O nome do produto mais caro é {prodbarato}')
