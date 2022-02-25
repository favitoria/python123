resposta = ''
cont = maioridade = homens = mulheres = mulher20 = 0
print('==== CADASTRE UMA PESSOA ====')
while resposta in 'S,s':
    cont += 1
    print(f'--------- {cont}º PESSOA ---------')
    sexo = str(input('SEXO [M/F]: '))
    idade = int(input('IDADE: '))
    resposta = str(input('Quer continuar? [S/N]')).upper()
    if idade >= 18:
        maioridade += 1
    if sexo in 'M,m':
        homens += 1
    if sexo in 'F,f':
        mulheres += 1
    if sexo in 'F,f' and idade < 20:
        mulher20 += 1
print(f'No total temos {maioridade} maiores de 18 anos!')
print(f'Com {homens} homens cadastrados!')
print(f'E {mulheres} mulheres cadastradas, sendo {mulher20} menores de 20 anos')
