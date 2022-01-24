ano = int(input('Qual o ANO que você nasceu? '))
idade = 2022 - ano
print('Quem nasceu no ano {} tem {} anos de idade!'.format(ano, idade))
if idade == 18:
    print('Deve se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda não tem 18 anos! Faltam {} anos para se alistar!'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))
else:
    print('RESPOSTA INVÁLIDA')