somaidade = 0
médialidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulheres = 0
for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = (str(input('Nome: '))).strip()
    idade = (int(input('Idade: ')))
    sexo = (str(input('Sexo [M/F]: '))).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulheres += 1
médialidade = somaidade /4
print('A média de idade do grupo informado é {}'.format(médialidade))
print('O homem mais velho têm {} anos e se chama: {}'.format(maioridadehomem, nomevelho))
print('Temos {} mulheres com menos de 20 anos'.format(totalmulheres))