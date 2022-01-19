from datetime import date
ano = int(input('Digite algum ano, caso queira que seja o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} digitado é bissexto!'.format(ano))
else:
    print('O ano {} digitado não é bissexto'.format(ano))