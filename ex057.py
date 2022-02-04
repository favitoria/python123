sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Diga seu sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dados inválidos!')
print('Dado {} salvo!'.format(sexo))
