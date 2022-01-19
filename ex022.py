nc = str(input('Digite seu nome completo:')).strip()
print('Maisculo: {}'.format(nc.upper()))
print('Minusculo: {}'.format(nc.lower()))
print('Total de letras: {}'.format(len(nc.replace(' ', ''))))
dividido = nc.split()
print('Total de letras do primeiro nome: {}'.format(len(dividido[0])))

nc2 = str(input('Digite seu nome completo:')).strip()
print('Maisculo: {}'.format(nc2.upper()))
print('Minusculo: {}'.format(nc2.lower()))
print('Total de letras: {}'.format(len(nc2) - nc2.count(' ')))
print('Total de letras do primeiro nome: {}'.format(nc2.find(' ')))

