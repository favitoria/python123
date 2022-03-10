palavras = ('BRINCADEIRA', 'PAO', 'ESTUDOS','AVIAO',
            'BICICLETA', 'PYTHON','AMOR', 'ODIO', 'FUTURO',
            'CADERNO', 'MAE', 'BARCO')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for vogais in p:
        if vogais in 'AEIOU':
            print(vogais, end=' ')
